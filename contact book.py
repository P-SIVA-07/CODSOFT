class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        print("Contact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, keyword):
        result = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                result.append(contact)
        return result

    def update_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == old_name:
                self.contacts[i] = new_contact
                print(f"{old_name}'s contact updated successfully.")
                return
        print(f"Contact with name {old_name} not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print(f"{name}'s contact deleted successfully.")
                return
        print(f"Contact with name {name} not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == "2":
            contact_manager.view_contact_list()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            search_result = contact_manager.search_contact(keyword)
            if search_result:
                print("\nSearch Result:")
                for contact in search_result:
                    print(f"Name: {contact.name}, Phone: {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            name = input("Enter name of contact to update: ")
            updated_name = input("Enter updated name: ")
            phone = input("Enter updated phone number: ")
            email = input("Enter updated email: ")
            address = input("Enter updated address: ")
            updated_contact = Contact(updated_name, phone, email, address)
            contact_manager.update_contact(name, updated_contact)

        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

