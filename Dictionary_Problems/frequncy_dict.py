'''HW # Count the number of each chars in a inping. Use Dictionary. 
# Print the chars and its num of occurrence in the same order as it appears in the inping
#we attack at dawn
#output -  w2e1a4t3c1k1d1n1
'''

# function to print the dict as inping
def printDict(dict):
    for i in dict:
        print(i,end="")
        print(dict[i],end="")


inp = "We Attack at Dawn"    # input
inp = inp.lower()            # converting to lower case
inp = inp.replace(" ","")    # removing whitspace

dict = {}   # empty dictionary

# traverse each letter in dict
for letter in inp:    

    # adding the letter as key , get the old value of the key and increament by 1
    dict[letter] = dict.get(letter,0)+1

#{'w': 2, 'e': 1, 'a': 4, 't': 3, 'c': 1, 'k': 1, 'd': 1, 'n': 1}
printDict(dict)