class Employee():
    def __init__(self,last,first,annualSalary):
        self.last = last
        self.first = first
        self.annualSalary = annualSalary

    def give_raise(self,incresment = 5000):
        self.annualSalary += incresment

