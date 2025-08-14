s = {45, 32, 67, 2, 89}

print(s)

s.add(23)
s.add(344)
s.remove(2)
s.remove(89) #if the element is not present in the set it will throw an error.
s.discard(5656) #it will remove the element if it is present in the set. If not present it will not throw any error.
print(s)
