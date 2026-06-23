#User manual entry of medicines
# - Ask Questions
# - Validate Answers
# - Generate Code
# - Create Medicine Object
# - Save to Database

from medicines import Medicine 
from medicines_database import MedicineDatabase 
from code_generator import generate_medicine_code 

#While true loop to get a non empty input
def get_non_empty_input(prompt: str):
    while True:
        value = input(prompt).strip()

        if value:
            return value 
        print("This field cannot be empty")

def get_positive_int(prompt: str):
    while True:
        value= input(prompt).strip()
        try:
            number = int(value)

            if number < 0:
                print("Please enter a number of 0 or more")
                continue 
            return number 

        except ValueError:
            print("Please enter a whole number.")

def get_yes_No(prompt:str):
    while True:
        value = input(prompt).strip().lower()
        
        if value in ("y", "yes"):
            return True 
        if value in ("n", "no"):
            return False 
        print("please enter y or n")

def add_medicine_manually(database: MedicineDatabase):
    print("\n--- Add Medicine Manually---")

    name = get_non_empty_input("Medicine Name: "
    )
    strength = get_non_empty_input("strength: "
    )
    formulation = get_non_empty_input("Forumlation: "
    )
    pack_size = get_positive_int("Pack size: "
    )
    manufacturer = get_non_empty_input("Manufacturer: "
    )
    is_controlled = get_yes_No("controlled Drug? (y/n):"
    )

    code = generate_medicine_code(
        name,
        strength,
        formulation 
    )
    medicine = Medicine(name = name, strength = strength, formulation = formulation, pack_size=  pack_size, 
                        manufacturer = manufacturer, code = code, is_controlled = is_controlled)
    
    try:
        database.add_medicine(medicine)
        print("\nMedicine Added Successfully.")
        print(f"Generated Code: {medicine.code}")
    except ValueError as error:
        print(f"\nError: {error}")

def search_medicine_manually(database:MedicineDatabase):
        print("\n--- Search Medicine ---")
        code = get_non_empty_input("Enter Medicine Code: ")

        medicine = database.search_by_code(code)

        if medicine:
            print("\nMedicine Found:\n")
            print(medicine)
        else: 
            print("\nMedicine not found.")

def delete_medicine_manually(database:MedicineDatabase):
        print("\n--- Delete Medicine ---")
        code = get_non_empty_input("Enter Medicine Code: ")
        deleted = database.delete_medicine(code)
        if deleted: 
            print("\nMedicine Deleted Successfully.")
        else: 
            print("\n Medicine Not Found.")

def list_all_medicines(database:MedicineDatabase):
        print("\n--- All Medicines ---")
        medicines = database.list_all_medicines()
        if not medicines:
            print (" No medicines in database.")
            return 
        
        for number, medicine in enumerate(medicines, start = 1):
            print(f"\n{number}.")
            print(medicine)
            print("-" * 30 )