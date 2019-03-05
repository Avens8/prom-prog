import pika
import random
import time

rabbit_params = pika.ConnectionParameters('rabbit', 5672)
print(f"Params: {rabbit_params}")

while True:
	try:
		connection = pika.BlockingConnection(rabbit_params)
		break
	except Exception:
		time.sleep(2)

channel = connection.channel()
channel.queue_declare(queue='random_queue')
consume = lambda ch, meth, head, body: print("Got number", int(body.decode()))
channel.basic_consume(consume, 'random_queue')
channel.start_consuming()
