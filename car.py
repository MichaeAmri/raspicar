import RPi.GPIO as GPIO


class Car:

	def __init__(self, l_wheel, r_wheel):

		self.l_wheel = l_wheel
		self.r_wheel = r_wheel

	def forward(self):

		self.l_wheel.move_forward()
		self.r_wheel.move_forward()

	def backward(self):

		self.l_wheel.move_backward()
		self.r_wheel.move_backward()

	def left(self):

		self.l_wheel.move_backward()
		self.r_wheel.move_forward()

	def right(self):

		self.l_wheel.move_forward()
		self.r_wheel.move_backward()

	def stop(self):

		self.l_wheel.stop()
		self.r_wheel.stop()



class Wheel:

	def __init__(self, forward, backward, pwm):

		self.forward = forward
		self.backward = backward
		self.pwm = pwm

		GPIO.setup(self.forward, GPIO.OUT)
		GPIO.setup(self.backward, GPIO.OUT)
		GPIO.setup(self.pwm, GPIO.OUT)

	def stop(self):

		GPIO.output(self.pwm, GPIO.LOW)
		GPIO.output(self.forward, GPIO.LOW)
		GPIO.output(self.backward, GPIO.LOW)

	def move_forward(self):

		GPIO.output(self.pwm, GPIO.HIGH)
		GPIO.output(self.forward, GPIO.HIGH)
		GPIO.output(self.backward, GPIO.LOW)

	def move_backward(self):

		GPIO.output(self.pwm, GPIO.HIGH)
		GPIO.output(self.forward, GPIO.LOW)
		GPIO.output(self.backward, GPIO.HIGH)


# setup
GPIO.setmode(GPIO.BCM)
left_wheel = Wheel(5, 6, 12)
right_wheel = Wheel(19, 16, 13)
car = Car(left_wheel, right_wheel)
