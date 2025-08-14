# while True:

#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The sum is {a / b}")

#     except Exception as e:
#         print("Error!", e)

#     except ValueError:
#         print("Please dont perform bad typecasts")

#     except ZeroDivisionError:
#         print("Hey dont divide by 0")

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b==0:
    raise ValueError("Please don't divide by 0") #To make our own error

print(f"The division is {a / b}")