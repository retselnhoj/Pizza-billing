# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# letSmallPizza = 15
# letMediumPizza = 20
# letLargePizza = 25
# letPepperoniforSmall = 2
# letPepperoniforMedium = 3
# letPepperoniforLarge = 3
# letCheese = 1
# if size == 'S' or size == 's':
#     if add_pepperoni == 'Y' or add_pepperoni =='y':
#         if extra_cheese == 'Y' or extra_cheese == 'y':
#             print(f"Your final bill is: ${letSmallPizza + letPepperoniforSmall + letCheese}.")
#     if add_pepperoni == 'Y' or add_pepperoni =='y':
#         if extra_cheese == 'N' or extra_cheese =='n':
#             print(f"Your final bill is: ${letSmallPizza + letPepperoniforSmall}.")
#     if add_pepperoni == 'N' or add_pepperoni == 'n':
#         if extra_cheese == 'Y' or extra_cheese == 'y':
#             print(f"Your final bill is: ${letSmallPizza + letCheese}.")
#     if add_pepperoni == 'N' or add_pepperoni == 'n':
#         if extra_cheese == 'N' or extra_cheese =='n':
#             print(f"Your final bill is: ${letSmallPizza}.")
# elif size == 'M' or size =='m':
#     if add_pepperoni == 'Y':
#         if extra_cheese == 'Y' or extra_cheese == 'y':
#             print(f"Your final bill is: ${letMediumPizza + letPepperoniforMedium + letCheese}.")
#     if add_pepperoni == 'Y' or add_pepperoni =='y':
#         if extra_cheese == 'N' or extra_cheese =='n':
#             print(f"Your final bill is: ${letMediumPizza + letPepperoniforMedium}.")
#     if add_pepperoni == 'N' or add_pepperoni == 'n':
#         if extra_cheese == 'Y' or extra_cheese == 'y':
#             print(f"Your final bill is: ${letMediumPizza + letCheese}.")
#     if add_pepperoni == 'N' or add_pepperoni == 'n':
#         if extra_cheese == 'N' or extra_cheese =='n':
#             print(f"Your final bill is: ${letMediumPizza}.")
# elif size == 'L' or size == 'l':
#     if add_pepperoni == 'Y' or add_pepperoni == 'y':
#         if extra_cheese == 'Y' or extra_cheese == 'y':
#             print(f"Your final bill is: ${letLargePizza + letPepperoniforLarge + letCheese}.")
#     if add_pepperoni == 'Y' or add_pepperoni == 'y':
#         if extra_cheese == 'N' or extra_cheese =='n':
#             print(f"Your final bill is: ${letLargePizza + letPepperoniforLarge}.")
#     if add_pepperoni == 'N' or add_pepperoni == 'n':
#         if extra_cheese == 'Y' or extra_cheese == 'y':
#             print(f"Your final bill is: ${letLargePizza + letCheese}.")
#     if add_pepperoni == 'N' or add_pepperoni == 'n':
#         if extra_cheese == 'N' or extra_cheese =='n':
#             print(f"Your final bill is: ${letLargePizza}.")
            
            
bill = 0

if size == 'S' or size == 's':
    bill += 15
elif size == 'M' or size == 'm':
    bill += 20
else:
    bill += 25
    
if add_pepperoni == 'Y' or size == 'y':
    if size == 'S' or size == 's':
        bill += 2
    else:
        bill += 3
        
if extra_cheese == 'Y' or extra_cheese =='y':
    bill += 1
    
print(f"Your final bill pay is $ {bill}")