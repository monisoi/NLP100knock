# coding: utf-8
# knock12.py
import sys

def save_col(lines, file_name, col_num):
	with open(file_name, 'a') as col:
		for line in lines:
			line_list = line.split()
			col.write(line_list[col_num-1] + '\n')

if __name__ == '__main__':

	with open(sys.argv[1]) as input_file:
		lines = input_file.readlines()

	save_col(lines, "col1.txt", 1)
	save_col(lines, "col2.txt", 2)


