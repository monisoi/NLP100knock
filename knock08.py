# coding: utf-8
# knock08.py

def cipher(string):
	ret = ""
	
	for char in string:
		ret += chr(219 - ord(char)) if char.islower() else char

	return ret

if __name__ == '__main__':

	string = input()
	cipher_str = cipher(string)
	print(cipher_str)

