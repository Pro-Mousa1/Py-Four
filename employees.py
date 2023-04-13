from database import Employee

employees = Employee.select()

for employee in employees:
    print(employee.name, employee.badge_no, employee.work_field, employee.id)


Employee.delete().where(Employee.id == 3).execute()
