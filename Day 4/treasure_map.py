#     1     2     3
# 1 ["◻️","◻️" ,"◻️"]
# 2 ["◻️","◻️" ,"◻️"]
# 3 ["◻️","◻️" ,"◻️"]

# User will enter which position to save the treasure(X)
# For example postion = 23 where 2 is the vertical(column) axis location and 3 is the horizontal(row) axis location

row1 = ["◻️","◻️" ,"◻️"]
row2 = ["◻️","◻️" ,"◻️"]
row3 = ["◻️","◻️" ,"◻️"]

map = [row1, row2, row3]

user_input =  str(input("Enter your position: "))

horizontal = int(user_input[0]) - 1
vertical = int(user_input[1]) - 1

map[vertical][horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}")



