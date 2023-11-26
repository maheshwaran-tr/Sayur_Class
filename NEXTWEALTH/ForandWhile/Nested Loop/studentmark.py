######## Problem   ###############
# Get and print the 2 marks for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc

def using_Dict():
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



def using_List():
    noOfStudents = 3
    noOfSubjects = 2
    namelist = []    #list for name and mark
    marklist = []
    for student in range(noOfStudents):        

        name= input("Enter the student name : ")
        namelist.append(name)     # appending name to the namelist

        for mark in range(noOfSubjects):
            marklist.append(int(input("Enter mark :")))     # appending marks to the mark list

    # printing details in format 1
    i=0
    for names in range(noOfStudents):
        for marks in range(noOfSubjects):
            print(f"Mark {marks+1} for Student {names+1} is {marklist[i]}")
            i+=1

    # printing details in format 2
    i=0
    for names in namelist:
            
            print(f"Marks for {names} is ",marklist[i],marklist[i+1])   
            i+=2
    print("\n")

   


using_List()