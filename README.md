# forline
A small utility to execute python instructions for each line of text files. Inspired by awk and the perl -n option missing in python. Based on http://code.activestate.com/recipes/437932/ with additional options for heading code (-b, which can be used for imports), trailing code (-e) and separators (-s). As in the original script, the variables line, words[] and num have the following meaning:

* line refers to the current line (without carriage return),
* words[n] refers to the nth word (starting from 0). The line is splitted with spaces or the separator given with the -s option
* num is the current line number (starting from 1)

The following example removes duplicated lines.

    $ cat exemple | forline.py -b "lines = set()" "if line not in lines: lines.add(line); print(line)"
    
The following example sums the first word matching an integer in each line. Note that the body instructions must be separated in two strings as an assgnment cannot be separated from a if with a semicolon. Refer to the definition of compound statements at  https://docs.python.org/2/reference/compound_stmts.html.

    $ cat exemple | forline.py -b "import re; s = 0" -e "print(s)" "m = re.search(r'\b(\d+)\b', line)" "if m: s += int(m.group(1))"
    
Syntax, error and behaviour

forline is compatible python 2 and 3 and uses syntax from python 3 (print and division). An additional -t option enables to trace the generated script. Using the generated script is strictly equivalent than using forline command line. As a consequence, all questions regarding syntax or execution errors may be analyzed by running the generated script.
