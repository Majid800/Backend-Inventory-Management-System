from medicines import Medicine
import psycopg 

def connect():
    conn = psycopg.connect(host ="localhost", dbname ="pharmacy_inventory", user="postgres", password ="King1978!")
    return conn 



def get_all_medicines():
    conn = psycopg.connect(host = "localhost", dbname="pharmacy_inventory", user ="postgres", password ="King1978!")
    cur = conn.cursor()
    cur.execute("SELECT * FROM medicines ORDER BY id ASC;")
    rows = cur.fetchall()

    print("\nid, Name, Strength, Formulation, Medicine Code, Barcode, Manufacturer, Pack size, Controlled Drug\n")
    for row in rows:
        print(row)

    cur.close()
    conn.close()

def add_medicine(medicine):
        conn = psycopg.connect(
        host="localhost",
        dbname="pharmacy_inventory",
        user="postgres",
        password="King1978!"
    )
        cur = conn.cursor()
        cur.execute(
        """
        INSERT INTO medicines
        (name, strength, formulation, code, barcode, manufacturer, pack_size, notes, is_controlled)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            medicine.name,
            medicine.strength,
            medicine.formulation,
            medicine.code,
            medicine.barcode,
            medicine.manufacturer,
            medicine.pack_size,
            medicine.notes,
            medicine.is_controlled
        )
    )

    
        conn.commit()
        cur.close()
        conn.close()


def search_by_code(code):
    conn = psycopg.connect(
        host="localhost",
        dbname="pharmacy_inventory",
        user="postgres",
        password="King1978!"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM medicines WHERE code = %s",
        (code,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def delete_by_code(code):
    conn = psycopg.connect(
        host="localhost",
        dbname="pharmacy_inventory",
        user="postgres",
        password="King1978!"
    )
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM medicines WHERE code = %s",
        (code,)
    )
    conn.commit()
    cur.close()
    conn.close()

def search_by_barcode(barcode):
    conn = psycopg.connect(
        host="localhost",
        dbname="pharmacy_inventory",
        user="postgres",
        password="King1978!"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM medicines WHERE barcode = %s",
        (barcode,)
    )
    medicine = cur.fetchone()
    cur.close()
    conn.close()
    return medicine

def search_medicine_stock(search_term):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            m.code,
            m.name,
            m.strength,
            m.formulation,
            m.manufacturer,
            m.barcode,
            COALESCE(s.stock_quantity, 0) AS stock_quantity
        FROM medicines m
        LEFT JOIN stock s
            ON s.medicine_code = m.code
        WHERE m.barcode = %s
           OR m.name ILIKE %s
        ORDER BY
            CASE WHEN m.barcode = %s THEN 0 ELSE 1 END,
            m.name ASC,
            m.strength ASC;
    """, (search_term, f"{search_term}%", search_term))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def delete_medicine():
    conn = connect()
    cursor = conn.cursor()
    search_name = input("Enter medicine name: ").strip()
    cursor.execute(
        """
        SELECT id, name, strength, formulation
        FROM medicines
        WHERE LOWER(name) LIKE LOWER(%s)
        ORDER BY name, strength;
        """,
        (f"%{search_name}%",)
    )
    medicines = cursor.fetchall()
    if not medicines:
        print("No medicines found.")
        cursor.close()
        conn.close()
        return
    print("\nMatching medicines:\n")
    for index, medicine in enumerate(medicines, start=1):
        print(
            f"{index}. "
            f"{medicine[1]} "
            f"{medicine[2]} "
            f"{medicine[3]}"
        )
    try:
        choice = int(input("\nSelect medicine to delete: "))
        if choice < 1 or choice > len(medicines):
            print("Invalid selection.")
            cursor.close()
            conn.close()
            return
    except ValueError:
        print("Please enter a valid number.")
        cursor.close()
        conn.close()
        return
    selected = medicines[choice - 1]
    confirm = input(
        f"\nDelete {selected[1]} {selected[2]} {selected[3]}? (Y/N): "
    ).upper()
    if confirm == "Y":
        cursor.execute(
            """
            DELETE FROM medicines
            WHERE id = %s
            """,
            (selected[0],)
        )
        conn.commit()
        print("Medicine deleted successfully.")
    else:
        print("Deletion cancelled.")
    cursor.close()
    conn.close()




if __name__ == "__main__":
     delete_medicine()