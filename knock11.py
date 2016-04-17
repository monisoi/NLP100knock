# coding: utf-8
# knock11.py
import sys

if __name__ == '__main__':
	
	with open(sys.argv[1]) as input_file:
		input_file = input_file.read()

	print(input_file.replace('\t', ' '), end = '')