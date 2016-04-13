# coding: utf-8
# knock09.py
import random

def shuffle(word):
	ret = ""
	length = len(word) 

	if length <= 4:
		ret = word
	else:
		char_list = list(word[1:length-1])
		random.shuffle(char_list)
		ret = word[0] + ''.join(char_list) + word[length-1]

	return ret

if __name__ == '__main__':

	string = input()
	str_list = string.split()
	for i in range(len(str_list)):
		str_list[i] = shuffle(str_list[i])
	print(' '.join(str_list))


