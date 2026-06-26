from database import connect 


def dispense_stock():
    conn = connect()
    cursor = conn.cursor()
    barcode = input("\nScan medicine barcode: ").strip()
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
    stock = medicine[4]
    if stock <= 0:
        print("\nStock discrepency detected.")
        print("Recorded stock quantity is already zero.")
        print("Please perform a stock adjustment if the medicine is physically available.")
        
        cursor.close()
        conn.close()
        return
    cursor.execute(
        """
        UPDATE stock
        SET stock_quantity = stock_quantity - 1
        WHERE medicine_code = %s
        """,
        (medicine_code,)
    )
    conn.commit()
    print(
        f"\n{name} {strength} {formulation}"
    )
    print(f"Stock updated: {stock} → {stock - 1}")
    cursor.close()
    conn.close()

def cancel_dispensing():
    conn = connect()
    cursor = conn.cursor()
    barcode = input("\nScan medicine barcode: ").strip()
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
    stock = medicine[4]
    cursor.execute(
        """
        UPDATE stock
        SET stock_quantity = stock_quantity + 1
        WHERE medicine_code = %s
        """,
        (medicine_code,)
    )
    conn.commit()
    print(
        f"\n{name} {strength} {formulation}"
    )
    print(f"Stock updated: {stock} → {stock + 1}")
    cursor.close()
    conn.close()



if __name__ == "__main__":
    cancel_dispensing()