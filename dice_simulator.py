import random
while True:
    print("1.Roll the dice, 2.exit")
    user_input=int(input("Enter the choice"))
    if user_input==1:
        print(random.randint(1,6))
    else:
        break