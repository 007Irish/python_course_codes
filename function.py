# a = 4
# b = 2
# c = 1

# average = (a+b+c)/3
# print(average)

# a1 = 6
# b1 = 7
# c1 = 8

# average1 = (a1+b1+c1)/3
# print(average1)


# def average(a,b,c):  #This is function definition.
#     d=(a+b+c)/3
#     print(d)

# average(9,9,9)   #This is function calling
# average(7,8,9)

def average(a,b,c):
    d=(a+b+c)/3
    return d

o1 = average(9,9,9)
o2 = average(7,8,9)

print(o1)
print(o2)

def percentage(a,b,c,d):
    e = ((a+b+c+d)/400)*100
    
    return e

i = percentage(23,56,78,99)
print(i)