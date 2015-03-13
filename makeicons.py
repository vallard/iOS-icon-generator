#!/usr/bin/env python

from subprocess import call
import sys

sizes = [29, 40, 60, 76 ]

if len(sys.argv) < 2:
  print "please enter a file name to process"
  exit()

for s in sizes:
  for p in range(1,4):
    ss = p * s
    g = "%dx%d" % (ss, ss)
    iconName = "icon@%d.png" % ss
    print "Making icon %s" % iconName
    call(["convert", sys.argv[1], "-resize", g, iconName])

#g = "180x180"
#iconName = "icon@180.png"
#print "Making icon %s" % iconName
#call(["convert", sys.argv[1], "-resize", g, iconName])
