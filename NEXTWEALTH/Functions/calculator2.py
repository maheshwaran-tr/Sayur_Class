""" #Fill in the missing code whereever it says #FillinMissingCode
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


def divideAFromB(#FillinMissingCode):
     
    return #FillinMissingCode

#main code


 
marksInMaths = [56,78,56,45,90]
#FillinMissingCode to calculate avg for Maths

marksInScience = [90,78,67,8,98]
#FillinMissingCode to calculate avg for Maths


marksInHistory = [87,44,56,34,90]
#FillinMissingCode to calculate avg for History


#Call divide function to get the average from all three subjects
#FillinMissingCode

print("The avg mark is ", avg)
"""


def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans


def subtractAfromB(a, b):
    ans = b - a
    return ans


def multiplyTwoNumbers(n1, n2):
    ans = n1 * n2
    return ans


def divide(numerator, denominator):
    ans = numerator / denominator
    return ans


def calc(marklist):
    total = 0
    noOfSub = len(marklist)
    for mark in marklist:
        total = addTwoNumbers(total, mark)
    return divide(total, noOfSub)


# main code

noOfSubjects = 3
marksInMaths = [56, 78, 56, 45, 90]
# FillinMissingCode to calculate avg for Maths
avg_maths = calc(marksInMaths)

marksInScience = [90, 78, 67, 8, 98]
# FillinMissingCode to calculate avg for Maths

avg_science = calc(marksInScience)

marksInHistory = [87, 44, 56, 34, 90]
# FillinMissingCode to calculate avg for History

avg_history = calc(marksInHistory)

print("Average in Maths : " , avg_maths)
print("Average in Science : " , avg_science)
print("Average in History : " , avg_history)
# Call divide function to get the average from all three subjects
# FillinMissingCode
avg = divide(
    addTwoNumbers(avg_history, addTwoNumbers(avg_maths, avg_science)), noOfSubjects
)
print(f"The avg mark is ",avg)
