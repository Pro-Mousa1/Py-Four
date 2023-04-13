from database import Admin

try:
    ad_name = input("Enter admin name\n")
    ad_email = input("Enter admin email\n")
    ad_agenda = input("Enter admin agenda\n")
    ad_account = input("Enter admin account\n")
    ad_location = input("Enter admin location\n")

    Admin.create(name=ad_name,email=ad_email,agenda=ad_agenda,
                 account=ad_account,location=ad_location)
    print("Admin saved successfully")
except:
    print("Please enter your correct email")
