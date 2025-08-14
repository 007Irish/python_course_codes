def divide(a, b):
    try:
        c=a/b
        print(c)
        return c
    except Exception as e:
        print("There is an error", e)
        
    #This is always executed no matter if they completely executes or not
    finally:
        print("This will always executed")

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

divide(a, b)
