import mysql.connector as c

# Connect to the database
mydb = c.connect(
    host='localhost',
    user="root",
    password="1234",
    database="cvr"
)

# Main operation loop
while True:
    choice = input("Choose any operation\n1. Insert\n2. Update\n3. Delete\n4. Select\n5. Exit\n")

    if choice == "1":
        try:
            mycursor = mydb.cursor()
            name = input("Enter your name: ")
            roll = input("Enter your rollno: ")
            mycursor.execute("INSERT INTO students (sid, sname) VALUES (%s, %s)", (roll, name))
            mydb.commit()
            print("Record inserted successfully.")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "2":
        try:
            mycursor = mydb.cursor()
            name = input("Enter the new name: ")
            roll = input("Enter the roll number of the student to update: ")
            mycursor.execute("UPDATE students SET sname = %s WHERE sid = %s", (name, roll))
            mydb.commit()
            print("Record updated successfully.")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "3":
        # Delete operation
        try:
            mycursor = mydb.cursor()
            roll = input("Enter the roll number of the student to delete: ")
            mycursor.execute("DELETE FROM students WHERE sid = %s", (roll,))
            mydb.commit()
            print("Record deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "4":
        # Select operation
        try:
            mycursor = mydb.cursor()
            name = input("Enter name to search: ")
            mycursor.execute("SELECT * FROM students WHERE sname = %s", (name,))
            students = mycursor.fetchall()
            if students:
                for std in students:
                    print(std)
            else:
                print("No students found with that name.")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "5":
        # Exit
        print("Exiting program.")
        mydb.close()
        break

    else:
        print("Invalid choice. Please try again.")
