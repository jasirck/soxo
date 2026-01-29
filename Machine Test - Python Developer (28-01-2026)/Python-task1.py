employees = [
    (101,"Alice","HR",50000),
    (102,"Bob","IT",70000),
    (103,"Charlie","IT",90000),
    (104,"David","HR",60000),
    (105,"Eve","Finance",75000),
    (106,"Frank","Finance",72000)
]
# Task 1 : FInd Highest Salary Employee

Highest_Salary_Employees = {}
for emp in employees:
    if emp[2] not in Highest_Salary_Employees:
        Highest_Salary_Employees[emp[2]] = emp
    else:
        if emp[3] > Highest_Salary_Employees[emp[2]][3]:
            Highest_Salary_Employees[emp[2]] = emp
print('Highest Salary Employees in each Department:')
for emp in Highest_Salary_Employees.values():
    print(f"Department: {emp[2]}| Employee ID: {emp[0]}| Name: {emp[1]}| Salary: {emp[3]}")
