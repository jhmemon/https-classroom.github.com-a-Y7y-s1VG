import mysql.connector

"""""
def get_db_connection():
    return mysql.connector.connect(
        host="database1.cm5ge0qyc76x.us-east-1.rds.amazonaws.com",
        user="admin",
        password="Jazib!23",
        database="database1"
    )
"""
"""
def view_shopping_list():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM shopping_list")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Item: {row[1]}, Quantity: {row[2]}, Added On: {row[3]}")
    cursor.close()
    connection.close()
"""
"""
def add_item_to_shopping_list():
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO shopping_list (item_name, quantity) VALUES (%s, %s)", (item_name, quantity))
    connection.commit()
    print("Item added successfully!")
    cursor.close()
    connection.close()

"""
"""
def delete_item_from_shopping_list():
    item_id = int(input("Enter the ID of the item to delete: "))
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM shopping_list WHERE id = %s", (item_id,))
    connection.commit()
    print("Item deleted successfully!")
    cursor.close()
    connection.close()
"""
"""
def display_menu():
    print("=== Shopping List Application ===")
    print("1. View Shopping List")
    print("2. Add Item to Shopping List")
    print("3. Delete Item from Shopping List")
    print("4. Exit")
"""

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_shopping_list()
        elif choice == "2":
            add_item_to_shopping_list()
        elif choice == "3":
            delete_item_from_shopping_list()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")