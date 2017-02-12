#!/usr/bin/env python

from pyo import *

dev = pm_get_input_devices()
print dev[0][1]
print "device number:", dev[1][1]

s = Server()
s.setMidiInputDevice(3)
s.boot()
s.start()

midi = Notein()
amp = MidiAdsr(midi['velocity'])
print amp
pitch = MToF(midi['pitch'])
wave = SquareTable()
osc = Osc(wave, freq=pitch, mul=amp)
verb = Freeverb(osc).out()
osc.out()
s.gui(locals())
