#We use constructors in python to initialize our objects. A constructor is a special function in a class that runs automatically when you create a new object.

class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary #Create an instance attribute of name salary and assign it with salary.
        self.name = name
        self.bond = bond

    # def get_name(self ): 
    #     return "irish"
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")

e1 = Employee(91000, "Chintu", 2)
# print(e1.get_name())
e1.get_info()            