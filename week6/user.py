from database import connect_db
import mysql.connector

def create_user(name, username, password):
    conn = connect_db()
    try:
        with conn.cursor() as cur:
            query = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
            values = (name, username, password)
            cur.execute(query, values)
            conn.commit()  # Commit changes to the database
            
            user_obj = {
                "name": name,
                "username": username,
                "password": password,
            }
            return user_obj  # Moved inside try to ensure it only executes if no exception occurs

    except mysql.connector.Error as e:
        print(f"Error creating user: {e}")
        return None  # Or handle the error as appropriate

    finally:
        conn.close()

def get_user(username):
    conn = connect_db()
    try:
        with conn.cursor() as cur:
            query = "SELECT * FROM member WHERE name = %s"
            cur.execute(query, (username,))
            user = cur.fetchall() 
    except mysql.connector.Error as e:
        print(f"Error fetching user: {e}")
        user = None  
    finally:
        conn.close()  

    return user


def login_user(username, password):
    conn = connect_db()
    try:
        with conn.cursor(dictionary=True) as cur:
            # Query to retrieve the password from the database
            query = "SELECT password, name FROM member WHERE username = %s"
            cur.execute(query, (username,))
            result = cur.fetchone()  # Fetch the single result row
            name = ""
            if result:
                stored_password = result['password']
                name = result['name']
                if password == stored_password:
                    return name, True  # Successful login if the passwords match
                else:
                    print("Password does not match")
                    return "",False  # Password does not match
            else:
                print("Username not found")
                return "",False  # Username not found in the database

    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return False  # Return False on exception

    finally:
        conn.close()
        

def logout_user():
    pass

def create_msg(username, message):
    conn = connect_db()
    if conn is None:
        print("Failed to connect to the database.")
        return False
    try:
        with conn.cursor() as cur:
            # Get the user ID based on the username
            query_user_id = "SELECT id FROM member WHERE username = %s"
            cur.execute(query_user_id, (username,))
            user_id_result = cur.fetchone()
            
            if user_id_result:
                user_id = user_id_result[0]
                # Insert the new message into the message table
                query_insert_message = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
                cur.execute(query_insert_message, (user_id, message))
                conn.commit()
                print("Message inserted successfully.")
                return True
            else:
                print("No user found with that username.")
                return False
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
        return False
    finally:
        conn.close()

    

def get_msg():
    """ Fetch messages and their respective member names from the database. """
    conn = connect_db()
    if conn is None:
        return []

    try:
        with conn.cursor() as cur:
            query = """
            SELECT 
                mem.name, 
                m.content
            FROM 
                message m
            JOIN 
                member mem ON m.member_id = mem.id
            ORDER BY 
                m.time DESC;
            """
            cur.execute(query)
            results = cur.fetchall()  # Retrieve all rows as a list of tuples
            return results
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
        return []
    finally:
        conn.close()