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

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("Received %s" % (body,))

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

# loop forever
channel.start_consuming()
