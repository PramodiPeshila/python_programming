height = float(input("Enter Your Height : "))
weight = float(input("Enter Your Weight : "))

BMI = weight / (height ** 2)

print (f"BMI = {BMI} ")

if BMI < 18.5 :
    print("You Are Underweight")
elif 18.5 <= BMI < 25 : 
    print("You Are Normal Weight")
else :
    print ("You Are OverWeight") 


