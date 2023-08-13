#!/usr/bin/env python3
# ----------------------------
import json
import signal
from urllib import parse
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.request import HTTPError
#import config.py
import os
import sys
import yaml
import argparse
#import router.py
import re
from urllib.request import urlopen, Request, HTTPError
# ----------------------------
class ServerConfig:
    # Host configuration
    host = '0.0.0.0'
    port = 9999

    # Runtime settings
    working = "."
    plugins = []

    # Optional: Define the default route hander as one of the following
    static = None
    proxy = None

    discover = True
    routes = {}


def GetConfig():
    opts = GetArgs()
    config = ServerConfig()

    # Try and load from config file (if specified)
    if opts.config and os.path.isfile(opts.config):
        ApplyYamlConfig(config, opts.config)

    # Apply and load additional config settings
    ApplyArgs(config, opts)  # <-- Apply CLI args to config
    PrintConfig(config)

    # Apply any CLI args and return the config
    return config


def GetArgs(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description='Extremely simple python server that can be easily be extended.'
    )

    # Core configurations and valiables used by all server types
    parser.add_argument('-c', '--config',
                        dest='config',
                        help='Specify your `config.yaml` file.',
                        )
    parser.add_argument('--host',
                        dest='host',
                        help='Specify the host we will bind the server to',
                        default='0.0.0.0'
                        )
    parser.add_argument('-p', '--port',
                        dest='port',
                        help='serve HTTP requests on specified port (default: 9999)',
                        type=int,
                        default=9999
                        )
    parser.add_argument('-w', '--working',
                        dest='working',
                        help='Specify the working directory',
                        default=os.getenv('WORK_DIR')
                        )

    # Allow the loading of plugins
    parser.add_argument('-a', '--add',
                        dest='plugins',
                        help='List of plugins to load',
                        type=lambda s: [item for item in s.split(',')])

    # Allow the user to specify the type of server that will be created
    parser.add_argument('-s', '--static',
                        dest='static',
                        help='Static web contents to serve, if no other route defined',
                        # Default option: Serve current dir...
                        default=os.getenv('STATIC_DIR', '')
                        )
    parser.add_argument('--proxy',
                        dest='proxy',
                        help='Default route handler will reverse proxy to a URL'
                        )

    # Parse the args provided by the CLI
    args = parser.parse_args(argv)

    return args


def ApplyArgs(config, args):
    for key, val in vars(args).items():
        if val and key != "config":
            setattr(config, key, val)
    return config


def ApplyYamlConfig(config, file):
    with open(file, "r") as stream:
        configDict = yaml.safe_load(stream)
        for key in configDict.keys():
            setattr(config, key, configDict[key])


def printIf(message, value=None):
    if value:
        print(message % value)


def PrintConfig(config):
    print('---------------------------------------------------------')
    print('Starting python server...')
    print('---------------------------------------------------------')
    printIf(' + Work Dir: %s', config.working)
    printIf(' + Live Dir: %s', config.static)
    printIf(' ~ Proxy To: %s', config.proxy)
    print(' - Hostname: http://%s:%s' % (config.host, config.port))
    print('---------------------------------------------------------')




class Serializable:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class WebRequest(Serializable):
    def __init__(self, verb, path, head={}, body=None, params={}):
        self.verb = verb
        self.path = path
        self.head = head
        self.body = body
        self.params = params


class WebResponse(Serializable):
    def __init__(self, verb, path, head, body, status=200):
        self.verb = verb
        self.path = path
        self.status = status
        self.head = head
        self.body = body


