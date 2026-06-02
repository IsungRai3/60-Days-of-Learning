user = {}

while True:
    print("\n===MENU===")
    print("1.Create")
    print("2.View")
    print("3.Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        user["name"] = name
        user["age"] = age

        print("Created successfully!!")

    elif choice == "2":
        if user:
            print("\n*** USER-INFO ***")
            print(f"Name: {user['name']}")
            print(f"age: {user['age']}")
        else:
            print("Error: User not found!")
    
    elif choice == "3":
        print("Exiting program....")
        break

    else:
        print("Error: Invalid choice! Try again!")