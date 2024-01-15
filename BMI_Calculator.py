weight=float(input("Enter Your weight(in kilogram) : "))
height=float(input("Enter Your height(in meters) : "))

def BMI(w,h):
    bmi = w/h**2
    if bmi>=25:
        print("Your BMI is ",bmi," You are Overweight")
    elif bmi>=18.5 and bmi<=24.9:
        print("Your BMI is ",bmi," You are Healthy")
    else:
        print("Your BMI is ",bmi," You are Underweight")

BMI(weight,height)