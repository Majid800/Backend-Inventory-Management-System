from medicines import Medicine
from database import search_by_barcode, add_medicine
from code_generator import generate_medicine_code
from stock_manager import update_stock


def add_medicine_by_barcode():
    barcode = input("Scan or type barcode: ").strip()

    existing = search_by_barcode(barcode)

    if existing:
        medicine_code = existing[4]
        update_stock(medicine_code)
        
        print("\nMedicine already exists.")
        print("stock increased by 1")
        return

    print("\nBarcode not found. Enter new medicine details.")

    name = input("Name: ").strip()
    strength = input("Strength: ").strip()
    formulation = input("Formulation: ").strip()
    code = generate_medicine_code(name,strength, formulation)
    manufacturer = input("Manufacturer (press Enter if unknown): ").strip() or None
    pack_size = (int(input("Pack size: ").strip()))
    notes = input("Notes (press Enter if none): ").strip() or None
    is_controlled = input("Is controlled? (y/n): ").strip().lower() == "y"

    
    
    medicine = Medicine(
        name=name,
        strength=strength,
        formulation=formulation,
        code=code,
        barcode=barcode,
        manufacturer=manufacturer,
        pack_size=pack_size,
        notes=notes,
        is_controlled=is_controlled
    )

    add_medicine(medicine)
    update_stock(medicine.code)
    print("\nMedicine added successfully.")
    print(f"{medicine.name} = 1")


if __name__ == "__main__":
    add_medicine_by_barcode()