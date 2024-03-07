#!/usr/bin/env python
"""
$ cat filein | forline.py [-b head code] [-e tail code] [-s sep] <body code>
https://github.com/GillesArcas/forline
"""

from __future__ import print_function, division
import sys
import getopt


SCRIPT = """\
import sys
import re
%s
for num, line in enumerate(sys.stdin, 1):
    line = line.rstrip('\\r\\n')
    words = line.split(%s)
    %s
%s
"""

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'b:e:s:t')
        opts = dict(opts)
    except:
        print(__doc__)
        exit(1)

    head = opts['-b'] if '-b' in opts else 'pass'
    tail = opts['-e'] if '-e' in opts else 'pass'
    body = '\n    '.join(args)
    body = body if body.strip() else 'pass'
    sep = opts['-s'] if '-s' in opts else None

    script = SCRIPT % (head, sep, body, tail)

    if '-t' in opts:
        print(script)
    else:
        eval(compile(script, 'command', 'exec'), globals(), locals())


if __name__ == '__main__':
    main()
