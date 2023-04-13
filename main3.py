from database import Employee

try:
    e_name = input("Enter employee name\n")
    e_badge_no = input("Enter employee badge number\n")
    e_work_field = input("Enter employee work field\n")

    Employee.create(name=e_name,badge_no=e_badge_no, work_field=e_work_field)
    print("Employee saved successfully")
except:
    print("Error, Please try again ")
    