
class Employee:
    """This is an employee class"""

    num_emps = 0                # these are class variables
    raise_amt = 1.04
    comp_stock_price = 630

    def __init__(self, first, last, pay):
        self.first = first      # these are instance variables
        self.last = last
        self.pay = pay
        Employee.num_emps += 1  # to update for all instances

    def create_email(self):
        self.email = '{}.{}@gmail.com'.format(self.first, self.last)

    def apply_personal_raise(self):
        self.pay = int(self.pay * self.raise_amt)       # this uses the instance var. version of raise_amt

    @classmethod
    def update_stock_price(cls, new_price):
        cls.comp_stock_price = new_price                # class method to play with class variables

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)                    # returns the object


print(Employee.num_emps)                                # 0
emp1 = Employee('Aryan', 'Mobiny', 1000)
print(emp1.__doc__)                                     # This is an employee class
print(emp1.__dict__)                                    # {'pay': 1000, 'first': 'Aryan', 'last': 'Mobiny'}
print(Employee.num_emps)                                # 1
print(emp1.num_emps)                                    # 1

emp2 = Employee('Pegah', 'Chavoshi', 1000)
print(Employee.num_emps)                                # 2
print(emp1.num_emps)                                    # 2
print(emp2.num_emps)                                    # 2

print(Employee.raise_amt)                               # 1.04
print(emp1.raise_amt)                                   # 1.04
print(emp2.raise_amt)                                   # 1.04

Employee.raise_amt = 1.05
print(Employee.raise_amt)                               # 1.05
print(emp1.raise_amt)                                   # 1.05
print(emp2.raise_amt)                                   # 1.05

emp1.raise_amt = 1.06
print(Employee.raise_amt)                               # 1.05
print(emp1.raise_amt)                                   # 1.06
print(emp2.raise_amt)                                   # 1.05

print(Employee.comp_stock_price)                        # 630
print(emp1.comp_stock_price)                            # 630
print(emp2.comp_stock_price)                            # 630

Employee.update_stock_price(680)
print(Employee.comp_stock_price)                        # 680
print(emp1.comp_stock_price)                            # 680
print(emp2.comp_stock_price)                            # 680

emp1.update_stock_price(690)            # using an instance to update the class variable is a bad practice
print(Employee.comp_stock_price)                        # 690
print(emp1.comp_stock_price)                            # 690
print(emp2.comp_stock_price)                            # 690
# because it updates the value for class and all instances


# now if we receive the input info as a single string, we can use a class method for generating the employees at once
new_info = 'Hannah-Mobiny-3000'
emp3 = Employee.from_str(new_info)

# see https://github.com/amobiny/Practice/tree/master/Object-Oriented for more

