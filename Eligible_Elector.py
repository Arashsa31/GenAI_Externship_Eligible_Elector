#Step 1: Ask the User’s Age
age = int(input("How old are you? "))

#Step 2: Decide the Eligibility
eligible = 18
if age >= eligible:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    print("Oops! You’re not eligible yet. But hey, only", eligible - age ,"more years to go!")