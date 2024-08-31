# This is a rock paper scissors game, where the computer generates random response to the user's input
import random

rock = """    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
"""


paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

computer_response = random.randint(0,2)
print("""Welcome to the Rock, Paper and Scissors game
    _______
---'   ____)
      (_____)        
      (_____)        
      (____)
---.__(___)             
      
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)  
      
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""")

print("Follow the Instructions below, Any invalid response will lead to you losing ")
user_input = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

images = [rock, paper,scissors]

if user_input == 0 and computer_response == 2:
    print(f"Your response: \n {images[user_input]} \n Computer Response: \n {images[computer_response]} \n You win 🏆")
elif user_input == 1 and computer_response == 0:
    print(f"Your response: \n {images[user_input]} \n Computer Response: \n {images[computer_response]} \n You win 🏆")
elif user_input == 2 and computer_response == 1:
    print(f"Your response: \n {images[user_input]} \n Computer Response: \n {images[computer_response]} \n You win 🏆")
elif user_input == computer_response :
    print(f"Your response: \n {images[user_input]} \n Computer Response: \n {images[computer_response]} \n a draw 😑")
elif user_input >= 3 :
    print(f" Invalid Response, You lose 🥴")
else:
    print(f"Your response: \n {images[user_input]} \n Computer Response: \n {images[computer_response]} \n You lose 🥴")

