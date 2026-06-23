from medicines import Medicine
import psycopg 
def connect():
    conn = psycopg.connect(host ="localhost", dbname ="pharmacy_inventory", user="postgres", password ="King1978!")
    print("Connected Succesfully!")
    conn.close()



def get_all_medicines():
    conn = psycopg.connect(host = "localhost", dbname="pharmacy_inventory", user ="postgres", password ="King1978!")
    cur = conn.cursor()
    cur.execute("SELECT * FROM medicines ORDER BY id ASC;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def add_medicine(medicine):
        conn = psycopg.connect(
        host="localhost",
        dbname="pharmacy_inventory",
        user="postgres",
        password="King1978"
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
        password="King1978"
    )
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM medicines WHERE code = %s",
        (code,)
    )
    conn.commit()
    cur.close()
    conn.close()






if __name__ == "__main__":
    result = search_by_code("PAR500TAB")
    print(result)