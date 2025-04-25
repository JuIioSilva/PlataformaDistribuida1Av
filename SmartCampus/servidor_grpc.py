from concurrent import futures
import grpc
import analise_pb2
import analise_pb2_grpc

class ServicoAnalise(analise_pb2_grpc.ServicoAnaliseServicer):
    def AnalisarTemperatura(self, request, context):
        alerta = ""
        acao = False
        if request.temperatura > 28.0:
            alerta = "ALERTA: Temperatura alta"
            acao = True
        elif request.temperatura < 18.0:
            alerta = "ALERTA: Temperatura baixa"
            acao = True
        else:
            alerta = "Temperatura normal"
        return analise_pb2.ResultadoAnalise(alerta=alerta, acao_recomendada=acao)

def serve():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    analise_pb2_grpc.add_ServicoAnaliseServicer_to_server(ServicoAnalise(), servidor)
    servidor.add_insecure_port('[::]:50051')
    servidor.start()
    print("[gRPC] Servidor rodando na porta 50051")
    servidor.wait_for_termination()

if __name__ == '__main__':
    serve()
