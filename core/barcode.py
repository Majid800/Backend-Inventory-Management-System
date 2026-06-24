from medicines import Medicine
from database import search_by_barcode, add_medicine
from code_generator import generate_medicine_code


def add_medicine_by_barcode():
    barcode = input("Scan or type barcode: ").strip()

    existing = search_by_barcode(barcode)

    if existing:
        print("\nMedicine already exists in the database:")
        print(existing)
        return

    print("\nBarcode not found. Enter new medicine details.")

    name = input("Name: ").strip()
    strength = input("Strength: ").strip()
    formulation = input("Formulation: ").strip()
    code = generate_medicine_code(name,strength, formulation)
    manufacturer = input("Manufacturer (press Enter if unknown): ").strip() or None
    pack_size = int(input("Pack size: ").strip())
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
    print("\nMedicine added successfully.")


if __name__ == "__main__":
    add_medicine_by_barcode()