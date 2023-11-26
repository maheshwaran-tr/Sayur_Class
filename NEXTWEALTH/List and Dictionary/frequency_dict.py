########## Program 1
#find the list unique words in a sentence
#hint - Each word is a key, count is the value

sentence = "This is a cat and it has a tail and two eyes"

countOfWords = {}
sentence = sentence.split()
for word in sentence:
    countOfWords[word] = countOfWords.get(word,0) + 1
   
print (countOfWords)