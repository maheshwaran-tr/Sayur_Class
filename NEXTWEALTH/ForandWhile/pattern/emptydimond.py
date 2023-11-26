# program to print empty dimond

n = int(input("Enter no of rows : "))

# top part
for i in range(n):
    print(" "*(n-i-1)+ "$ " + "  "*(i-1),end="")
    print("$" if not i==0 else "")

# bottom part
for i in reversed(range(n-1)):
    print(" "*(n-i-1)+ "$ " + "  "*(i-1),end="")
    print("$" if not i==0 else "")