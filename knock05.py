# coding: utf-8
# knock05.py
if __name__ == '__main__':

	string = "I am an NLPer"
	str_list = string.split()
	string = "$" + string + "$"
	str_list = ["$"] + str_list + ["$"]
	word_bi_gram = []
	char_bi_gram = []

	for i in range(len(str_list)+1):
		word_bi_gram.append(str_list[i:i+2])

	for i in range(len(string)+1):
		char_bi_gram.append(string[i:i+2])

	print(word_bi_gram[1:len(str_list)-2])
	print(char_bi_gram[1:len(string)-2])
