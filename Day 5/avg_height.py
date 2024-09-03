# For loops for calculating average height

student_height = input("Enter your height: ").split()
total_sum = 0
count = 0

for student in student_height:
    total_sum = total_sum + int(student)
    count = count + 1

Average_height = total_sum/count

print(f"The average height is {Average_height}")