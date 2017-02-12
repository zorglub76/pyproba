#!/usr/bin/env python

from pyo import *

dev = pm_get_input_devices()
print dev[0][1]
print "device number:", dev[0][1]

s = Server()
s.deactivateMidi()
s.boot()
s.start()

def midicall(status, data1, data2):
    print status, data1, data2

listen = MidiListener(midicall, dev[1][1])
listen.start()

def asdf():
    print "aaaaaa"
    sf = SfPlayer("hall.wav", speed=1, loop=True).out(1)

asdf()
raw_input("Press Enter to finish...")
s.stop()
