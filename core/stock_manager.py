from database import connect 

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
    print(f"{'CODE':<12}{'NAME':<20}{'STRENGTH':<15}{'FORMULATION':<12}{'STOCK':<8}{'STATUS'}")
    print("-" * 90)
    for code, name, strength, formulation, qty in rows:
        if qty == 0:
            status = "OUT OF STOCK"
        elif qty <= LOW_STOCK_THRESHOLD:
            status = "LOW STOCK"
        else:
            status = "OK"
        print(f"{code:<12}{name:<20}{strength:<15}{formulation:<12}{qty:<8}{status}")
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

if __name__ =="__main__":
    view_stock()

 
