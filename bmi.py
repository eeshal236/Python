h = int(input("Enter your height in cm!"))
w= float(input("Enter your weight in kg!"))

bmi=w/(h/100)**2
if bmi<18.5:
    print("You are underweight!")
elif bmi>=18.5 and bmi<=24.9:
    print("You are normal!")
elif bmi>=25 and bmi<=29.9:
    print("you are overweight!")
elif bmi>=30 and bmi<=39.9:
    print("You are obese!")
else:
    print("You are severly obese!")