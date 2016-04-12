# coding: utf-8
# knock05.py

def n_gram(input_str, N):
	last = len(input_str) - N + 1
	n_gram_list = []

	for i in range(last):
		n_gram_list.append(input_str[i:i+N])
	
	return n_gram_list

if __name__ == '__main__':

	string = "I am an NLPer"
	print(n_gram(string, 2))
	string = string.split()
	print(n_gram(string, 2))

