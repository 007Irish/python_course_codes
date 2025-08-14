# Dunder means double underscore. Eg:- __init__, __str__ etc.
class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    
    def __repr__(self):
        return f"name : {self.name}\nsalary : {self.salary}"
    
    def __len__(self):
        return len(self.name)
        
e = Employee("Harry", 45000)
print(e.name, e.salary)
print(len(e))
print(str(e))
print(repr(e))