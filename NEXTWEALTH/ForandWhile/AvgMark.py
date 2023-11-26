#write code for both for and while loop
#Get marks from 5  students and calculate avg
#

noOfStudents = 5
#for loop
total = 0
for i in range(noOfStudents):
     mark = int(input(f"Enter mark {i+1} :"))
     total += mark
avg = total/noOfStudents
print("Avg is : ", avg)  


#using while loop
total = 0
noOfStudents = 5
i = 0
while (i < noOfStudents):
     mark = int(input(f"Enter mark {i+1} :"))
     total += mark
     i += 1
avg = total/noOfStudents
print ("Avg is ",avg)