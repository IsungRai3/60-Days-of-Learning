users = []

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
        username = input("Enter username: ")
        password = input("Enter password: ")

        exists = False

        for user in users:
            if user["username"] == username:
                exists = True
                break

        if exists:
            print("Username already exists!") 
    
        else:
            users.append({"username":username, "password":password})
            print("User registered successfully!")
    
    elif choice == "2":

        attempt = 3

        if not users: 
                print("No users registered")
                continue
        
        while attempt > 0:
            username = input("Enter username: ")
            password = input("Enter password: ")
            found = False

            for user in users:
                if user["username"] == username and user["password"] == password:
                    print(f"Welcome {username}!")
                    found = True
                    break
                
            if found:
                break

            if not found:
                attempt -= 1
                print(f"Invalid credentials. Attempts left: {attempt}")

        if attempt == 0:
            print("Too many failed attempts! Access denied.")

    elif choice == "3":
        if users:
            print("\n*** User ***")
            for i, user in enumerate(users, start=1):
                print(f"{i}. {user['username']}")
        else:
            print("No registered user!")
    
    elif choice == "4":
        username = input("Enter username: ")

        found = False

        for user in users:
            if user["username"] == username:
                new_pass = input("Enter new password: ")
                user["password"] = new_pass
                print("User update successfully!")
                found = True
                break
        if not found:
            print("User not found!")
    
    elif choice == "5":
        username = input("Enter username: ")
        found = False

        for user in users:
            if user["username"] == username:
                users.remove(user)
                print("User deleted successfully!")
                found = True
                break
            
        if not found:
            print("User not found!")


    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Error: Invalid choice! Try again!")
        