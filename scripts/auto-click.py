import time, threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

class ClickMouse(threading.Thread):
	"""
	Thread used to control autoclicker
	"""

	def __init__(self, delay: float, include_right: bool):
		"""
		delay: sleep delay for event monitoring
		is_active: autorun status
		is_running: program status
		"""
		super(ClickMouse, self).__init__()
		self.delay = delay
		self.include_right = include_right
		self.is_active = False
		self.is_running = True

	def start_clicking(self):
		self.is_active = True
		print("autoclicker activated")

	def stop_clicking(self):
		self.is_active = False
		print("autoclicker disabled")

	def exit(self):
		self.stop_clicking()
		self.is_running = False

	def run(self):
		"""
		Main loop that runs if the program and autoclicker are running
		"""
		while self.is_running:
			time.sleep(0.1)

			while self.is_active:
				# mouse.click(self.button)
				# time.sleep(self.delay)

				mouse.press(Button.left)
				if self.include_right: mouse.press(Button.right)
				time.sleep(self.delay / 2)

				mouse.release(Button.left)
				if self.include_right: mouse.release(Button.right)
				time.sleep(self.delay / 2)

def on_press(event_key):
	"""
	event_key: keyboard event key
	"""
	if event_key == AUTORUN_TOGGLE_KEY:
		if click_thread.is_active:
			click_thread.stop_clicking()
		else:
			click_thread.start_clicking()

	# here exit method is called and when
	# key is pressed it terminates auto clicker
	elif event_key == EXIT_PROGRAM_KEY:
		click_thread.exit()
		listener.stop()

if __name__ == '__main__':

	# four variables are created to
	# control the auto-clicker
	DELAY = 0.066
	AUTORUN_TOGGLE_KEY = KeyCode(char='+')
	EXIT_PROGRAM_KEY = KeyCode(char='-')

	# instance of mouse controller is created
	mouse = Controller()
	click_thread = ClickMouse(DELAY, include_right=False)
	click_thread.start()

	with Listener(on_press=on_press) as listener:
		listener.join()
