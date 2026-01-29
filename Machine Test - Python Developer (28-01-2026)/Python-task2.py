data = {
    "deparments": ["HR", "Engineering", "HR", "Sales", "Engineering", "Sales", "Engineering"],
    "employees": ["A", "B", "C", "D", "E", "F", "G"],
    "salaries": [3000, 5000, 3200, 2500, 5500, 2700, 6000],
    "experience": [2, 5, 3, 1, 6, 2, 7]
}

# Task 2: Calculate Average Salary by Department, Filter employees with more than 5 years , add new column ( junior,senior,mid)

deparments = {}
experience_employees = {'employees': [], 'experience': [],'years': []}
data["Level"] = []
for i in range(len(data["employees"])):
    if data["deparments"][i] not in deparments:
        deparments[data["deparments"][i]] = [data["salaries"][i]]
    else:
        deparments[data["deparments"][i]].append(data["salaries"][i])
    if data["experience"][i] > 5:
        experience_employees['employees'].append(data["employees"][i])
        experience_employees['experience'].append(data["experience"][i])
        experience_employees['years'].append(data["experience"][i])
        data["Level"].append("Senior")
    elif data["experience"][i] > 2:
        data["Level"].append("Mid")
    else:
        data["Level"].append("Junior")

print('Average Salary by Department:')
for dept, salaries in deparments.items():
    avg_salary = sum(salaries) / len(salaries)
    print(f"Department: {dept} | Average Salary: {avg_salary}")

print('\nEmployees with more than 5 years of experience:')
for i in range(len(experience_employees['employees'])):
    print(f"Employee: {experience_employees['employees'][i]} | Experience: {experience_employees['experience'][i]} years: {experience_employees['years'][i]} ")

print('\nEmployee Levels:')
for i in range(len(data["employees"])):
    print(f'Employee: {data["employees"][i]}| Experience: {data["experience"][i]} | Level: {data["Level"][i]}')
    