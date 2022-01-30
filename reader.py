#This piece of code analyses all of the 5 letter words and saves them to a single file.
#Dictionary.com had some 5 letter words that weren't recognised by wordle, I removed the "top" words that did not exist according to wordle from the final list manually.
import glob
import re

#This is the set object for 5 letter words, I put 2 words in to make sure python recognised it as a set.
#Theres probably a better way to do this, but this works and does not affect results.
words={'zaire', 'zloty'}

#This function searches each of the web page for 5 letter words.
def print_file(pathh):
	filee = open(pathh,"r",encoding="utf-8")
	content= filee.read()
	five_letter_words = re.findall(r"\"displayForm\":\"[a-zA-Z]{5}\"",content)
	for word in five_letter_words:
		words.add(word[15:20].lower())
	filee.close()

files=glob.glob("*")
for filee in files:
	print_file(filee)

filee = open("../all_words.txt","a",encoding="utf-8")
for word in words:
	filee.write(word+ "\n")
filee.close

	