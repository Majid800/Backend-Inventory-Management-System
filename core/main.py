from medicines_database import MedicineDatabase
from manual_entry import (add_medicine_manually, search_medicine_manually, delete_medicine_manually, list_all_medicines)

def display_menu():

    print("\n========================")
    print(" Pharmacy Inventory System")
    print("====================")
    print("1. Add Medicine")
    print("2. Search Medicine")
    print("3. Delete Medicine")
    print("4. List All Medicines")
    print("5. Exit")

def main():
        database = MedicineDatabase()

        while True: 
            display_menu()

            choice = input("\nChoose an option: ").strip()

            if choice == "1":

                add_medicine_manually(database)

            elif choice == "2":
                search_medicine_manually(database)
            
            elif choice =="3":
                delete_medicine_manually(database)

            elif choice =="4":
                list_all_medicines(database)

            elif choice == "5":
                print("\nExiting.")
                break 
            
            else: 
                print("\nInvalid choice. please try again.")

if __name__ == "__main__":
    main()