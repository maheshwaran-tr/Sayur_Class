num = int(input("Enter the number : "))
rev=0
while num>0:
    rem = num % 10
    rev = rem + (rev * 10)
    num = num//10
print("Reversed integer : ",rev)