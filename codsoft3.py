contacts = {}

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    contacts[name] = {'phone': phone}
    print("✅ Contact added successfully!")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n--- Contact List ---")
    for name, details in contacts.items():
        print(f"\nName : {name}")
        print(f"Phone: {details['phone']}")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        details = contacts[name]
        print(f"\nName : {name}")
        print(f"Phone: {details['phone']}")
    else:
        print("❌ Contact not found.")

def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contacts:
        phone = input("New Phone: ").strip()
        contacts[name]['phone'] = phone
        print("🔄 Contact updated successfully.")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("🗑️ Contact deleted.")
    else:
        print("❌ Contact not found.")

def menu():
    while True:
        print("\n📇 --- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

# Ensure the main menu runs
if __name__ == "__main__":
    menu()

