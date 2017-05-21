#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
from bs4 import BeautifulSoup

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    myfile = open(filename,'r')
    soup = BeautifulSoup(myfile, "html.parser")
    # Extract srting containing year digits from its <h3>
    yearstr = soup.body.h3
    # The 2008 file has the year string inside a <h2> instead. Test if that's the case and \
    # get the correct value.
    if not yearstr:
        yearstr = soup.body.h2
    # Get only the year digits from the string.
    year_digits = [int(s) for s in yearstr.text.split() if s.isdigit()]
    # Find all <tr align="right"> elements. The data we want is in their <td> children.
    # There are no other elements with the align="right" attribute in this document.
    table_soup = soup.find_all(align="right")
    listing = []
    for row in table_soup:
        listing.append(row.contents[1].string + " " + row.contents[0].string)
        listing.append(row.contents[2].string + " " + row.contents[0].string)
    sortedlist = sorted(listing)
    sortedlist.insert(0, str(year_digits[0]))
    return sortedlist


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

        # +++your code here+++
        # For each filename, get the names, then either print the text output
        # or write it to a summary file

    listsofnames = []
    for filename in args:
        listsofnames.append(extract_names(filename))

    if summary:
        with open('summary_file.txt', 'w') as f:
            for row in listsofnames:
                f.write(", ".join(row))
    else:
        for row in listsofnames:
            print(row)




if __name__ == '__main__':
    main()
