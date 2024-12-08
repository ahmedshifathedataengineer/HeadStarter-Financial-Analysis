import psycopg2

# Set up your database connection
DB_CONFIG = {
    "dbname": "yourdb",
    "user": "youruser",
    "password": "yourpass",
    "host": "localhost",
    "port": 5432
}

def save_to_db(data):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO articles (title, author, publish_date, text)
            VALUES (%s, %s, %s, %s)
            """,
            (data["title"], ", ".join(data["author"]), data["publish_date"], data["text"])
        )
        conn.commit()
        cursor.close()
        conn.close()
        print("Article saved to database.")
    except Exception as e:
        print(f"Error saving to database: {e}")
