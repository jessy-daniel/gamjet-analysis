#!/usr/bin/env python

import sys
import json

f = open(sys.argv[1])
map = json.load(f)
f.close()

outfile = open(sys.argv[2], "w")

for run, lumis in map.items():
   for lumi in lumis:
				print(run, " ".join([str(num) for num in lumi]))
				outfile.write(run+" ".join([str(num) for num in lumi])+"\n")

outfile.close()
