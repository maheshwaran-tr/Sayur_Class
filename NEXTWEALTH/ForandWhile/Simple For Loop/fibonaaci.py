######## Problem 2 ###############
#Write a program that prints out the Fibonacci sequence up to a given number.
#example 1,2,3,5,8 , next number is the sum of previous two numbers.

n = int(input("Enter the limit : "))  # getting the limit from user

first , second = 0,1
next = 0
print(first,second , end = " ")      # printing first two numbers
for i in range(n-2):
    next = first + second             # adding first and second number
    print(next , end = " ")
    first = second            
    second = next