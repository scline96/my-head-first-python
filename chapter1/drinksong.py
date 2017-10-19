drink_in = input("What're you drinkin'?\n")
container_in = input("What stuffs ya drinkn' outa?\n")

drink = str(drink_in).lower()
container = str(container_in).lower()

for drink_num in range(99, 0, -1):
    print("{0} {1} of {2} on the wall.\n{0} {1} of {2}.\nTake one down.\nPass it around."
          .format(drink_num, container, drink))

    drink_num -= 1
    if drink_num == 1:
        container = container[:-1]
    elif drink_num == 0:
        print("No more {}s of {} on the wall.\n".format(container, drink))
        break
    print("{} {} of {} on the wall.\n".format(drink_num, container, drink))
