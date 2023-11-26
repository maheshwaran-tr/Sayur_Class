#Write code for drawing these patterns.
#Get width and length from the user.
# draw a empty rectangle woth char *
#eg 
'''
Row 5, col 7
* * * * * * *
*           *
*           *
*           *
* * * * * * *
'''


row = int(input("Enter no of rows : "))
col = int(input("Enter no of cols : "))


for i in range(1,row+1):
    if i==1 or i==row:
        print("* " * col)
    else:
        print("* " + "  " * (col-2) + "* ")