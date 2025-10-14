companies = {}

while True:
    line = input()
    if line == "End":
        break
    company_name, employee_id = line.split(" -> ")

    if company_name not in companies:
        companies[company_name] = set()

    companies[company_name].add(employee_id)

for company_name, employee_ids in companies.items():
    print(company_name)
    for emp_id in employee_ids:
        print(f"-- {emp_id}")
