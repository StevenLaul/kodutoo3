import mysql.connector # Impordin MySQLi Connectori
import bcrypt # Impordin bcrypti

conn = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    database="sql7620863",
    user="sql7620863",
    password='9T7P1uHFr6'
)
cursor = conn.cursor()  # Tekitan kursoriobjekti SQL-päringute jaoks

def login_user():
    query = "SELECT password_hash, salt FROM users WHERE username = %s"
    params = (username,)

    cursor.execute(query, params)
    result = cursor.fetchone()

    if result is None:
        print("User is not registered.")
    else:
        password_hash, salt = result

        input_password_hash = hashlib.sha256((password + salt).encode()).hexdigest()

        if input_password_hash == password_hash:
            print("Login successful.")
        else:
            print("Wrong login.")

    conn.close()

username = input("Enter username: ")
password = input("Enter password: ")

login_user()