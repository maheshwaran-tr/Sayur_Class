'''
Same details as above.
But the input is in a file in the following format
Name/Month  Sam    Adam     Sara
Month1      300     340     1000
Month2      567     456     234
Month3      234     456     3000
Month4      1000    234     2000   
Find the name of the employee who had the most the phone sales each month and add it to the end of the
table and write it back to the file
eg
Name/Month  Sam    Adam     Sara    MostSales
Month1      300     340     1000    Sara    
Month2      567     456     234     Sam    
Month3      234     456     3000    Sara
Month4      1000    234     2000    Sara
Also , print the employee who sold most phones in all 4 months added.

'''

with open("D:/GITHUB_MAHES/Sayur_Mahesh-2/NEXTWEALTH/Files/test.txt","r") as inputfile:
    lineList = inputfile.readlines()    # converting eachline into list

    header = lineList[0].split()      # taking header part
   
    data = [line.split() for line in lineList[1:]]    # taking data part
    salesList = []
    maxSales = []
    for row in data:     # traversing each row in the data part

        monthSales = [int(sale) for sale in row[1:]]   # converting string to int for each phone sales
        salesList.append(monthSales)
        monthSalesIndex  = monthSales.index(max(monthSales))   # finding the index of max sale 
        
        maxSales.append(header[monthSalesIndex + 1])  # appending the employee name based on max index
   
    header.append("MostSales")   # appending "mostsales" to the header part
    for i in range(len(data)):
        data[i].append(maxSales[i])    # appending the max sales employee to the each row of data part 
    

    # salesList = [[300,340,1000],[567,456,234],[234,456,3000],[1000,234,2000]] 
    #code to find the employee who sold most phones in all 4 months added
    totalSalesPerPerson=[]
    for i in range(len(salesList[0])):
        a = 0
        for j in range(len(salesList)):
            a = a + salesList[j][i]         # adding coloumns of the data , to find the 4 month total sales for an employee
        totalSalesPerPerson.append(a)        # totalSalesPerPerson = [2101,1486,6234]
    mostSalesEmp = header[totalSalesPerPerson.index(max(totalSalesPerPerson)) + 1]    # getting the employee of maximum values index 


# code to write updated details to file
with open("D:/GITHUB_MAHES/Sayur_Mahesh-2/NEXTWEALTH/Files/test.txt","w") as outputfile:
    outputfile.write('  '.join(header)+"\n")           # writing updated header and data part to the file
    for row in data:
        outputfile.write('    '.join(row)+"\n") 
    outputfile.write(f"{mostSalesEmp} is the employee who sold most phones")