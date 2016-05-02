#!/usr/bin/python2.7 -tt

"""Usage: ReadFile.py [--reversed | -r] --input=FILE --output=FILE

  Arguments:
    FILE  required input file

  Options:
    --input=FILE  specify input file
    --output=FILE  specify output file

"""

import docopt


class Parser():

  def cat(self):

    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt.docopt(__doc__)

    #  --input and --output is a mandatory option, -r is optional
    input_filename = arguments['--input']
    output_filename = arguments['--output']
    is_reverse = arguments['-r']

    # open input and output files
    input_f = open(input_filename, 'r')
    output_f = open(output_filename, 'wb')

    if is_reverse:
        sorted_input = sorted(input_f.readlines(), reverse=True)
    else:
        sorted_input = sorted(input_f.readlines(), reverse=False)

    # Write the output file
    for x in sorted_input:
        output_f.write(x)

        input_f.close()


# Define a main() function that paints a little greeting.
def main():
     _parser_ = Parser()
     _parser_.cat()


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
