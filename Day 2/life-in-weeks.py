max_month = 90 * 12
max_weeks = 90 * 52
max_days = 90 * 365
new_age = int(input("Enter your age: "))

month_left = max_month - (new_age * 12)
weeks_left = max_weeks - (new_age * 52)
days_left = max_days - (new_age * 365)

print(f"You have {days_left} days, {weeks_left} weeks and {month_left} months left. ")