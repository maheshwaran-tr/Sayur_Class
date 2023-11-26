# Fill in the missing code whereever it says #FillinMissingCode
# Fix the syntax errors as needed.

# This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
# add new functions as needed.

# The main functions is to find the total profit


def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans


def subtractAfromB(a, b):
    ans = a - b
    return ans


def multiplyTwoNumbers(n1, n2):
    mul = n1 * n2
    return mul


def divideAFromB(a, b):
    ans = a / b
    return ans


def calc(itemList):
    res = 0
    for i in itemList:
        res = addTwoNumbers(res, i)
    return res


# main code

# we have sales data for a week.
costOfCoffee, costOfTea, costOfVadai = 25, 20, 25

coffeeSales = [56, 78, 56, 45, 90, 103, 120]
teaSales = [100, 123, 456, 123, 222, 400, 346]
vadaiSales = [23, 45, 67, 12, 89, 90, 120]

# Find total sales in the week.
totalSales = calc(coffeeSales) + calc(teaSales) + calc(vadaiSales)
print("Total sales : ",totalSales)

# calculate avg sales for a week
avgSale = divideAFromB(totalSales, 7)
print("Average Sales : ",avgSale)

employeeSalary = 500  # Rs500 per day

# calculate sales per week
salesPerWeek = totalSales
print("Sales per Week : ",salesPerWeek)

# calcuate sales per month
salesPerMonth = multiplyTwoNumbers(salesPerWeek, 4)
print("Sales per Month : ",salesPerMonth)

# calculate profit.
totalCost = addTwoNumbers(
    (
        multiplyTwoNumbers(costOfCoffee, calc(coffeeSales))+
        multiplyTwoNumbers(costOfTea, calc(teaSales))
    ),
    multiplyTwoNumbers(costOfVadai, calc(vadaiSales)),
)

profit = subtractAfromB(totalCost,totalSales)
print("Profit : ",profit)