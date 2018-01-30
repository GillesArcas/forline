#!/usr/bin/env python
"""
$ forline.py [-b head code] [-e tail code] [-s sep] <body code> [filein]
$ cat filein | forline.py [-b head code] [-e tail code] [-s sep] <body code>
"""

# based on http://code.activestate.com/recipes/437932/

from __future__ import print_function
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], 'b:e:s:')
    opts = dict(opts)
except:
    print(__doc__)
    exit(1)

head = opts['-b'] if '-b' in opts else 'pass'
tail = opts['-e'] if '-e' in opts else 'pass'
body = args[0] if args and args[0].strip() else 'pass'
sep = opts['-s'] if '-s' in opts else None
filein = open(args[1]) if args[1:] else sys.stdin

SCRIPT = """\
%s
for num, line in enumerate(filein, 1):
    line = line[:-1]
    words = line.strip().split(%s)
    %s
%s
""" 
script = SCRIPT % (head, sep, body, tail)

codeobj = compile(script, 'command', 'exec')
eval(codeobj, globals(), locals())
