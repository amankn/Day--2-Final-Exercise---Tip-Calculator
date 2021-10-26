#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print(12 /100)

print(150 * 0.12)

print(150 + 18)

print(150 * 1.12)

print(168 / 5)

# 10% of hundred + 100, 1 represent the number itself
print(100 * 1.10)

bill = 150

tip = (bill / 15) * 1.10

print(tip)

# Tip Calculator

print("Welcome to the tip calculator.")

bill= float(input("What was the total bill? "))

tip = int(input("What percentge tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill

bill_with_tip_1 = bill * (1 + tip /100)

print(bill_with_tip)


