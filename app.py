from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret!')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)
if __name__ == '__main__':
    # Localhost only
    socketio.run(app, debug=True)
else:
    # Production mode on Vercel
    app = socketio.WSGIApp(app)