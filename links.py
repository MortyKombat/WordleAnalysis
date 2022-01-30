import os
#This creates the link to dictionary.com
def create_link(letter,page):
	return "https://www.dictionary.com/list/"+letter+"/"+str(page)

#This creates a sub-process for each of the websites and saves the result to a file
def print_links(letter,pages):
	for i in range(pages+1):
		#print(create_link(letter,i))
		os.popen("curl "+create_link(letter,i)+" > "+letter+str(i)+".txt")

#This list was built manually after checking the different url options and searching for the first 404
print_links("a",49)
print_links("b",46)
print_links("c",67)
print_links("d",36)
print_links("e",27)
print_links("f",29)
print_links("g",27)
print_links("h",32)
print_links("i",25)
print_links("j",8)
print_links("k",11)
print_links("l",28)
print_links("m",43)
print_links("n",20)
print_links("o",19)
print_links("p",59)
print_links("q",4)
print_links("r",29)
print_links("s",76)
print_links("t",39)
print_links("u",13)
print_links("v",12)
print_links("w",19)
print_links("x",1)
print_links("y",3)
print_links("z",3)