#!/usr/bin/env python
"""
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
body = '\n    '.join(args)
body = body if body.strip() else 'pass'
sep = opts['-s'] if '-s' in opts else None

SCRIPT = """\
%s
for num, line in enumerate(sys.stdin, 1):
    line = line[:-1]
    words = line.strip().split(%s)
    %s
%s
""" 
script = SCRIPT % (head, sep, body, tail)

eval(compile(script, 'command', 'exec'), globals(), locals())
