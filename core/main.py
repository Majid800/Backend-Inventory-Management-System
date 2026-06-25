from medicines_database import MedicineDatabase
from manual_entry import ( search_medicine_manually, delete_medicine_manually,)
from barcode import add_medicine_by_barcode, search_medicine_by_name_or_barcode
from stock_manager import view_stock 

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

                add_medicine_by_barcode()

            elif choice == "2":
                search_medicine_by_name_or_barcode()
            
            elif choice =="3":
                delete_medicine_manually(database)

            elif choice =="4":
                view_stock()
                

            elif choice == "5":
                print("\nExiting.")
                break 
            
            else: 
                print("\nInvalid choice. please try again.")

if __name__ == "__main__":
    main()