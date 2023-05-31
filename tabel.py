cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password_hash VARCHAR(64) NOT NULL,
            salt VARCHAR(32) NOT NULL
        )
    """)

    conn.commit()
    print("Table created successfully.")
except mysql.connector.Error as error:
    print("Error creating table:", error)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()