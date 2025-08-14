class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property    #This is getter
    def first_name(self):
        l = self.name.split(" ") # .split execute it in the form of a list.
        print(l)
        return l[0]
    
    @first_name.setter  #This is setter
    def  first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name


e = Employee("Jackie Chan", 95000)
# print(e.first_name())
# e.set_first_name("Jackiee")
# print(e.name)

print(e.first_name)
e.first_name = "Shin"
print(e.name)