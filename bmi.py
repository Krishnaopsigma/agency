Weight=float(input("Enter your Weight in Kg: "))

Height = float(input("Enter your height in centimeters: "))
Height=Height/100

BMI=Weight/(Height*Height)
print("BMI:",BMI)
if BMI<=16:
    print("Severely underweight")
elif BMI<=18.5:
    print("Underweight")
elif BMI<=25:
    print("You are normal")
elif BMI<=30:
    print("You are obessed")
else:
    print("You are severely overweight")