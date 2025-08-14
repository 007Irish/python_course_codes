class Employee:
    company = "Asus" #This is class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary #Create an instance attribute of name salary and assign it with salary.
        self.name = name
        self.bond = bond
        self.company = company 

    # def get_name(self ): 
    #     return "irish"
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")

e1 = Employee(91000, "Chintu", 2, "Google")
# print(e1.get_name())
# e1.get_info()   
print(e1.company) #will always print instance attribute whenever present.
print(Employee.company) #This will always print the class attributes

#Object introspection = way to find all the methods present in an object
print(dir(e1)) 