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
        time.sleep(1)

channel = connection.channel()
channel.queue_declare(queue='random_queue')

while True:
    num_to_send = str(random.randint(0, 10000))
    channel.basic_publish(exchange='', routing_key='random_queue',
                          body=num_to_send)
    print('Sent number', num_to_send)
    time.sleep(2)
