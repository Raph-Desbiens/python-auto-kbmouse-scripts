import threading
from pynput.keyboard import Listener, KeyCode, Controller

class AutoRun(threading.Thread):
	"""
	Thread used to control autorunner
	"""

	def __init__(self, delay, autorun_key):
		"""
		delay: sleep delay for event monitoring
		autorun_key: keyboard key to be pressed or released
		is_active: autorun status
		is_running: program status
		"""
		super(AutoRun, self).__init__()
		self.delay = delay
		self.autorun_key = autorun_key
		self.is_active = False
		self.is_running = True

	def start_clicking(self):
		self.is_active = True
		kb.press(self.autorun_key)
		print("w key pressed")

	def stop_clicking(self):
		self.is_active = False
		kb.release(self.autorun_key)
		print("w key released")

	def exit(self):
		self.stop_clicking()
		self.is_running = False

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
	DELAY = 0.1
	AUTORUN_KEY = 'w'
	AUTORUN_TOGGLE_KEY = KeyCode(char='+')
	EXIT_PROGRAM_KEY = KeyCode(char='-')

	kb = Controller()
	click_thread = AutoRun(DELAY, AUTORUN_KEY)
	click_thread.start()

	with Listener(on_press=on_press) as listener:
		listener.join()
