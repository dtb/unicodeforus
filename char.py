#! /usr/bin/env python
# coding=utf-8


import sys
import re

def doChar(char, charName):
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

if len(sys.argv) == 3:

	char = sys.argv[1].decode('UTF-8')
	charName = sys.argv[2].decode('UTF-8')
	doChar(char, charName)
elif len(sys.argv) == 2:
	with open(sys.argv[1]) as f:
		for line in f:
			line = line.strip()
			if len(line) == 0:
				continue

			[cp, charName] = map(lambda s: s.strip(), line.split(','))
			char = unichr(int(cp, 16))
			doChar(char, charName)
else:
	print """
Specify either a character and a character name (e.g., ./char.py ⁂ Asterism), or
a file that contains a unicode code point and a name separated by a comma, e.g.:

	2606, Empty Star
	260E, Telephone
	260F, Empty telephone

	"""
	sys.exit()


