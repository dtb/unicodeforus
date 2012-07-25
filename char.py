#! /usr/bin/env python

import sys
import re

if len(sys.argv) != 3:
	print("You gotta specify a character to print and its name!")
	sys.exit()

char = sys.argv[1].decode('UTF-8')
charName = sys.argv[2].decode('UTF-8')

string = u"""
---
layout: default
character: {0}
name: {1}
code: {2:X}
---
""".format(char, charName, ord(char))

fname = "./characters/" + re.sub('[^\w0-9]+', '-', charName.lower()) + ".html"

f = open(fname, 'w')
f.write(string.strip().encode('utf-8'))
f.close()
