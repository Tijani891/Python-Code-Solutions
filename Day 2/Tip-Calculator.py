original_bill = float(input("Enter the total bill: "))
tip = int(input("What Percentage tip are you giving 10,12,15: "))
total_people = int(input("ENter total number of people to split bill: "))

new_bill = original_bill + ((tip*original_bill)/100)

bill_per_person = round((new_bill/total_people), 2)

print(f"Each person should pay ${bill_per_person}")
