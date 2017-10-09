import pyjsonrpc

http_client = pyjsonrpc.HttpClient(
	url = "http://localhost:9898",
)


# http_client.notify("add",3,4)
if __name__ == '__main__':
	print http_client.call("add",1,2)
	print http_client.add(1,2)
	assert http_client.add(3,4)==7
