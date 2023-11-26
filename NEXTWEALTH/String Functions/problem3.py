########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputSentence = input("Enter sentence : ")
pigLatinKey = 'ay'
for word in inputSentence.split(): #gets the word in a sentence
    #take the first char
    firstChar = word[0]
    if len(firstChar)>1:
        firstChar = word[0][0]
    #FillinMissingCode - check if the word has more than one char

    word = word[1:] + firstChar + pigLatinKey
    print(word,end=" ")