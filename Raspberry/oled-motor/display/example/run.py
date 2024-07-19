#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging    
import time
import traceback
import OLED_1in3
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)

try:
    disp = OLED_1in3.OLED_1in3()

    logging.info("\r 1.3inch OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()
    # IN = disp.gpio_mode(2,disp.INPUT)
    # while True:
    #     print(disp.digital_read(IN))
    #     time.sleep(0.5)
    # Create blank image for drawing.
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    logging.info ("***draw text")
    # draw.text((20,0), 'it is matter ', font = font1, fill = 0)
    draw.text((20,24), u'┑(￣Д ￣)┍', font = font2, fill = 0)
    image1 = image1.rotate(180) 
    disp.ShowImage(disp.getbuffer(image1))
    time.sleep(3)
    
    # logging.info ("***draw image")
    # Himage2 = Image.new('1', (disp.width, disp.height), 255)  # 255: clear the frame
    # bmp = Image.open(os.path.join(picdir, 'hackton.bmp'))
    # Himage2.paste(bmp, (0,0))
    # Himage2=Himage2.rotate(180) 	
    # disp.ShowImage(disp.getbuffer(Himage2)) 
    # time.sleep(3)    
    disp.clear()

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    disp.module_exit()
    exit()
# (^•ﻌ•^)