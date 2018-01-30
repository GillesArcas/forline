# forline
A small utility to execute python instructions for each line of text files. Inspired by awk and the perl -n option missing in python. Based on http://code.activestate.com/recipes/437932/ with additional options for heading code (-b, which can be used for imports), trailing code (-e) and separators (-s). As in the original script, the variables line, words[] and num have the following meaning:

* line refers to the current line (without carriage return),
* words[n] refers to the nth word (starting from 0). The line is splitted with spaces or the separator given with the -s option
* num is the current line number (starting from 1)

The following example removes duplicated lines.

    $ cat exemple | forline.py -b "lines = set()" "if line not in lines: lines.add(line); print(line)"
    
The following example sums the first word matching an integer in each line.

    $ cat exemple | forline.py -b "import re; s = 0" -e "print(s)" "m = re.search(r'\b(\d+)\b', line)" "if m: s += m.group(1)"
    
