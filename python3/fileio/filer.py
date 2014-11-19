"""filer.py
File opener module by Kenny
better file functions using try/catch/except
"""

#returns a file object instance
def opener(filename):
	try:
		fs = open(filename, 'w')
		print("File %s is open for writing" % filename)
	except IOError:
		print("File did not exist, creating file now")
		os.touch(filename)

	#print("Returning file object")
	return fs

def print_file(filename):
	print("Reading file...")
	fs = open(filename, 'r')
	lines = fs.readlines()
	for line in lines:
		print(line, end='')
	return True
