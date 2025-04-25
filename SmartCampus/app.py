from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segredo123'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print("[Servidor Flask] Cliente conectado.")
    dados_teste = {"sala": "Lab101", "temperatura": 25.0, "alerta": "Temperatura normal"}
    socketio.emit('atualizar_dados', dados_teste)  # Enviar dados de teste ao conectar

# Função para enviar dados dinamicamente (usada no consumidor)
def enviar_dado(dados):
    print(f"[Servidor Flask] Enviando dados para o front-end: {dados}")
    socketio.emit('atualizar_dados', dados)

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=8080, use_reloader=False)
