""" 1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit."""


cafeItems = {
    "coffee":{
        "price" : 20,
        "stock" : 100,
        "profit" : 5,
        "refill" : 100,
        "profitAdded" : 0,
        "itemsold" : 0
    },
    "tea":{
        "price" : 20,
        "stock" : 100,
        "profit" : 2,
         "refill" : 100,
        "profitAdded" : 0,
        "itemsold" : 0
    },
    "cookies":{
        "price" : 10,
        "stock" : 50,
        "profit" : 3,
         "refill" : 50,
        "profitAdded" : 0,
        "itemsold" : 0
    },
    "donuts":{
        "price" : 15,
        "stock" : 60,
        "profit" : 4,
         "refill" : 60,
        "profitAdded" : 0,
        "itemsold" : 0
    },
    "bun":{
        "price" : 5,
        "stock" : 40,
        "profit" : 7,
         "refill" : 40,
        "profitAdded" : 0,
        "itemsold" : 0
    }
}

# functions to process the input 
def processinput(inputlist):  
    bill = 0;
    numList1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numList2 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    quantity = 0
    for word in inputlist:
        if word in numList1:
            quantity = int(word)
        elif word in numList2:
            quantity = numList2.index(word)+1
        elif word in cafeItems.keys():
            cafeItems[word]["itemsold"]+=quantity     
            bill += cafeItems[word]["price"]*quantity  # to calculate bill
    print(cafeItems)
    return bill

# function to update stock
def updateStock():
    for item in cafeItems:  
        cafeItems[item]["stock"] -= cafeItems[item]["itemsold"]
        cafeItems[item]["profitAdded"] = cafeItems[item]["itemsold"] * cafeItems[item]["profit"]
        # to refill stock if it reaches 20% of stock
        if cafeItems[item]["stock"] <= cafeItems[item]["stock"] * 0.2:
            cafeItems[item]["stock"] = cafeItems[item]["refill"]

# functions to print Top 3 items     
def topItems(list1):
    list1 = list(enumerate(list1))
    list1 = sorted(list1,key = lambda x: x[1] , reverse = True)
    print(list1)
    for i in list1[0:3]:
        print(list(cafeItems)[i[0]])


customer = 1
while customer<=5:
    print("Customer no : ",customer)
    print("----MENU CARD----")
    for k in cafeItems:
        print(k,cafeItems[k]["price"])
    custIn = input("What would you like to order:").lower().split(" ") 
    bill = processinput(custIn)
    print("Thanks for ordering ,  Enjoy your food")
    print("your bill : ",bill)
    updateStock()
    customer = customer + 1
# coverting profit and solditems into list  
profitList =[]
soldList =[]
for i in cafeItems:
    element1 = cafeItems[i]["profitAdded"] 
    profitList.append(element1)
    element2 = cafeItems[i]["itemsold"]
    soldList.append(element2)

print("---TOP 3 PROFIT---")
topItems(profitList)
print("---TOP 3 SALES---")
topItems(soldList)