class WebRouter:
    routes = {}

    def register(self, routes):
        http = self.routes

        for verb in routes:
            # Create verb entry if not exist
            if not verb in http:
                http[verb] = {}
            for route in routes[verb]:
                action = routes[verb][route]
                http[verb][route] = action
                print('   [ %-5s ] %s' % (verb, route))

    def bind(self, verb, route, action):
        # This method should be extended by a server implementation
        message = "You need to pass the routes to a server implementation.\n"
        message += "Verb: %s, Path: %s\n" % (verb, route)
        raise Exception('FATAL: %s' % message)

    def default(self, verb, path):
        # This method should be extended by a server implementation
        message = "You need to implement the `default(self, verb, path)` function.\n"
        message += "Verb: %s, Path: %s\n" % (verb, path)
        raise Exception('FATAL: %s' % message)
        
    def route(self, verb, path):
        def decorator(action):
            self.register({verb: {path: action}})
        return decorator

    def head(self, path):
        return self.route("HEAD", path)

    def get(self, path):
        return self.route("GET", path)

    def post(self, path):
        return self.route("POST", path)

    def put(self, path):
        return self.route("PUT", path)

    def patch(self, path):
        return self.route("PATCH", path)

    def delete(self, path):
        return self.route("DELETE", path)

    def find(self, verb, path):
        if not self.routes or not verb in self.routes:
            return None
        matched = [r for r in self.routes[verb] if re.search(r, path)]
        if len(matched) > 0:
            return matched[0]  # Return the first match
        else:
            return None

    def reply(self, verb, path, ctx):
        # See if we can match a route to the current verb
        route = self.find(verb, path)
        if route:  # route has been matched, execute action
            handler = self.routes[verb][route]
            # Wrap the action into a standard request-response model
            action = self.bind(verb, path, handler)
        else:  # No route defined, use default handler
            action = self.default(verb, path)
        return action(ctx)

    def proxy(self, url, req):
        if not url:
            raise Exception("FATAL: No proxy URL has been set up.")

        url = '{}{}'.format(url, req.path)
        print(' ~ Proxy me: %s' % url)

        # Populate the new request with the headers that was requested from client
        headers = {}
        for key in req.head:
            name = key.lower()
            value = req.head[key]
            if name == "host":  # <-- Trick endpoint into thinking its a direct call
                proxy_host = url.replace('http://', '')
                proxy_host = proxy_host.replace('https://', '')
                proxy_host = proxy_host.replace('localhost', '127.0.0.1')
                proxy_host = proxy_host.split('/')[0]
                value = proxy_host
                pass
            if name.startswith('x-') or name.startswith('sec-') or name in (
                'connection',
                'user-agent'
            ):
                pass  # <-- Filtering out noise and tracers we dont need
            else:
                headers[key] = value

        # Create a new request handler, then fetch the response via a proxied request
        req = Request(url, headers=headers)
        resp = urlopen(req)
        return resp






class Request(WebRequest):
    # Wrap your request object into serializable object
    def __init__(self, ctx): super().__init__(
        verb=ctx.command,
        path=ctx.path,
        head=self.headers(ctx),
        body=self.body(ctx) if ctx.command in ["POST", "PUT"] else None,
        params=self.query(ctx),
    )

    def headers(self, ctx):
        head = {}
        for key in ctx.headers:
            head[key.lower()] = ctx.headers.get(key)
        return head

    def query(self, ctx):
        path_parts = ctx.path.split('?')
        if len(path_parts) > 1:
            return parse.parse_qs(path_parts[1])
        return {}

    def body(self, ctx):
        # Only try and parse the body for known methods (eg: POST, PUT)
        ctype = self.head['content-type'] if 'content-type' in self.head else 'application/json'
        length = int(ctx.headers.get('content-length'))
        match ctype:
            case 'application/json':
                input = ctx.rfile.read(length).decode('utf8')
                data = json.loads(input)
            case 'application/x-www-form-urlencoded':
                input = ctx.rfile.read(length).decode('utf8')
                form = parse.parse_qs(input, keep_blank_values=1)
                data = {}
                for key in form:
                    if len(form[key]) > 1:
                        data[key] = form[key]
                    elif len(form[key]) == 1:
                        data[key] = form[key][0]
            case _:
                message = 'Content type "%s" cannot be parsed into a body.' % ctype
                raise Exception(message)

        return data


class Response(WebResponse):
    __sent = False

    # Wrap your response object into serializable object
    def __init__(self, ctx, req): super().__init__(
        verb=ctx.command,
        path=ctx.path,
        head={},
        body=None
    )

    def encoder(self): return self.__dict__

    def respond(self, ctx, status=200, headers={}, message=""):
        if self.__sent:
            raise Exception('Headers already sent')
        self.__sent = True

        # Finilize the headers
        ctx.send_response(status, message)
        for key in headers:  # Append headers
            self.head[key] = headers[key]
        for key in self.head:
            ctx.send_header(key, self.head[key])
        ctx.end_headers()

    def redirect(self, ctx, location):
        self.respond(ctx, 302, {
            'Location': location
        })

    def reply(self, ctx, body={}):
        ctype = self.head['content-type'] if 'content-type' in self.head else 'application/json'
        data = None
        match ctype:
            case 'application/json':  # Send a JSON response
                data = json.dumps(body, default=self.encoder)
            case 'application/x-www-form-urlencoded':  # Redirect to GET route after post by default
                self.redirect(ctx, ctx.path)

        # Reply with headers (if not already sent)
        if not self.__sent:
            self.respond(ctx, 200)

        # Send the response UTF encoded (if defined)
        if data:
            ctx.wfile.write(data.encode('utf8'))


