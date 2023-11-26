#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user.

#find how many choc and cake the user can buy


noOfCake = 0
noOfChoc = 0
#get budget
money = int(input("Enter your budget : "))

while (money >= 150):   # minimum amount 150
    if (money >= 200):     # checking money is greater than 200 for buying choc
        noOfChoc += 1
        money -= 200

     #for buying cake
    if(money >= 150):
        noOfCake += 1
        money -= 150

#print no of cakes and choc
print(f"user can buy {noOfChoc} of Chocos ")
print(f"user can buy {noOfCake} of Cakes ")