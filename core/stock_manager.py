from database import connect 
from barcode_processor import process_barcode

LOW_STOCK_THRESHOLD = 5
def view_stock():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            m.code,
            m.name,
            m.strength,
            m.formulation,
            COALESCE(s.stock_quantity, 0) AS stock_quantity
        FROM medicines m
        LEFT JOIN stock s
            ON s.medicine_code = m.code
        ORDER BY m.name ASC;
    """)
    rows = cursor.fetchall()
    print("\n" + "=" * 90)
    print(f"{'CODE':<20}{'NAME':<20}{'STRENGTH':<15}{'FORMULATION':<12}{'STOCK':<8}{'STATUS'}")
    print("-" * 90)
    for code, name, strength, formulation, qty in rows:
        if qty == 0:
            status = "OUT OF STOCK"
        elif qty <= LOW_STOCK_THRESHOLD:
            status = "LOW STOCK"
        else:
            status = "OK"
        print(f"{code:<20}{name:<20}{strength:<15}{formulation:<12}{qty:<8}{status}")
    print("=" * 90)
    cursor.close()
    conn.close()

    


def update_stock(medicine_code):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO stock (medicine_code, stock_quantity)
        VALUES (%s, 1)
        ON CONFLICT (medicine_code)
        DO UPDATE SET stock_quantity = stock.stock_quantity + 1
    """, (medicine_code,))
    conn.commit()
    cursor.close()
    conn.close()

def stock_adjustment():
    conn = connect()
    cursor = conn.cursor()

    print("\n==========================")
    print("     STOCK ADJUSTMENT")
    print("==========================")
    barcode = process_barcode(
        input("\nScan medicine barcode: ")
    )
    cursor.execute(
        """
        SELECT
            m.code,
            m.name,
            m.strength,
            m.formulation,
            s.stock_quantity
        FROM medicines m
        JOIN stock s
            ON m.code = s.medicine_code
        WHERE m.barcode = %s
        """,
        (barcode,)
    )
    medicine = cursor.fetchone()
    if medicine is None:
        print("Medicine not found.")
        cursor.close()
        conn.close()
        return
    medicine_code = medicine[0]
    name = medicine[1]
    strength = medicine[2]
    formulation = medicine[3]
    current_stock = medicine[4]
    print(f"\n{name} {strength} {formulation}")
    print(f"Current stock: {current_stock}")
    try:
        new_stock = int(
            input("\nEnter corrected stock quantity: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        cursor.close()
        conn.close()
        return
    if new_stock < 0:
        print("Stock cannot be negative.")
        cursor.close()
        conn.close()
        return
    cursor.execute(
        """
        UPDATE stock
        SET stock_quantity = %s
        WHERE medicine_code = %s
        """,
        (new_stock, medicine_code)
    )
    conn.commit()
    print("\nStock adjusted successfully.")
    print(f"Previous stock : {current_stock}")
    print(f"Current stock  : {new_stock}")
    cursor.close()
    conn.close()




if __name__ =="__main__":
    stock_adjustment()

 
