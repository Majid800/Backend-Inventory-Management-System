from medicines import Medicine
from database import search_by_barcode, add_medicine, search_medicine_stock
from code_generator import generate_medicine_code
from stock_manager import update_stock
from barcode_processor import process_barcode




def add_medicine_by_barcode():
    barcode = process_barcode(input("Scan or type barcode: ").strip())

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
    manufacturer = input("Manufacturer: ").strip() or None
    pack_size = (int(input("Pack size: ").strip()))
    code = generate_medicine_code(name,strength, formulation, manufacturer, pack_size)
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

def search_medicine_by_name_or_barcode():
    search_term = input("\nEnter medicine name or barcode: ").strip()
    processed = process_barcode(search_term)
    if processed is not None:
        search_term = processed
    
    results = search_medicine_stock(search_term)
    if not results:
        print("\nNo medicine found.")
        return
    print("\n" + "=" * 130)
    print(f"{'CODE':<20}{'NAME':<20}{'STRENGTH':<15}{'FORM':<12}{'MANUFACTURER':<15}{'BARCODE':<18}{'STOCK':<8}{'STATUS'}")
    print("-" * 130)
    for code, name, strength, formulation, manufacturer, barcode, stock in results:
        if stock == 0:
            status = "OUT OF STOCK"
        elif stock <= 5:
            status = "LOW STOCK"
        else:
            status = "OK"
        print(f"{code:<20}{name:<20}{strength:<15}{formulation:<12}{manufacturer:<15}{(barcode or 'N/A'):<18}{stock:<8}{status}")
    print("=" * 130)

if __name__ == "__main__":
    search_medicine_by_name_or_barcode()
   