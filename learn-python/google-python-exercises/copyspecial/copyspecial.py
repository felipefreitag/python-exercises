#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise


Copy Special Python Exercise

The Copy Special exercise goes with the file-system and external commands material in the Python Utilities section. This
 exercise is in the "copyspecial" directory within google-python-exercises (download google-python-exercises.zip if you 
 have not already, see Set Up for details). Add your code in copyspecial.py.

The copyspecial.py program takes one or more directories as its arguments. We'll say that a "special" file is one where 
the name contains the pattern __w__ somewhere, where the w is one or more word chars. The provided main() includes code 
to parse the command line arguments, but the rest is up to you. Write functions to implement the features below and 
modify main() to call your functions.

Suggested functions for your solution(details below):

    get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
    copy_to(paths, dir) given a list of paths, copies those files into the given directory
    zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile 

Part A (manipulating file paths)

Gather a list of the absolute paths of the special files in all the directories. In the simplest case, just print that 
list (here the "." after the command is a single argument indicating the current directory). Print one absolute path per line.

$ ./copyspecial.py .
/Users/nparlante/pycourse/day2/xyz__hello__.txt
/Users/nparlante/pycourse/day2/zz__something__.jpg

We'll assume that names are not repeated across the directories (optional: check that assumption and error out if it's 
violated).
Part B (file copying)

If the "--todir dir" option is present at the start of the command line, do not print anything and instead copy the files 
to the given directory, creating it if necessary. Use the python module "shutil" for file copying.

$ ./copyspecial.py --todir /tmp/fooby .
$ ls /tmp/fooby
xyz__hello__.txt        zz__something__.jpg

Part C (calling an external program)

If the "--tozip zipfile" option is present at the start of the command line, run this command: "zip -j zipfile <list all
 the files>". This will create a zipfile containing the files. Just for fun/reassurance, also print the command line you
  are going to do first (as shown in lecture). (Windows note: windows does not come with a program to produce standard 
  .zip archives by default, but you can get download the free and open zip program from www.info-zip.org.)

$ ./copyspecial.py --tozip tmp.zip .

Command I'm going to do:zip -j tmp.zip /Users/nparlante/pycourse/day2/xyz__hello__.txt
/Users/nparlante/pycourse/day2/zz__something__.jpg

If the child process exits with an error code, exit with an error code and print the command's output. Test this by 
trying to write a zip file to a directory that does not exist.

$ ./copyspecial.py --tozip /no/way.zip .

Command I'm going to do:zip -j /no/way.zip /Users/nparlante/pycourse/day2/xyz__hello__.txt
/Users/nparlante/pycourse/day2/zz__something__.jpg

zip I/O error: No such file or directory

zip error: Could not create output file (/no/way.zip)


"""


# +++your code here+++
# Write functions and modify main() to call them
# Get a list of paths from a single dir
def get_path(dir):
    filenames = os.listdir(dir)
    special_path_list = []
    for filename in filenames:
        # matches a filename that has 0 or more characters, then __, then 1 or more\
        # characters, then __, then . and any characters as an extension.
        match = re.search(r'\w*__\w+__\w*\.\w+',filename)
        if match:
            rel_path = os.path.join(dir, match.group())
            abs_path = (os.path.abspath(rel_path))
            special_path_list.append(abs_path)
    # print(special_path_list)
    return special_path_list

# From a list of directories, returns a list of paths from all dirs
def get_special_paths(dir_list):
    path_list = []
    for dir in dir_list:
        l = get_path(dir)
        for path in l:
            path_list.append(path)
    print(path_list)
    return path_list

def copy_to(paths, dir):
    print(paths)
    print(dir)
    if not os.path.exists(dir):
        os.mkdir(dir)
        # print("creating dir")
    for file_path in paths:
        shutil.copy(file_path, dir)
        #print("copying %s to %s" %(file_path, dir))
    return None

def zip_to(paths, zip_file):
    cmd = ['zip', '-j', zip_file]
    for path in paths:
        cmd.append(path)
    print("Command I'm going to do: ", " ".join(cmd))  # good to debug cmd before actually running it
    output = subprocess.run(cmd)
    #print("Ran the command")
    if output.returncode:
        print("Error code: ", output.returncode)
    #if status:  # Error case, print the command's output to stderr and exit
    #    sys.stderr.write(output)
    #    sys.exit(1)
    #print(output)  # Otherwise do something with the command's output
    return None

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    path_list = get_special_paths(args)

    if todir:
        copy_to(path_list, todir)
    elif tozip:
        zip_to(path_list, tozip)
    else:
        for path in path_list:
            print(path)

        # +++your code here+++
        # Call your functions


if __name__ == "__main__":
    main()
