members = []
while True:
    print("\nGYM MANAGER")
    print("1. Add Member")
    print("2. View Members")
    print("3. Search Member")
    print("4. Delete Member")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter member name: ")
        age = input("Enter age: ")
        print("Enter how many months you want to subscribe for")
        plan = input("Enter membership plan:")

        member = {"name": name,
            "age": age,
            "plan": plan}

        members.append(member)
        print("Member added successfully")

    elif choice=="2":
        if len(members) == 0:
            print("No members found")
        else:
            print("\nMembers:")

            for i in range(len(members)):
                print("Member", i + 1)
                print("Name:", members[i]["name"])
                print("Age:", members[i]["age"])
                print("Plan:", members[i]["plan"])
                print()

    elif choice =="3":
        name = input("Enter member name: ")
        found = False

        for member in members:
            if member["name"].lower()== name.lower():
                print("Member found")
                print("Name:", member["name"])
                print("Age:", member["age"])
                print("Plan:", member["plan"])
                found = True
                break

        if found == False:
            print("Member not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        found = False

        for member in members:
            if member["name"].lower() == name.lower():
                members.remove(member)
                print("Member deleted successfully")
                found = True
                break
        if found==False:
            print("Member not found")
    elif choice=="5":
        print("Thank you for using Gym Manager")
        break
    else:
        print("Invalid choice, Pls enter a valid input")