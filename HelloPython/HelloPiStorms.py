# coding: utf-8

# for ptvsd debug.
import ptvsd        
import platform

import os
import sys
import inspect
import time

# for ptvsd debug.
ptvsd.enable_attach(secret = 'ptvsd')
os = platform.system()
print 'Waiting for attach...'
if os != 'Windows':
    ptvsd.wait_for_attach()

# common three lines need for each PiStorms programs.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# import PiStorms library.
from PiStorms import PiStorms
psm = PiStorms()

# print a message on the screen.
psm.screen.termPrintln("EV3 touch sensor readout (BBS1):")
psm.screen.termPrintln(" ")

# reset EV3 touch sensor count.
psm.BBS1.resetTouchesEV3()

# main loop
exit = False
while(not exit):
    # get touch sensor data.
    touch = psm.BBS1.isTouchedEV3()
    numTouch = psm.BBS1.numTouchesEV3()
    # print the data on PiStorms screen.
    psm.screen.termReplaceLastLine(str(touch) + " " + str(numTouch))
    # exit code.
    if (psm.screen.checkButton(0, 0, 320, 320)):
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Exiting to menu")
        exit = True