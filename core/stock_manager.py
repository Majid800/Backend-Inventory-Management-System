from database import connect 

def view_stock():
    medicine_code = input("Enter medicine code: ").strip().upper()
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT stock_quantity
            FROM stock
            WHERE medicine_code = %s
        """, (medicine_code,))
        result = cursor.fetchone()
        if result:
            print(f"\nMedicine Code: {medicine_code}")
            print(f"Stock Quantity: {result[0]}")
        else:
            print("\nMedicine not found in stock table.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
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

if __name__ =="__main__":
    view_stock()

 
