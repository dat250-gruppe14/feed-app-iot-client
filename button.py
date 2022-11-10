import RPi.GPIO as GPIO

class IoTButtons:
	bouncetime = 150

	def __init__(self, event_maps):
		GPIO.setmode(GPIO.BCM)
		self.set_events(event_maps)

	def set_events(self, event_maps):
		for pin_number, event_function in event_maps:
			GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
			GPIO.remove_event_detect(pin_number)
			GPIO.add_event_detect(pin_number, GPIO.RISING, callback=event_function, bouncetime=self.bouncetime)

	def __del__(self):
		print('cleanup')
		GPIO.cleanup()

