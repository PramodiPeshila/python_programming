print("Welcome to the tip calculator!")

bill = float (input("What was the total bill? $ " ))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip / 100)

final_amount = (bill + tip_amount) / people

print(f"Each Person should pay: $ {final_amount:.2f}")

