# forline
A small utility to execute python instructions for each line of text files. Inspired by awk and the perl -n option missing in python. Based on http://code.activestate.com/recipes/437932/ with additional options for heading code (-b, which can be used for imports), trailing code (-e) and separators (-s). As in the original script, the variables line, words[] and num have the following meaning:

* `line` refers to the current line (without carriage return),
* `words[n]` refers to the nth word (starting from 0). The line is splitted with spaces or the separator given with the -s option
* `num` is the current line number (starting from 1)

The first example emulates `head -10`:

    $ cat exemple | forline "if num <= 10: print(line)"

A second instruction may be added to the if body:

    $ cat exemple | forline "if num <= 10: print(num); print(line)"

Printing then testing to exit the loop must be written using two strings. Python syntax does not accept a simple statement followed by a compound statement in the same line. Refer to the definition of statements at https://docs.python.org/2/reference/compound_stmts.html. This is the only difficulty to keep in mind when using forline.

    $ cat exemple | forline "print(line)" "if num == 10: break"

Emulating `tail -10` illustrates the use of heading and trailing code sections.

    $ cat exemple | forline -b "x = []" -e "for _ in x: print(_)" "x = (x + [line])[-10:]"

The next example removes duplicated lines.

    $ cat exemple | forline -b "lines = set()" "if line not in lines: lines.add(line); print(line)"
    
The next example sums the first word matching an integer in each line. 

    $ cat exemple | forline -b "import re; s = 0" -e "print(s)" "m = re.search(r'\b(\d+)\b', line)" "if m: s += int(m.group(1))"
    
##### Installation

Download the zip file, unzip and and key `pip install .` in forline directory.

##### Syntax, error and behaviour

forline is compatible with python 2 and 3 and uses syntax from python 3 (print and division). An additional -t option enables to trace the generated script. Using the generated script is strictly equivalent than using forline command line. As a consequence, all questions regarding syntax or execution errors may be answered by running the generated script.
