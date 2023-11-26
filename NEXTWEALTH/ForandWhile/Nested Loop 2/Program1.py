'''
Program 1 - Write a program to print the following pattern.
Input is 5 for the following pattern.

5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
'''
def method1(n):
    row = (n*2)-1
    val = [0] * row
    for x in range (row):
        val[x] = [0] * row


    start = 0
    end = row 

    while n!=0:
        for i in range(start,end):
            for j in range(start,end):
                val[i][j] = n
        n-=1
        start+=1
        end-=1

    for i in range(row):
        for j in val[i]:
            print(j,end=" ")
        print()


def method2(n):
    li = [str(i) for i in range(n,0,-1)]   # 5 4 3 2 1
    row = (n*2)-1
    # top part
    for i in range(n):
        if i==0:
            print(f"{li[0]} "*row)
            continue
        if i==(row//2):
            print(' '.join(li) , ' '.join(li[-2::-1]))
            continue

        print(' '.join(li[:(i+1)]) , end=" ")
        print((li[i]+" ")*(row-((i+1)*2)), end="")
        print(' '.join(li[i::-1]))

    #bottom part
    for i in reversed(range(n-1)):
        if i==0:
            print(f"{li[0]} "*row)
            continue
        
        print(' '.join(li[:(i+1)]) , end=" ")
        print((li[i]+" ")*(row-((i+1)*2)), end="")
        print(' '.join(li[i::-1]))


#main method
num = int(input("Enter number : "))
method1(num)
method2(num)