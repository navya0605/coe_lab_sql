import mysql.connector as c

# Connect to the database
mydb = c.connect(
    host='localhost',
    user="root",
    password="1234",
    database="cvr"
)
mycursor = mydb.cursor()

# Insert a new patient
name = input("Enter the name of the new patient: ")
id = input("Enter the ID of the new patient: ")
dis = input("Enter the disease: ")
wek = input("How many weeks have you been suffering from this disease? ")
doc = input("Enter the name of your current doctor: ")
ph = input("Enter your phone number: ")

# Insert into database
mycursor.execute("INSERT INTO patients (patient_id, patient_name, doctor_referred, disease, suffering_weeks, phone_number) VALUES (%s, %s, %s, %s, %s, %s)", (id, name, doc, dis, wek, ph))

# Update the disease information for a patient
diss = input("Enter the new disease for the patient: ")
no = input("Enter the patient ID to update: ")
mycursor.execute("UPDATE patients SET disease = %s WHERE patient_id = %s", (diss, no))

# Delete patients who have been suffering for less than 4 weeks
mycursor.execute("DELETE FROM patients WHERE suffering_weeks < 4")

# Select and display patients who have been suffering for more than 5 weeks
mycursor.execute("SELECT * FROM patients WHERE suffering_weeks > 5")
patients = mycursor.fetchall()

# Print the selected patients' details
for pat in patients:
    print(pat)

# Commit the changes
mydb.commit()
