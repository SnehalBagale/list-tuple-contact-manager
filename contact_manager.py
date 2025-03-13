contacts = []

def add_contact(name, email, phone):
    contacts.append((name, email, phone))
    print("Contact added successfully!")
    print("\n------------------------------------------------")


def view_contacts():
    if not contacts:
        print("No contact found.")
        print("\n------------------------------------------------")

    else:
        print("\nList Of contacts")
        print("------------------------------------------------")
        for name, email, phone in contacts:
            print(f"Name: {name}, Email: {email}, Phone: {phone}")
            print("\n------------------------------------------------")


def search_contact(name):
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"Name: {contact[0]}, Email: {contact[1]}, Phone: {contact[2]}")
            print("\n------------------------------------------------")

            return
    print("Contact not found.")
    print("\n------------------------------------------------")


def update_phone(name, new_phone):
    for i, contact in enumerate(contacts):
        if contact[0].lower() == name.lower():
            contacts[i] = (contact[0], contact[1], new_phone)
            print("Phone number updated successfully!")
            print("\n------------------------------------------------")
            return
    print("\nContact not found.")
    print("\n------------------------------------------------")



def delete_contact(name):
    global contacts
    if not contacts:
        print("There is no data for delete.")
        print("\n------------------------------------------------")
        return
    contacts = [contact for contact in contacts if contact[0].lower() != name.lower()]
    print("Contact deleted successfully!")
    print("\n------------------------------------------------")


while True:
    print("\nWelcome to Contact Manager")
    choice = input("\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit\n\nEnter your choice: ")
    if choice == "1":
        add_contact(input("Name: "), input("Email: "), input("Phone: "))
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact(input("Name: "))
    elif choice == "4":
        update_phone(input("Name: "), input("New Phone: "))
    elif choice == "5":
        delete_contact(input("Name: "))
    elif choice == "6":
        print("Exiting Contact Manager. Goodbye!")
        break
    else:
        print("Invalid choice!")
