def add(a, b, plus=0): #perameters  #plus=0 is default argument # normally they are positional arguments.
    x = a + b +  plus
    return x


c = add(3, 5, 6) #arguments 
print(c)

c1 = add(b=5, a=3) #keywords arguments 


