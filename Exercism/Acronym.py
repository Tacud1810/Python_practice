def abbreviate(words: str):
	words = words.replace("-", " ")
	mylist = words.split()
	my_list_2 = []
	for x in mylist:
		if x[0].isalpha():
			my_list_2.append(x[0])
		if x[0].isalpha() == False and len(x)>1:
			my_list_2.append(x[1])
	return "".join(my_list_2).upper()


print(abbreviate("Complementary metal-oxide semiconductor"))