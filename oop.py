class employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay, location):
        self.first = first
        self.last = last
        self.pay = pay
        self.location = location

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = employee( "Wajih" ,"ullah" , 100000, "Hyderabad")
emp2 = employee("Muneef", "Khan", 50000, "Mehdipatnam")


emp2.raise_amount = 1.08

print(employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)