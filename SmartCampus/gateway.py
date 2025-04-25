import pika
import json
import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

# Testar a conexão com o RabbitMQ antes de publicar
try:
    conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    canal = conexao.channel()
    canal.queue_declare(queue='fila_sensores')  # Cria a fila se não existir
    print("[Gateway] Conexão com o RabbitMQ bem-sucedida!")
except pika.exceptions.AMQPConnectionError as e:
    print(f"[Gateway] Falha na conexão com o RabbitMQ: {e}")

print("[Gateway] Aguardando dados UDP...")

while True:
    dados, addr = sock.recvfrom(1024)
    mensagem = dados.decode()
    print(f"[Gateway] Recebido de {addr}: {mensagem}")
    canal.basic_publish(exchange='', routing_key='fila_sensores', body=mensagem)
    print("[Gateway] Mensagem publicada na fila 'fila_sensores'.")
