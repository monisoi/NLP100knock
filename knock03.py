# coding: utf-8
# knock03.py
if __name__ == '__main__':

	string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
	string = string.replace('.', '')
	string = string.replace(',', '')
	str_list = string.split()
	str_len_list = []
	for word in str_list:
		str_len_list.append(len(word))

	print(str_len_list)


