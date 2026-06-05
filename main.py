users = []

#FUNCTIONS
def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user["username"] == username:
            print("Username already exists!") 
            return
    else:
        users.append({"username":username, "password":password})
        print("User registered successfully!")
    
def login_user():

    attempt = 3

    if not users: 
        print("No users registered")
        return
        
    while attempt > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in users:
            if user["username"] == username and user["password"] == password:
                print(f"Welcome {username}!")
                return
        attempt -= 1
        print(f"Invalid credentials. Attempts left: {attempt}")

    if attempt == 0:
        print("Too many failed attempts! Access denied.")

def user_view():
    if users:
        print("\n---User---")
        for i, user in enumerate(users, start=1):
            print(f"{i}. {user['username']}")
    else:
        print("No registered user!")
    
def user_update():
    username = input("Enter username: ")

    for user in users:
        if user["username"] == username:
            new_pass = input("Enter new password: ")
            user["password"] = new_pass
            print("User updated successfully!")
            return
    else:
        print("User not found!")
    
def user_remove():
    username = input("Enter username: ")

    for user in users:
        if user["username"] == username:
            users.remove(user)
            print("User deleted successfully!")
            return
    else:
        print("User not found!")


while True:
    print("\n=== MENU ===")
    print("1.Register user")
    print("2.Login")
    print("3.View all users")
    print("4.Update user")
    print("5.Delete user")
    print("6.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_user()
        
    elif choice == "2":
        login_user()

    elif choice == "3":
        user_view()

    elif choice == "4":
        user_update()

    elif choice == "5":
        user_remove()

    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Error: Invalid choice! Try again!")
        