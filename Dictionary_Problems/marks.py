######## Problem   ###############
# Get and print the 2 marks for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc


noOfStudents = 3
noOfSubjects = 2

stduentDetails = {}

for stduent in range(noOfStudents):
    name = input("Enter Student Name : ")
    mark1 = int(input("Enter mark1 : "))
    mark2 = int(input("Enter mark2 : "))
    stduentDetails[name]  = [mark1,mark2]    # appending details to the Dictionary

# printing details in format 1
for no,student in enumerate(stduentDetails):
    for j in range(noOfSubjects):
        print(f"Mark {j+1} for Student{no+1} is {stduentDetails[student][j]}")

print("\n")

# printing details in format 2
for name,mark in stduentDetails.items():
    print(f"Marks for {name} is {mark}")