############# Problem  2 #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.

monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year
#FillinMissingCode - initialise all the variables needed

previousMonthSalary = 0

for month, phoneCount in enumerate(monthlySalesList,1):
    print(f"\n ------- MONTH {month} ---------")
    #calculate the Salary using If stmts
    if phoneCount>=5:
        currentMonthSalary = (5000 * (phoneCount//5))  + (1100 * (phoneCount - 5))
    
    currentMonthSalary = currentMonthSalary + 10000
    print (f"This month's salary before additional bonus {currentMonthSalary}") 

    if(phoneCount < 20):
        previousMonthSalary = currentMonthSalary #we set this so that, we can use this info in the next iteration
        continue #no need to calculate anything because <20 phones sold
    
    #check for condition #If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
    # this month also, then he gets additional Rs5000.
    if previousMonthSalary > 20000 and phoneCount>=20:
        currentMonthSalary += 5000
    
    print(f"This month's salary after additional bonus {currentMonthSalary}")
    previousMonthSalary = currentMonthSalary #Why are we doing this?