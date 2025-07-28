a = int(input("enter a number between 1 to 10"))

match (a):
    case 4:
        print("you got a phone")
    case 6:
        print("you got a pen")
    case 1:
        print("you got a headphone")
    case _:
        print("better luck next time")

