n = int(input("Enter number : "))

# count = 1
# prime = 2

# while count<=n:
#     res = True
#     for i in range(2,(prime//2)+1):
#         if prime%i==0:
#             res = False
#             break
#     if res:
#         print(prime , end=" ")
#         count+=1
#     prime+=1

count=2
while count<=n:
    res = True
    for i in range(2,(count//2)+1):
        if count%i==0:
            res = False
            break
    if res:
        print(count , end=" ")
    count = count+1