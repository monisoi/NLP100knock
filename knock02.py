# coding: utf-8
# knock02.py
if __name__ == '__main__':

	first_str  = "パトカー"
	second_str = "タクシー"
	ans = ""
	for first, second in zip(first_str, second_str):
			ans += first + second

	print(ans)

