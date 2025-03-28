class Item:
    def __init__(self, id, name, description, price):
        """
        Initialize an Item object.

        :param id: Unique identifier for the item.
        :param name: Name of the item.
        :param description: Description of the item.
        :param price: Price of the item.
        """
        
        
        
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"


class ItemManagementSystem:
    def __init__(self):
        """
        Initialize the item management system with an empty dictionary.
        """
        self.items = {}

    def create_item(self, id, name, description, price):
        """
        Create a new item and add it to the system.



        :param id: Unique identifier for the item.
        :param name: Name of the item.
        :param description: Description of the item.
        :param price: Price of the item.
        :raises ValueError: If the item ID already exists or if any field is invalid.
        """
        if id in self.items:
            raise ValueError("Item ID already exists.")

        if not isinstance(id, int) or id <= 0:
            raise ValueError("Invalid ID. ID must be a positive integer.")

        if not name or not description:
            raise ValueError("Name and description cannot be empty.")

        try:
            price = float(price)
            if price <= 0:
                raise ValueError("Price must be a positive number.")
        except ValueError:
            raise ValueError("Invalid price. Price must be a number.")



        new_item = Item(id, name, description, price)
        self.items[id] = new_item
        print(f"Item created successfully: {new_item}")

    def read_item(self, id):
        """
        Retrieve an item by its ID.

        :param id: ID of the item to retrieve.
        :return: The item if found, otherwise None.
        :raises ValueError: If the ID is invalid.
        """
        
        
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Invalid ID. ID must be a positive integer.")

        return self.items.get(id)

    def update_item(self, id, name=None, description=None, price=None):
        """
        Update an existing item.

        :param id: ID of the item to update.
        :param name: New name for the item.
        :param description: New description for the item.
        :param price: New price for the item.
        :raises ValueError: If the item ID does not exist or if any field is invalid.
        """
        if id not in self.items:
            raise ValueError("Item ID does not exist.")

        item = self.items[id]

        if name:
            if not name:
                raise ValueError("Name cannot be empty.")
            item.name = name

        if description:
            if not description:
                raise ValueError("Description cannot be empty.")
            item.description = description

        if price:
            try:
                price = float(price)
                if price <= 0:
                    raise ValueError("Price must be a positive number.")
                item.price = price
            except ValueError:
                raise ValueError("Invalid price. Price must be a number.")

        print(f"Item updated successfully: {item}")

    def delete_item(self, id):
        """
        Delete an item by its ID.

        :param id: ID of the item to delete.
        :raises ValueError: If the item ID does not exist or if the ID is invalid.
        """
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Invalid ID. ID must be a positive integer.")

        if id not in self.items:
            raise ValueError("Item ID does not exist.")

        del self.items[id]
        print(f"Item with ID {id} deleted successfully.")

    def list_items(self):
        """
        List all items in the system.
        """
        if not self.items:
            print("No items in the system.")
        else:
            for item in self.items.values():
                print(item)


# Example usage
if __name__ == "__main__":
    system = ItemManagementSystem()

    while True:
        print("\nItem Management System Menu:")
        print("1. Create Item")
        print("2. Read Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. List Items")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                id = int(input("Enter item ID: "))
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = input("Enter item price: ")
                system.create_item(id, name, description, price)
            elif choice == "2":
                id = int(input("Enter item ID to read: "))
                item = system.read_item(id)
                if item:
                    print(item)
                else:
                    print("Item not found.")
            elif choice == "3":
                id = int(input("Enter item ID to update: "))
                name = input("Enter new name (leave blank if no change): ")
                description = input("Enter new description (leave blank if no change): ")
                price = input("Enter new price (leave blank if no change): ")
                system.update_item(id, name or None, description or None, price or None)
            elif choice == "4":
                id = int(input("Enter item ID to delete: "))
                system.delete_item(id)
            elif choice == "5":
                system.list_items()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError as e:
            print(f"Error: {e}")
