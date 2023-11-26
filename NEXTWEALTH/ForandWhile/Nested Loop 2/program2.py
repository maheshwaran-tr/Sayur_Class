'''
Get the list of employee names from the user.
Get the monthly phone sales for each employee for the first 4 months of the year.
Sort the employees by name in alphabetical order and for each employee sort their phones sales in 
ascending order.
Eg - Sam, Adam, Sara
Sam's sales - 300, 567,234,1000
Adam's Sales - 340, 456,456,234
Sara' Sales - 1000,234,3000,2000
Output sample
Adam - 456,456,340,234
Sam - ...
Sara - ...
'''
print("Enter -1 to end")
employeeList = []
phoneSales = []
while True:
    monthSales = []
    empName = input("Enter the employee name : ")
    if empName=="-1":
        break
    employeeList.append(empName)

    for i in range(1,5):
        sales = int(input(f"Enter the month {i} sales of {empName} : "))
        monthSales.append(sales)
    monthSales.sort(reverse=True)
    phoneSales.append(monthSales)    
    

sortedList = sorted(enumerate(employeeList) , key=lambda x:x[1])

for index,name in sortedList:
    print(f"{name}'s Sales - {phoneSales[index]}")
