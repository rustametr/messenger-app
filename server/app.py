from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bruh'

socket = SocketIO(app, cors_allowed_origins="*")


@socket.on('message')
def handle_message(msg):
    print(msg)
    socket.send('ok')

@socket.on("connect")
def connected():
    print("client has connected")

if __name__ == '__main__':
    socket.run(app)