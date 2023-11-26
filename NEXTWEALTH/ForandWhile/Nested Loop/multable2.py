######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.

'''     1  2  3  4  5
  ********************
1 |  1  2  3  4  5
2 |  2  4  6  8 10
3 |  3  6  9 12 15
4 |  4  8 12 16 20
5 |  5 10 15 20 25 

'''

start = int(input("Enter starting value : "))    # getting start and end values
end = int(input("Enter ending value : "))


# for first line of table
for i in range(start , end+1):          
        print("\t",i,end="")
        

# for print *******
print("\n   ","**********"*(end-start))

# for printing rest of the tabel
for i in range(start,end+1):
    print(f"{i}  |  ",end = "\t")
    for j in range(start,end+1):
           print(f"{i*j}",end="\t")
    print("\n")