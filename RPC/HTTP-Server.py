import pyjsonrpc

class RequestHandler(pyjsonrpc.HttpRequestHandler):

	@pyjsonrpc.rpcmethod
	def add(self,a,b):
		print "add fxn is called with %f and %f" % (a,b)
		return a+b

http_server = pyjsonrpc.ThreadingHttpServer(
	server_address = ('localhost',9898),
	RequestHandlerClass = RequestHandler
)

print "serving HTTP server at http://localhost:9898"

http_server.serve_forever()
