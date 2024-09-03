student_score = input("Enter your height: ").split()

highest_score = 0

for score in student_score:
    if int(score) > highest_score:
        highest_score = int(score)

print(f"The highest number is : {highest_score}")