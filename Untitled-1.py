class Emp:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary


e1 = Emp(emp_id="161E90", name="Ramu", age=35, salary=59000)
e2 = Emp(emp_id="171E22", name="Tejas", age=30, salary=82100)
e3 = Emp(emp_id="171G55", name="Abhi", age=25, salary=100000)
e4 = Emp(emp_id="151K46", name="Jaya", age=32, salary=85000)


emps = [e1, e2, e3, e4]


print("press 1 to sort by age")
print("press 2 to sort by name")
print("press 3 to sort by salary")
a=int(input("enter here"))
if a == 1:
    sorted_emps = sorted(emps, key=lambda emp: emp.age)
elif a == 2:
    sorted_emps = sorted(emps, key=lambda emp: emp.name)
elif a == 3:
    sorted_emps = sorted(emps, key=lambda emp: emp.salary)
else:
    print("Invalid input")

# Print sorted employees
#  
for emp in sorted_emps:
    print("Employee ID:", emp.emp_id)
    print("Name:", emp.name)
    print("Age:", emp.age)
    print("Salary (PM):", emp.salary)
    print()