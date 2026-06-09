import hashlib
from storage import save_users

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(users):
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == "":
        print("Username cannot be empty!")
        return
    if password == "":
        print("Password cannot be empty!")
        return
    password = hash_password(password)

    for user in users:
        if user["username"] == username:
            print("Username already exists!") 
            return
    else:
        users.append({"username":username, "password":password})
        save_users(users)
        print("User registered successfully!")
    
def login_user(users):

    attempt = 3

    if not users: 
        print("No users registered")
        return
        
    while attempt > 0:
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        if username == "" or password == "":
            print("Fields cannot be empty!")
            continue
        hashed_pass = hash_password(password)
        for user in users:
            if user["username"] == username and user["password"] == hashed_pass:
                print(f"Welcome {username}!")
                return
        attempt -= 1
        print(f"Invalid credentials. Attempts left: {attempt}")

    if attempt == 0:
        print("Too many failed attempts! Access denied.")

def user_view(users):
    if users:
        print("\n--- USERS ---")
        for i, user in enumerate(users, start=1):
            print(f"{i}. {user['username']}")
    else:
        print("No registered user!")
    
def user_update(users):
    username = input("Enter username: ").strip()

    if username == "":
        print("Username cannot be empty!")
        return

    for user in users:
        if user["username"] == username:
            new_pass = input("Enter new password: ").strip()
            if new_pass == "":
                print("Password cannot be empty!")
                return
            user["password"] = hash_password(new_pass)
            save_users(users)
            print("User updated successfully!")
            return
    else:
        print("User not found!")
    
def user_remove(users):
    username = input("Enter username: ").strip()

    for user in users:
        if user["username"] == username:
            users.remove(user)
            save_users(users)
            print("User deleted successfully!")
            return
    else:
        print("User not found!")
