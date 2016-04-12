# coding: utf-8
# knock06.py

def n_gram(input_str, N):
	last = len(input_str) - N + 1
	n_gram_set = set()

	for i in range(last):
		n_gram_set.add(input_str[i:i+N])
	
	return n_gram_set

if __name__ == '__main__':

	X = n_gram("paraparaparadise", 2)
	Y = n_gram("paragraph", 2)
	print(X.union(Y))
	print(X.intersection(Y))
	print(X.difference(Y))
	print("se" in X)
	print("se" in Y)	

