class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

        # Static Method
    @staticmethod
    def sum(a, b):
        return a+b
        
        # Class Method This gives the reference of the class. Here it is giving the reference of class employee.
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
            cls.company = new_company    



e1 = Employee("Golu", 1500)
# e2 = Employee("Chintu", 150000)
# print(Employee.company)
# print(Employee.name)  #This will throw an error
# e1.print_info()
# e2.print_info()

# print(e2.sum(5, 25))
print(Employee.company)
e1.change_company("acer")
print(Employee.company)
 
