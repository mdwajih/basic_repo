class employee:
    def __init__(self, first, last, pay, location, fullname):
        self.first = first
        self.last = last
        self.pay = pay
        self.location = location
        self.fullname = first + " " + last
    

emp1 = employee( "Wajih" ,"ullah" , "1,00,000", "Hyderabad", "Something" )
emp2 = employee("Muneef", "Khan", "50,000", "Mehdipatnam", "Something")

print(emp1.fullname)
print(emp2.fullname)