class Handler(SimpleHTTPRequestHandler):
    # Bind your route handlers into our router's path resolvers
    def __init__(self, server, *extra_args, **kwargs):
        self.reply = server.reply
        self.config = server.config
        self.proxy = server.proxy
        super().__init__(directory=server.config.static, *extra_args, **kwargs)

    def do_DEFAULT(self, verb):
        # If no custom routes were triggered, this function will be called..
        # We will check for default actions in this order:
        #  1) config.proxy  - (URL)  Proxy the request
        #  2) config.static - (PATH) Serve static content
        #  3) Fallback: Send "Not found"
        if self.config.proxy:
            return self.do_PROXY(verb, self.config.proxy)
        elif verb == "GET" and self.config.static:
            # Serve contents from the specified static folder
            return self.do_STATIC()
        else:
            # The default action is to reply: "Not found"
            self.send_response(404, "Not Found")
            self.end_headers()

    def do_REPLY(self, verb): self.reply(verb, self.path, self)
    def do_STATIC(self): super().do_GET()
    def do_HEAD(self): self.do_GET()
    def do_GET(self): self.do_REPLY("GET")
    def do_POST(self): self.do_REPLY("POST")
    def do_PUT(self): self.do_REPLY("PUT")
    def do_PATCH(self): self.do_REPLY("PATCH")
    def do_DELETE(self): self.do_REPLY("DELETE")

    def do_PROXY(self, verb, proxy):
        # Wrap the generic proxy request and handle response to client
        def failed(status, message):
            print(' ! Error <-- [ %s ] %s' % (status, message))
            self.send_error(status, message)
        try:
            # Create a new request handler, then fetch the response via a proxied request
            res = self.proxy(proxy, Request(self))
            if not res:
                return

            # Forward the response to the client that is waiting for it
            self.send_response(res.getcode())
            for key in res.headers:
                self.send_header(key, res.headers[key])
            self.end_headers()
            self.wfile.write(res.read())
            res.close()
        except HTTPError as e:
            failed(599, 'Proxy Error: {}'.format(str(e)))
        except IOError as e:
            failed(404, 'IO Error: {}'.format(str(e)))
        except Exception as e:
            failed(503, 'error trying to proxy: {}'.format(str(e)))


class WebServer(WebRouter):
    app = None
    config = None

    def __init__(self, config=GetConfig()):
        self.config = config
        self.host = (config.host, config.port)

        # Create a new server instance that will be serving our routes
        self.app = HTTPServer(self.host, partial(Handler, self))

        # Bind the routes that was declared in the config file
        if config.routes:
            self.register(config.routes)

    def static(self, path):
        self.config.static = path

    def start(self):
        if not self.app:
            raise Exception("FATAL: App instance for server not set.")

        # Gracefully handle shutdowns
        signal.signal(signal.SIGINT, self.onExit)

        # Start the server using the target (request handler) type
        self.app.serve_forever()

    def bind(self, verb, route, action):
        def reply(ctx):
            # Service the incomming request
            req = Request(ctx)
            resp = Response(ctx, req)
            result = action(req, resp)

            # Set the response header and status
            resp.respond(ctx, resp.status, resp.head)

            # Write the body of the response
            if result:
                resp.reply(ctx, body=result)

            return result

        return reply

    def default(self, verb, path):
        def reply(ctx): ctx.do_DEFAULT(verb)
        return reply

    def discover(self, path="./routes"):
        print(' - Auto discovering routes in: %s' % path)

    def onExit(signum, frame): return exit(1)


def main():
    app = WebServer()
    app.discover()  # By default we auto discover the routes...
    app.start()


if __name__ == '__main__':
    main()
# ----------------------------
