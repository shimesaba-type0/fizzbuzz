# coding: utf-8

word = "fizz buzz"
for i in range(100):
	if i == 0:
		print ("This is zero")
	elif (i % 3 == 0 and i % 5 == 0):
		print word
	elif i % 3 == 0:
		print word.split(" ")[0]
	elif i % 5 == 0:
		print word.split(" ")[1]
	else:
		print i

