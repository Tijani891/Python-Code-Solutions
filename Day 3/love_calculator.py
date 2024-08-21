print("Welcome to the Love calculator Program")

name1 = str(input("Enter your name : "))
name2 = str(input("Enter your name : "))

name1_lower = name1.lower()
name2_lower = name2.lower()

True_counter = str(name1_lower.count("t") + name1_lower.count("r") + name1_lower.count("u") + name1_lower.count("e") )
Love_counter = str(name2_lower.count("l") + name2_lower.count("o") + name2_lower.count("v") + name2_lower.count("e") )

love_score = int(True_counter + Love_counter)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}%, you go together like coke and mentos")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}%, you are alright together")
else:
    print(f"Your score is {love_score}%")

