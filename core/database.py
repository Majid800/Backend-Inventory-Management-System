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

if __name__ == "__main__":
    get_all_medicines()