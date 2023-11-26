listInt = []
print("Enter 'z' to end ")
while True:
    num = input("Enter number : ")
    if num == "z":
        break
    listInt.append(int(num))
print("Before Sorting : ",listInt)
listInt.sort()
print("After Sorting : ", listInt)