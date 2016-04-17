# coding: utf-8
# knock13.py
import sys

def load_col(file_name):
	with open(file_name) as col:
		return col.readlines()

if __name__ == '__main__':

	col1 = load_col("col1.txt")
	col2 = load_col("col2.txt")
	marge_list = []

	for i in range(len(col1)):
		marge_list.append(col1[i].replace('\n', '') + '\t' + col2[i].replace('\n', ''))

	with open('marge.txt', 'a') as marge:
		for row in marge_list:
			marge.write(row + '\n')