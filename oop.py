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

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
print(employee.__dict__)
