#!/usr/bin/env python
import time
import argparse
import sys
import signal
import os
import subprocess

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

pid =  os.getpid()

parser = argparse.ArgumentParser(description="Cambia immagine sul marquee")
parser.add_argument('rom', type=str, nargs=1, help='la rom in funzione')
args=parser.parse_args()
path="{0}".format(args.rom[0])
image = Image.open(path)

options = RGBMatrixOptions()
options.rows = 32
options.cols=192
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'
options.brightness=50

matrix = RGBMatrix(options = options)
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
w,h =image.size
matrix.SetImage(image.convert('RGB'),abs(192-w)/2,abs(32-h)/2)

while True:
        time.sleep(100)