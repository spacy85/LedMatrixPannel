# !/usr/bin/python
import sys
import os
import time
import curses

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageSequence, GifImagePlugin


# Rows and chain length are both required parameters:
options = RGBMatrixOptions()
options.rows = 32
options.cols=192
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'
options.brightness=50

matrix = RGBMatrix(options = options)

dir = os.path.dirname( __file__ )
filename = os.path.join( dir , sys.argv[ 1 ])

image = Image.open(filename)

image.load()
pics = []
imRGBA = image.copy()
try :
	while True :
		imRGBA = image.copy()
		imRGBA.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
		w,h =imRGBA.size
		frame = matrix.SetImage(imRGBA.convert('RGB'),abs(192-w)/2,abs(32-h)/2)
		pics.append(frame)
		image.seek( len (pics))
		time.sleep(0.04)

except EOFError : pass

matrix.Clear()


