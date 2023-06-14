from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('images')
def handle_message(message):
    
    # Send the image to all connected clients
    emit('images', {'data': message["image"]}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app,port=5555)
