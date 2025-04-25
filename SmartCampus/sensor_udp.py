import socket
import json
import time
import random

IP_GATEWAY = "127.0.0.1"
PORTA_GATEWAY = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def gerar_dados():
    return {
        "sala": random.choice(["Lab101", "Lab102", "Lab103"]),
        "temperatura": round(random.uniform(20.0, 35.0), 2)
    }

while True:
    dados = gerar_dados()
    mensagem = json.dumps(dados).encode()
    sock.sendto(mensagem, (IP_GATEWAY, PORTA_GATEWAY))
    print(f"[Sensor] Enviado: {dados}")
    time.sleep(5)
