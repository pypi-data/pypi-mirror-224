import pika
import json
import traceback

class BugReports:
    def __init__(self, user, password, host, queue):
        self.__rabbitmq_user = user
        self.__rabbitmq_password = password
        self.__rabbitmq_host = host
        self.__rabbitmq_queue = queue

    def bugReports(self, idProyect, area, title):
        self.__idProyect = idProyect
        self.__area = area
        self.__title = title

        try:
            if not all((self.__rabbitmq_user, self.__rabbitmq_password, self.__rabbitmq_host, self.__rabbitmq_queue)):
                raise ValueError("RabbitMQ credentials not set. Call set_rabbitmq_credentials() first")

            # Establish connection to RabbitMQ
            credentials = pika.PlainCredentials(self.__rabbitmq_user, self.__rabbitmq_password)
            parameters = pika.ConnectionParameters(host=self.__rabbitmq_host, credentials=credentials)
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()

            # Declare the queue 'error_queue' to send the error message
            channel.queue_declare(queue=self.__rabbitmq_queue, durable=True)

            # Get the more detailed description of the exception
            description = f"Descripcion:\n{traceback.format_exc()}"

            body = {
                "idProyecto": self.__idProyect,
                "area": self.__area,
                "titulo": self.__title,
                "description": description
            }
            
            # Send the error message to RabbitMQ
            channel.basic_publish(exchange='', routing_key=self.__rabbitmq_queue, body=json.dumps(body))

            # Close the connection to RabbitMQ
            connection.close()

        except pika.exceptions.AMQPError as e:
            print(f"Error al conectar a RabbitMQ: {e}")

        except Exception as e:
            # If an error occurs while sending the message, just print the error message
            print(f"Error al enviar el mensaje a RabbitMQ: {e}")