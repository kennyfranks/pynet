#!/usr/bin/python3

import filer

"""Reading and writing from files
using standard python features
"""
fs = filer.opener('testfile.txt')
fs.write('This is the first line\n')
fs.write('This is the second line\n')
fs.write('This is the third line\n')
fs.close()

filer.print_file('testfile.txt')

try:
	fs.close()
	print("File is now closed")
except IOError:
	print("File could not be closed")

