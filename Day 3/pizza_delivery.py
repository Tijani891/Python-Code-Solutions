print("welcome to the Pizza Deliveries App ")

print("""Here are the price list below.
      1. Small pizza for $15 
      2. Medium Pizza for $20
      3. Large Pizza for $25
      ---------------------------
      Extra Additions
      -----------------------------
      Pepperoni for small pizza +$2
      Pepperoni for medium and large pizza +$3
      Extra chesse for all pizza size +$1
     -----------------------------------------

      """)


size = input("Enter the pizza size you want? S, M, L : ")
add_pepperoni = input("Do you want to add pepperoni? Y, N : ")
extra_chesse = input("Do you want to add chesse? Y, N : ")


small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_for_small = 2
pepperoni_for_medium_and_large = 3
extra_cheese_amount = 1


if size == "S":
    if size == "S" and add_pepperoni == "Y":
        total_bill = small_pizza + pepperoni_for_small
        print(f"Your total bill ${total_bill}")
    elif size == "S" and  extra_chesse == "Y":
        total_bill = small_pizza + extra_cheese_amount
        print(f"Your total bill ${total_bill}")
    else:
        print(f"Your total bill is ${small_pizza}")

elif size == "M":
    if size == "M" and add_pepperoni == "Y":
        total_bill = medium_pizza + pepperoni_for_medium_and_large
        print(f"Your total bill ${total_bill}")
    elif size == "S" and  extra_chesse == "Y":
        total_bill = medium_pizza + extra_cheese_amount
        print(f"Your total bill ${total_bill}")
    else:
        print(f"Your total bill is ${medium_pizza}")

elif size == "L":
    if size == "L" and add_pepperoni == "Y":
        total_bill = large_pizza + pepperoni_for_medium_and_large
        print(f"Your total bill ${total_bill}")
    elif size == "S" and  extra_chesse == "Y":
        total_bill = large_pizza + extra_cheese_amount
        print(f"Your total bill ${total_bill}")
    else:
        print(f"Your total bill is ${large_pizza}")

else:
    print("Enter the right response (S for Small pizza size ,M for Medium pizza size ,L for Large pizza size)")





