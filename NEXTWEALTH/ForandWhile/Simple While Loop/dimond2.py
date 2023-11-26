######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines

import msvcrt

# function to check if the key is pressed space or not

def is_space_key_pressed():
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b' ':
                return True
            else:
                return False
            
n = int(input("Enter the number of rows: "))

for i in range(n):
    if is_space_key_pressed():
        print(" "*(n-i-1) + "$ "*(i+1)) 
    else:
        break
    
for i in reversed(range(n-1)):
    if is_space_key_pressed():
        print(" "*(n-i-1) + "$ "*(i+1)) 
    else:
        break