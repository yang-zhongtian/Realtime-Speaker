from flask import Flask, render_template
from flask_socketio import SocketIO
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = '!SPEAKERKEY!'
socketio = SocketIO(app)
history=""
bann=["操","肏","cao","Cao","日","CAO","alert","br",".."]

@app.route('/')
def page():
	return render_template('index.html')

@app.route('/test/')
def test():
	return render_template('nb.html')


def broadcast(text):
	socketio.emit('send',{"data":text},broadcast=True)

def checkban(t):
	for i in bann:
		if i in t:
			return False
	return True

@socketio.on('recieve')
def recieve(jsons):
	deny=0
	jsons = str(jsons)
	if jsons!= history and jsons!="":
		if checkban(jsons):
			#print(jsons)
			broadcast(jsons)
			#history = jsons

if __name__ == '__main__':
	socketio.run(app,host="0.0.0.0",debug=True)