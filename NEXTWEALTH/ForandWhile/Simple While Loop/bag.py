########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

#initialize variables
redBags, whiteBags = 100, 200
totalSales , totalBagsSold = 0,0

costofRedbag , costofWhitebag= 1000 , 1500
while (totalSales < 10000 or totalBagsSold < 10) :
    #Ask customer for input
    bagclr = input("What colour bag do you want Red or White ? : " ).lower()
    if bagclr not in ["red","white"]:
        print("Enter correct bag colorr ! ")
        continue
    quantity = int(input(f"How many {bagclr} bags do you want ? : "))
    
    #calculate total cost for the bags
    if bagclr == "red":
        cost = costofRedbag * quantity
    else:
        cost = costofWhitebag * quantity
        
    totalSales += cost
    #increment no of bags sold
    totalBagsSold +=  quantity

    redBags -= quantity
    whiteBags -= quantity

    print("Your bill is : " , cost)

print("Total sales : ",totalSales)  
print("Bags Sold : " , totalBagsSold)