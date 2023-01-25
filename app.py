from flask import Flask, render_template
from car import*

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/forward')
def forward():
	print('forward')
	car.forward()
	return 'ok'

@app.route('/backward')
def backward():
	print('backward')
	car.backward()
	return 'ok'

@app.route('/stop')
def stop():
	print('stop')
	car.stop()
	return 'ok'

@app.route('/left')
def left():
	print('left')
	car.left()
	return 'ok'

@app.route('/right')
def right():
	print('right')
	car.right()
	return 'ok'



if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
