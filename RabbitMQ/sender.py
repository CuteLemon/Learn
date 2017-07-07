import pika

# remote server IP addr
remote_server_addr = 'a.b.c.d'

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(remote_server_addr,
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.basic_publish(exchange = '',routing_key='hello',body='Hello Cute Rabbit!')

connection.close()
