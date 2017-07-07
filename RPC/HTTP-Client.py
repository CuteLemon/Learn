import pyjsonrpc

http_client = pyjsonrpc.HttpClient(
	url = "http://localhost:9898",
)

print http_client.call("add",1,2)

print http_client.add(1,2)

http_client.notify("add",3,4)
