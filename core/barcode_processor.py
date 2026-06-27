import re

def process_barcode(barcode):
    barcode = barcode.strip()
    # Normal EAN-13 barcode
    if barcode.isdigit() and len(barcode) == 13:
        return barcode
    # GS1 barcode
    match = re.search(r"01(\d{14})", barcode)
    if match:
        gtin = match.group(1)
        # Convert GTIN-14 back to EAN-13
        if gtin.startswith("0"):
            return gtin[1:]
        return gtin
    return None