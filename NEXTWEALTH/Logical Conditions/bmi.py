############ Problem 2 ####
#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input.



def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Get input from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate and display the BMI
bmi = calculate_bmi(weight, height)
print("Your BMI is:", bmi)

if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("normal")
elif bmi>=25 and bmi<=29.9:
    print("overweight")
elif bmi>=30 and bmi<=34.9:
    print("obesity (class 1)")
elif bmi>=35 and bmi<=39.9:
    print("obesity (class 2)")
else:
    print("extreme obesity")