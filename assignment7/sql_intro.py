import sqlite3
import os

db_path = "../db/magazines.db"

# Delete the database if it already exists (optional for testing)
if os.path.exists(db_path):
    os.remove(db_path)

try:
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    print("Database connected successfully.")

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY(subscriber_id) REFERENCES subscribers(subscriber_id),
        FOREIGN KEY(magazine_id) REFERENCES magazines(magazine_id)
    )""")

    # Functions to add data
    def add_publisher(cursor, name):
        try:
            cursor.execute("SELECT * FROM publishers WHERE name = ?", (name,))
            if cursor.fetchone():
                print(f"Publisher '{name}' already exists.")
                return
            cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        except sqlite3.Error as e:
            print(f"Error inserting publisher: {e}")

    def add_magazine(cursor, name, publisher_name):
        try:
            cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
            publisher = cursor.fetchone()
            if not publisher:
                print(f"Publisher '{publisher_name}' not found.")
                return
            publisher_id = publisher[0]

            cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
            if cursor.fetchone():
                print(f"Magazine '{name}' already exists.")
                return

            cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        except sqlite3.Error as e:
            print(f"Error inserting magazine: {e}")

    def add_subscriber(cursor, name, address):
        try:
            cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
            if cursor.fetchone():
                print(f"Subscriber '{name}' at '{address}' already exists.")
                return
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        except sqlite3.Error as e:
            print(f"Error inserting subscriber: {e}")

    def add_subscription(cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):
        try:
            cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", (subscriber_name, subscriber_address))
            subscriber = cursor.fetchone()
            if not subscriber:
                print(f"Subscriber '{subscriber_name}' at '{subscriber_address}' not found.")
                return
            subscriber_id = subscriber[0]

            cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
            magazine = cursor.fetchone()
            if not magazine:
                print(f"Magazine '{magazine_name}' not found.")
                return
            magazine_id = magazine[0]

            cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
            if cursor.fetchone():
                print(f"Subscription already exists for '{subscriber_name}' to '{magazine_name}'.")
                return

            cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
                           (subscriber_id, magazine_id, expiration_date))
        except sqlite3.Error as e:
            print(f"Error inserting subscription: {e}")

    # Sample data
    add_publisher(cursor, "Tech Press")
    add_publisher(cursor, "Health Weekly")
    add_publisher(cursor, "Nature Publishing")

    add_magazine(cursor, "Tech Monthly", "Tech Press")
    add_magazine(cursor, "Healthy Living", "Health Weekly")
    add_magazine(cursor, "Nature World", "Nature Publishing")

    add_subscriber(cursor, "Alice Smith", "123 Main St")
    add_subscriber(cursor, "Bob Johnson", "456 Oak Ave")
    add_subscriber(cursor, "Alice Smith", "789 Pine Rd")

    add_subscription(cursor, "Alice Smith", "123 Main St", "Tech Monthly", "2025-12-31")
    add_subscription(cursor, "Bob Johnson", "456 Oak Ave", "Healthy Living", "2025-11-30")
    add_subscription(cursor, "Alice Smith", "789 Pine Rd", "Nature World", "2026-01-15")

    conn.commit()
    print("Data inserted successfully.")

    print("\nAll subscribers:")
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

    print("\nAll magazines sorted by name:")
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    for row in cursor.fetchall():
        print(row)

    print("\nMagazines published by 'Tech Press':")
    cursor.execute("""
        SELECT magazines.*
        FROM magazines
        JOIN publishers ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = ?
    """, ("Tech Press",))
    for row in cursor.fetchall():
        print(row)


except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        conn.close()
        print("Database connection closed.")
