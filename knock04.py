# coding: utf-8
# knock04.py
if __name__ == '__main__':

	string      = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
	str_list    = string.split()
	single_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
	str_map     = {}
	
	i = 1;
	for word in str_list:
		if i in single_list:
			str_map[word[0:1]] = i
		else:
			str_map[word[0:2]] = i
		i += 1 

	print(str_map)
