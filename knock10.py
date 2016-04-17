# coding: utf-8
# knock10.py
import sys

if __name__ == '__main__':
	
	with open(sys.argv[1]) as input_file:
		lines = input_file.readlines()

	print(len(lines))
