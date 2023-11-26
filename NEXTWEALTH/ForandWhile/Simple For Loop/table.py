######## Problem 1 ###############
#write multiplication table like this
# 1 * 1 = 1
# 1 * 2 = 2
#etc. Get the number as input

multiplicationNumber = int (input("Enter the multiplication number : "))
noOfEntries = int (input("How many rows do you want to print : "))

for i in range (1,noOfEntries+1):
    print (multiplicationNumber , "*" , i , " = ", i*multiplicationNumber)