############## Problem  1 #################### 
#Ask first friend the colors they like. Save it in a list
#Ask another friend the same question. If the color is in the first friend's list, 
#Print "You both like "name of the color"
#If it is not in the first friend's list, Save it another list.

#init variables
colors = input("What colors you like ? :")
#convert colors into a List
colors = colors.lower()
colorList = colors.split()

commonColors = []
commonColorsCount = 0
while (True) :
    #ask the second friend for one color at a time
    color = input (" What colors you like ? : " ).lower()
    #Check if this color is in the color list
    #if present, 
    if color in colorList:
        print(f"You both like {color} color")
        commonColors.append(color)
        commonColorsCount += 1
    else:
        print("Try again ! ")

    #check if we reached the max
    if(commonColorsCount >= 3):
        break;

print ("Common colors that you both like : ",commonColors) #FillinMissingCode - list all the common movies