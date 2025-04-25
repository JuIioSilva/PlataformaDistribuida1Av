import pika
import json
import grpc
import analise_pb2
import analise_pb2_grpc
from app import socketio  # Aqui, você importa o socketio do app Flask

canal_grpc = grpc.insecure_channel('localhost:50051')
stub = analise_pb2_grpc.ServicoAnaliseStub(canal_grpc)


def processar_dados(ch, method, properties, body):
    print("[Consumidor] Mensagem recebida da fila.")
    dados = json.loads(body)
    print(f"[Consumidor] Dados recebidos: {dados}")
    sala = dados.get("sala")
    temperatura = dados.get("temperatura")

    resposta = stub.AnalisarTemperatura(
        analise_pb2.DadosSensor(sala=sala, temperatura=temperatura)
    )

    print(f"[gRPC] Resposta: {resposta.alerta} | Ação: {resposta.acao_recomendada}")

    # Emitir dados para o Socket.IO, que atualizará o front-end
    socketio.emit('atualizar_dados', {
        "sala": sala,
        "temperatura": temperatura,
        "alerta": resposta.alerta
    })

    # Confirma o processamento da mensagem
    ch.basic_ack(delivery_tag=method.delivery_tag)


conexao = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
canal = conexao.channel()
canal.queue_declare(queue='fila_sensores')

canal.basic_consume(queue='fila_sensores',
                    on_message_callback=processar_dados,
                    auto_ack=False)

print('[Consumidor] Aguardando mensagens...')
canal.start_consuming()
