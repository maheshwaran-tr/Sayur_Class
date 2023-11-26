'''HW # Count the number of each chars . Use Dictionary. 
# Print the chars and its num of occurrence in the same order as it appears in the string
#we attack at dawn
#output -  w2e1a4t3c1k1d1n1
'''
# test cases
# apple -> a1p2l1e1
# banana -> b1a2n2


# function to print the dict as inping
def printDict(dict):
    for i in dict:
        print(i,end="")
        print(dict[i],end="")


dict = {}   # empty dictionary
print("Enter z to end")

while(True): 
    letter = input("enter letter : ").lower()  # get letter from user and converting to lower case
    if letter=='z':  # if the letter is z , then break the loop
        break
    else:                                       # otherwise ,
         dict[letter] = dict.get(letter,0)+1    # adding the letter as key , get the old value of the key and increament by 1

printDict(dict)