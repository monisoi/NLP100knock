# coding: utf-8
# knock14.py
import sys

if __name__ == '__main__':
	with open(sys.argv[1]) as input_file:
		lines = input_file.readlines()

	for line in lines[0:int(sys.argv[2])]:
		print(line, end='')