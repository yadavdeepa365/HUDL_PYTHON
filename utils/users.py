

# we can store test data in this module like users
users = [
    {"name": "invalid_user", "email": "invalidUser@test.com", "password": "qwert1235"},
    {"name": "valid_user", "email": "yadavdeepa365@gmail.com", "password": "Google123$"},
    ]      

def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n User %s is not defined" %name)