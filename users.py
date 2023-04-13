from database import User
users = User.select()

for user in users:
    print(user.name, user.email, user.password, user.id)


# Deleting a record from a Sqlite DB
User.delete().where(User.id == 2).execute()
