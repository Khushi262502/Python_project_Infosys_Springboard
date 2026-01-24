from fastapi import APIRouter
from mysql.connector import Error
from backend.confg.sql_config import database_connection

router = APIRouter()


#  CREATE USER
@router.post("/create/user")
def create_user(name: str, email: str, password: str):
    try:
        db = database_connection()
        cursor = db.cursor(dictionary=True)

        query = "INSERT INTO tbluser (name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, password))
        db.commit()

        return {"message": "User created successfully"}

    except Error as e:
        return {"error": str(e)}

    finally:
        try:
            cursor.close()
            db.close()
        except:
            pass


#  GET USER BY ID
@router.get("/get/user/{user_id}")
def get_user(user_id: int):
    try:
        db = database_connection()
        cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM tbluser WHERE id = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()

        if not user:
            return {"message": "User not found"}

        return user

    except Error as e:
        return {"error": str(e)}

    finally:
        try:
            cursor.close()
            db.close()
        except:
            pass


# GET ALL USERS
@router.get("/get/users")
def get_all_users():
    try:
        db = database_connection()
        cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM tbluser"
        cursor.execute(query)
        users = cursor.fetchall()

        return users

    except Error as e:
        return {"error": str(e)}

    finally:
        try:
            cursor.close()
            db.close()
        except:
            pass


# UPDATE USER (dynamic like screenshot)
@router.put("/update/user")
def update_user(user_id: int, name: str = None, email: str = None, password: str = None):
    try:
        db = database_connection()
        cursor = db.cursor(dictionary=True)

        fields = []
        values = []

        if name:
            fields.append("name = %s")
            values.append(name)

        if email:
            fields.append("email = %s")
            values.append(email)

        if password:
            fields.append("password = %s")
            values.append(password)

        if not fields:
            return {"message": "No fields provided to update"}

        values.append(user_id)

        query = f"UPDATE tbluser SET {', '.join(fields)} WHERE id = %s"
        cursor.execute(query, tuple(values))
        db.commit()

        return {"message": "User updated successfully"}

    except Error as e:
        return {"error": str(e)}

    finally:
        try:
            cursor.close()
            db.close()
        except:
            pass


#  DELETE USER
@router.delete("/delete/user/{user_id}")
def delete_user(user_id: int):
    try:
        db = database_connection()
        cursor = db.cursor(dictionary=True)

        query = "DELETE FROM tbluser WHERE id = %s"
        cursor.execute(query, (user_id,))
        db.commit()

        return {"message": "User deleted successfully"}

    except Error as e:
        return {"error": str(e)}

    finally:
        try:
            cursor.close()
            db.close()
        except:
            pass
