'''#Fill in the missing code whereever it says #FillinMissingCode
#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#The main function adds all student marks and finds the average

def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans

def subtractAfromB(a, b):
    #FillinMissingCode
    return #FillinMissingCode

def multiplyTwoNumbers(n1,n2):
    #FillinMissingCode
    return #FillinMissingCode
def divideAFromB(a, b):
    ans = b / a
    return #FillinMissingCode

#main code

#Get 5 marks from student and find the total
total = 0
for i in 5:
    mark = (int) input("Enter mark ", i) #correct te syntax as needed
    #FillinMissingCode


#Call divide function to get the average
#FillinMissingCode

print("The avg mark is ", avg)
'''

def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans

def subtractAfromB(a, b):
    ans = b - a
    return ans

def multiplyTwoNumbers(n1,n2):
    ans = n1 * n2
    return ans

def divide(numerator , denominator):
    ans = numerator / denominator
    return ans

#main code
#Get 5 marks from student and find the total
total = 0
noOfSubjects = 5
for i in range(noOfSubjects):
    mark = int(input(f"Enter mark {i+1} :")) #correct the syntax as needed
    total = addTwoNumbers(total , mark)


#Call divide function to get the average
avg = divide(total , noOfSubjects)
print("The avg mark is ", avg)