from flask import *
from flask_session import Session
from flask_socketio import *
from models import *
from settings import Settings
import time
import os

app = Flask(__name__)
app.config.from_object(Settings)
db.init_app(app)
Session(app)

socketio = SocketIO(app)
active = []


@app.route('/')
def index():
    return redirect('/chat')


@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        session['name'] = request.form['name'].strip()
        return redirect('/')


@app.route('/chat')
def chat():
    if session.get('name'):
        messages = Message.query.all()
        return render_template('chat.html', messages=messages, active=active)
    else:
        return redirect('/auth')


@socketio.on('connect', namespace='/chat')
def handle_connect():
    name = session['name']
    if name not in active:
        active.append(name)
    emit('active', active, broadcast=True)


@socketio.on('disconnect', namespace='/chat')
def handle_disconnect():
    name = session['name']
    if name in active:
        active.remove(name)
    emit('active', active, broadcast=True)


@socketio.on('message', namespace='/chat')
def handle_send_message(message):
    name = session['name']
    emit('message', {
         'name': name, 'text': message}, broadcast=True)
    new_message = Message(name=name, text=message, time=str(time.time()))
    db.session.add(new_message)
    db.session.commit()
    db.session.close()


@app.route('/logout')
def logout():
    try:
        active.remove(session['name'])
    except:
        pass
    socketio.emit('active', active, broadcast=True)
    session['name'] = None
    return redirect('/')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)
