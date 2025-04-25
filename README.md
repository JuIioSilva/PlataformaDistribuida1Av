# Sistema de Monitoramento de Temperatura - SmartCampus

Este é o projeto 1 da cadeira de Sistemas Distribuidos, é um sistema de monitoramento de temperatura para salas de um campus. Ele coleta dados de sensores de temperatura, os processa e exibe em tempo real em um painel web, permitindo o monitoramento remoto e geração de alertas automáticos.
Julio Mateus Costa da silva CC7NA 23070066
## Arquitetura do Sistema

O sistema é composto pelos seguintes componentes principais:

1. **Sensores de Temperatura (Simulados)**: 
   - Sensores geram dados de temperatura aleatórios.
   - Os dados são enviados via UDP para o Gateway.

2. **Gateway**:
   - Recebe os dados dos sensores via UDP.
   - Envia os dados para uma fila RabbitMQ para processamento posterior.

3. **Fila RabbitMQ**:
   - Armazena temporariamente os dados recebidos até serem processados.

4. **Serviço de Análise (gRPC)**:
   - Processa os dados recebidos da fila RabbitMQ.
   - Gera alertas e recomendações de ação com base na temperatura.

5. **Servidor Flask com Socket.IO**:
   - Recebe os dados processados pelo serviço de análise e os envia para o painel web em tempo real via Socket.IO.

6. **Painel Web**:
   - Exibe os dados de temperatura e alertas em tempo real.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para a implementação do servidor, gateway e serviço de análise.
- **gRPC**: Comunicação eficiente entre o servidor de análise e o servidor Flask.
- **RabbitMQ**: Fila de mensagens para comunicação assíncrona entre os componentes.
- **Socket.IO**: Comunicação em tempo real entre o servidor Flask e o frontend.
- **HTML/JavaScript**: Frontend para exibição dos dados em tempo real.