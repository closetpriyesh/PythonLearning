list = [-6, -5, -4, 1, 2, 3]

slist = sorted(list, key=abs)

print(slist)


from operator import attrgetter

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Ram', 23, '4500')
e2 = Employee('Shyam', 13, '3500')
e3 = Employee('Raj', 25, '4600')

e = [e1, e2, e3]

def e_sort(emp):
    return emp.name

s_employees = sorted(e, key=e_sort)

print(s_employees)