import sys
import keyboard
from pyHS100 import SmartPlug
from pprint import pformat as pf 
from datetime import datetime
from csv import writer

ip = sys.argv[1]
plug = SmartPlug(ip)
print("Harware: %s" % pf(plug.hw_info))

while True:
	try:
		if keyboard.is_pressed('q'):
			print('You pressed the key')
			break
		else:
			activePower = plug.current_consumption()
			currentTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			list_data = [currentTime,activePower]
			print(list_data)
			with open('powerlog.csv', 'a', newline='') as f_object:
				writer_object = writer(f_object)
				writer_object.writerow(list_data)
				f_object.close()
	except Exception as e:
		print(e.message, e.args)
		break
		