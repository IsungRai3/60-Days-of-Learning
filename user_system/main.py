from storage import load_users
from auth import register_user, login_user, user_view, user_update, user_remove

users = load_users()

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
        register_user(users)
        
    elif choice == "2":
        login_user(users)

    elif choice == "3":
        user_view(users)

    elif choice == "4":
        user_update(users)

    elif choice == "5":
        user_remove(users)

    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Error: Invalid choice! Try again!")
        