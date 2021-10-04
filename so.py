#!/bin/bash
import subprocess
import sys
import os
import signal
import argparse
import os.path
import time
import re

from pathlib import Path
from PIL import Image

def Found(file, obj) :
	path = path_rom/obj/file
	
	try:
		j= open(path)

	except FileNotFoundError:
		if (obj == 'roms') :
			path = Path(Found(system,'systems'))			
		else :
			path = Path('/home/pi/marquee/default.png')
	return path


#23
default ='default.png'
display='default'
marquee = 'default'

# Percorso del file Led.txt dove vengono scritte rom e system da emulationstation 
path_file = Path('/mnt/abc/led.txt')
# Directory delle immagini per le rom
path_rom = Path('/home/pi/marquee/')
pipe= subprocess.Popen("/home/pi/rpi-rgb-led-matrix/bindings/python/samples/marquee.py {0}".format(path_rom/'default.png'), preexec_fn=os.setsid, shell=True)					
#ciclo lettura del file

try :   
	while 1:	
		try:				
			if path_file.is_file():		
				if (marquee !='default'):					
					os.killpg(pipe.pid, signal.SIGSTOP)
					pipe= subprocess.Popen("/home/pi/rpi-rgb-led-matrix/bindings/python/samples/marquee.py {0}".format(path_rom/'default.png'), preexec_fn=os.setsid, shell=True)					
					marquee= 'default'
					file = open(path_file,'w')
					file.write('exit \n')
					file.write('default.png')
					file.close()
				else:				
					file = open(path_file,'r')
					rom = re.sub(' |[()]|USA', '', file.readline().rstrip('\n'))
					system = file.readline().rstrip('\n')
					file.close()
					if rom.strip() and system.strip() :				
						if (rom != 'shutdown') :
							if (rom != 'reboot') :							
								if( system != default) :										
									if (rom != display) :	
										os.killpg(pipe.pid, signal.SIGSTOP)
										pipe= subprocess.Popen("/home/pi/rpi-rgb-led-matrix/bindings/python/samples/marquee.py {0}".format(Found(system,'systems')), preexec_fn=os.setsid, shell=True)
										time.sleep(7)
										display = rom															
										os.killpg(pipe.pid, signal.SIGSTOP)
										pipe= subprocess.Popen("/home/pi/rpi-rgb-led-matrix/bindings/python/samples/marquee.py {0}".format(Found(rom,'roms')), preexec_fn=os.setsid, shell=True)
								else:
									if (display != default) :
										os.killpg(pipe.pid, signal.SIGSTOP)
										pipe= subprocess.Popen("/home/pi/rpi-rgb-led-matrix/bindings/python/samples/marquee.py {0}".format(path_rom/'default.png'), preexec_fn=os.setsid, shell=True)					
										display = default					
							else:
								os.system("sudo reboot -h now")
						else:
							os.system("sudo shutdown -h now")	
					
					time.sleep(1)
			else:
				if (marquee != 'reboot') :
					os.killpg(pipe.pid, signal.SIGSTOP)
					pipe= subprocess.Popen("/home/pi/rpi-rgb-led-matrix/bindings/python/samples/runtext.py", preexec_fn=os.setsid, shell=True)
					marquee='reboot'
				time.sleep(2)
				os.system("sudo mount -a")		
		except OSError:				
				if (marquee != 'reboot'):
                    			os.killpg(pipe.pid, signal.SIGSTOP)
                    			pipe= subprocess.Popen("/home/pi/rpi-rgb-led-matrix/bindings/python/samples/runtext.py", preexec_fn=os.setsid, shell=True)
                    			marquee='reboot'
				time.sleep(2)
				os.system("sudo mount -a")
			

except KeyboardInterrupt:
	os.killpg(pipe.pid, signal.SIGSTOP)
	sys.exit(0)