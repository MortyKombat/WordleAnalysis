#This is the scores table for every letter
scores={"a":[0,[0,0,0,0,0]],"b":[0,[0,0,0,0,0]],"c":[0,[0,0,0,0,0]],"d":[0,[0,0,0,0,0]],"e":[0,[0,0,0,0,0]],"f":[0,[0,0,0,0,0]],"g":[0,[0,0,0,0,0]],"h":[0,[0,0,0,0,0]],"i":[0,[0,0,0,0,0]],"j":[0,[0,0,0,0,0]],"k":[0,[0,0,0,0,0]],"l":[0,[0,0,0,0,0]],"m":[0,[0,0,0,0,0]],"n":[0,[0,0,0,0,0]],"o":[0,[0,0,0,0,0]],"p":[0,[0,0,0,0,0]],"q":[0,[0,0,0,0,0]],"r":[0,[0,0,0,0,0]],"s":[0,[0,0,0,0,0]],"t":[0,[0,0,0,0,0]],"u":[0,[0,0,0,0,0]],"v":[0,[0,0,0,0,0]],"w":[0,[0,0,0,0,0]],"x":[0,[0,0,0,0,0]],"y":[0,[0,0,0,0,0]],"z":[0,[0,0,0,0,0]]}


def writeScores(pathh,content):
    filee = open(pathh,"a")
    filee.write(str(content))
    filee.close

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][1] < arr[j + 1][1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#reads the list of all the words
filee=open("all_words.txt","r")
text=filee.read()
words=text.split("\n")
#last line seems so be a break so I added this line
words=words[:len(words)-2]

#calculates the probability-scores for each letter
#(I never divide because I need the score relative anyways)
for word in words:
	for letter_pos in range(len(word)):
		letter=word[letter_pos]
		score=scores[letter]
		update_score=[score[0]+1,score[1]]
		update_score[1][letter_pos]=update_score[1][letter_pos]+1
		scores[letter]=update_score

writeScores("results/word_strength.txt",words)

def calulator(yellow, green):
	word_scores={}
	word_scores_array=[]
	unique_array=[]
	#calculates each word "word score".
	#For yellow words it checks the "probability-score" for each unique letter
	#For green words it checks the "probability-score" for each of the letters in the different positions
	for word in words:
		score = 0
		so_far=""
		for letter_pos in range(len(word)):
			letter=word[letter_pos]
			if(yellow):
				if(not(letter in so_far)):
					score = score+scores[letter][0]
			if(green):
				score = score+(scores[letter][1][letter_pos] * 5)
			so_far+=letter
		word_scores[word]=score

	#This adds the words to an array from the dictionary, might not be necessary
	for word in word_scores:
		word_scores_array.append([word,word_scores[word]])

	#sorts the words according to their scores
	bubbleSort(word_scores_array)
    
	file_name="extra_results_"
	if(yellow):
		file_name+="yellow_"
	if(green):
		file_name+="green_"
	file_name+="probability_scores.txt"
	writeScores("results/"+file_name,word_scores_array)

	#This determains the strong words according to the last system. It finds the strongest words with no corralating letters.
	used_letters=""
	for pos in range(len(word_scores_array)):
		word=word_scores_array[pos][0]
		letter_exists=False
		for letter in word:
			letter_exists=letter_exists or (letter in used_letters)
		if(not letter_exists):
			unique_array.append(word)
			used_letters+=word

	print_msg="the best words for "
	if(green):
		print_msg+="green "
		if(yellow):
			print_msg+="and "
	if(yellow):
		print_msg+="yellow "
	print_msg+="spots"
	print("=========== "+print_msg+" ===========")
	print(unique_array)


#combined
calulator(True,True)
#yellow
calulator(True,False)
#green
calulator(False,True)