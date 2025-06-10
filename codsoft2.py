contact = {}

def display_contact():
    print("\nName\t\tContact Number")
    for key in contact:
        print(f"{key}\t\t{contact.get(key)}")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View Contact List")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print(" Invalid input! Please enter a number.")
        continue

    if choice == 1:
        name = input("Enter the contact name: ").strip()
        phone = input("Enter the mobile number: ").strip()
        contact[name] = phone
        print(" Contact added.")

    elif choice == 2:
        search_name = input("Enter the contact name to search: ").strip()
        if search_name in contact:
            print(f"{search_name}'s contact number is {contact[search_name]}")
        else:
            print(" Name not found in contact book.")

    elif choice == 3:
        if not contact:
            print(" Contact book is empty.")
        else:
            display_contact()

    elif choice == 4:
        edit_contact = input("Enter the contact name to update: ").strip()
        if edit_contact in contact:
            phone = input("Enter new mobile number: ").strip()
            contact[edit_contact] = phone
            print(" Contact updated.")
            display_contact()
        else:
            print(" Name not found in contact book.")

    elif choice == 5:
        del_contact = input("Enter the contact name to delete: ").strip()
        if del_contact in contact:
            confirm = input("Are you sure you want to delete this contact? (yes/no): ").lower()
            if confirm == 'yes':
                contact.pop(del_contact)
                print(" Contact deleted.")
                display_contact()
        else:
            print(" Name not found in contact book.")

    elif choice == 6:
        print(" Exiting contact book. Goodbye!")
        break

    else:
        print(" Invalid choice. Please select from 1 to 6.")
