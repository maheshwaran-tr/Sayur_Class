############## Problem 4 ##############
#Calculate the Grade for a student, using 3 marks.
# The student has 100 marks in any one subject, Grade is A.
# if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.

#Code
mark1 = int(input("Enter the mark 1 : "))
mark2 = int(input("Enter the mark 2 : "))
mark3 = int(input("Enter the mark 3 : "))

if(mark1 == 100 or mark2 == 100 or mark3 == 100):
    print ("Grade A")
elif(mark1 >= 90 or mark2 >= 90 or mark3 >= 90):
    print ("Grade B")
elif(mark1 >= 60 or mark2 >= 60 or mark3 >= 60):
    print("Garde C")
elif(mark1 <= 50 and mark2 <= 50 and mark3 <= 50) :
    print("Grade F")
else:
    print ("Grade D")