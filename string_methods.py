# name = "chinTu girish" # strings are immutable. We cannot change the original string.
 
# # name[0] = "C" # you cannot do this. it give a runtime error

# a = len(name)
# print(a)
 
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())

# text = " welcome again "
# print(text.strip())  #remove all the unnecessary blank spaces
# print(text.lstrip())  #removes the unnecessary blank spaces on the left.
# print(text.rstrip()) #removes all the unnecessary blank spaces on the right

# text = " \n welcome again \n"

# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# text = "python is funny language"
# print(text.find("is")) # output: 7 index of first occerence
# print(text.replace("funny","amazing"))

# text = "Apples,Banana,Mango"
# text1 = ['Apples','Banana','Mango']
# print(text.split(","))
# print(",".join(text1))

text = " Pytho __n"
print(text.isalpha()) #is alphabet or not

print(text.isdigit())  #is digit or not

print(text.isalnum())  #is alphabet and digit or not

print(text.isspace())  #is there any space or not


