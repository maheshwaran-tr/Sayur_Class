########  Problem 3  ###############
# Write a program that prints out a diamond shape using #.
# Hint - print(5 * "$") will print  - $$$$$
# Hint - print(5* "$ ") will print  - $ $ $ $ $


n = int(input("Enter the number of rows: "))
#print the top triangle
for i in range(n):
    print(" "*(n-i-1) + "$ "*(i+1)) 


#printing bottom of triangle 
for i in reversed(range(n-1)):            
    print(" "*(n-i-1) + "$ "*(i+1)) 