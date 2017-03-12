# coding: utf-8

word = "fizz"
word2 = "buzz"
for i in range(1,101):
	if (i % 3 == 0 and i % 5 == 0):
		print word + word2
	elif i % 3 == 0:
		print word
	elif i % 5 == 0:
		print word2
	else:
		print i

