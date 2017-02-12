#!/usr/bin/env python

from pyo import *
s = Server().boot()
wav = SquareTable()
env = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
met = Metro(.150, 12).play()
amp = TrigEnv(met, table=env, mul=.1)
pit = TrigXnoiseMidi(met, dist='loopseg', x1=20, scale=1, mrange=(24,84))
out = Osc(table=wav, freq=pit, mul=amp).out()
s.start()
raw_input("Press Enter to finish...")
s.stop()
