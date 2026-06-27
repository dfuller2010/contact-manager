import json

FILENAME = "contacts.json"

contacts = []

def load_contacts():
    global contacts
    try:
        with open(FILENAME, "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []


def save_contacts():
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    notes = input("Notes: ")

    contact = {
        "name": name,
        "email": email,
        "phone": phone,
        "notes": notes
    }

    contacts.append(contact)
    save_contacts()
    print(f"\n{name} added!")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts yet.")
        return

    for i, contact in enumerate(contacts):
        print(f"\n{i + 1}. {contact['name']}")
        print(f"   Email: {contact['email']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Notes: {contact['notes']}")

def search_contacts():
    term = input("Search by name: ").lower()

    results = []
    for contact in contacts:
        if term in contact["name"].lower():
            results.append(contact)

    if len(results) == 0:
        print("No contacts found.")
        return

    for contact in results:
        print(f"\n{contact['name']}")
        print(f"   Email: {contact['email']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Notes: {contact['notes']}")

def delete_contact():
    if len(contacts) == 0:
        print("No contacts yet.")
        return

    view_contacts()
    number = input("\nEnter the number of the contact to delete: ")
    index = int(number) - 1

    if index < 0 or index >= len(contacts):
        print("Invalid number.")
        return

    name = contacts[index]["name"]
    contacts.pop(index)
    save_contacts()
    print(f"{name} deleted.")

def main():
    load_contacts()
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contacts")
        print("4. Delete a contact")
        print("5. Quit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


main()