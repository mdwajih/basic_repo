class employee:
    def __init__(self, first, last, pay, location):
        self.first = first
        self.last = last
        self.pay = pay
        self.location = location
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    

emp1 = employee( "Wajih" ,"ullah" , "1,00,000", "Hyderabad")
emp2 = employee("Muneef", "Khan", "50,000", "Mehdipatnam")

print(emp1.fullname())
print(emp2.fullname())