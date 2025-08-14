# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    
a = [1, 3, 24, 16, 69, 32, 6, 29, 9, 15, 84, 4, 92]

# new = list(filter(is_greater_than_9, a))
new = list(filter(lambda x : x>9, a))
print(new)