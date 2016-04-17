# coding: utf-8
# knock16.py
import sys
import itertools
from itertools import zip_longest
import math

def split_lines(lines):
	lines_per_file = math.ceil(len(lines) / int(sys.argv[2]))
	i = 0
	for line_list in itertools.zip_longest(*[iter(lines)]*lines_per_file):
		file_name = "split" + str(i) + ".txt"
		with open(file_name, 'a') as export_file:
			for line in line_list:
				if line is not None:
					export_file.write(line) 
		i += 1

if __name__ == '__main__':
	
	with open(sys.argv[1]) as input_file:
		lines = input_file.readlines()

	split_lines(lines)
