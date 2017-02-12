#!/usr/bin/env python

from pyo import *

# pm_list_devices()
# print(pm_get_default_input)

s = Server()
s.setMidiInputDevice(3)
s.boot()
s.start()

ctl = []

for i in range(7):
    ctl.append(Midictl(ctlnumber=i+1))

notes = Notein(poly=10, scale=1, mul=.5)
p = Port(notes['velocity'], .001, .5)


# a = Sine(freq=notes['pitch'], mul=p)
lf = Sine([.11,5.99], mul=15, add=20)
a = Rossler(pitch=.003, stereo=True, mul=.2, add=.2)
b = Rossler(pitch=[.5,.48], mul=a).out()

# def ctl_scan(ctlnum, midichnl):
#     print ctlnum, midichnl
# a = CtlScan2(ctl_scan)

raw_input("Press Enter to finish...")
s.stop()
