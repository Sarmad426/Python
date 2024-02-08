guess_value = 3
counter = 0
while counter < 3:
    input_value = int(input("Enter guess Value: "))
    if input_value == guess_value:
        print("You win: ")
        break
    elif counter == 2:
        print("You lose: ")
    else:
        print("Try again: ")
    counter += 1
