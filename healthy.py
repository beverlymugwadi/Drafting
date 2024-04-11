import mysql.connector
from datetime import datetime

class HealthcareSystem:
    def _init_(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="beverlymugwadi",
            password="tashinga",
            database="health_db"
        )
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                patient_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                gender ENUM('Male', 'Female', 'Other')
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                appointment_id INT AUTO_INCREMENT PRIMARY KEY,
                patient_id INT,
                doctor_name VARCHAR(255),
                appointment_date DATE,
                appointment_type VARCHAR(50),
                payment_method VARCHAR(50),
                FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
            )
        """)
        self.conn.commit()

    def prompt_patient_registration(self):
        patient_name = input("Enter patient name: ")
        gender = input("Enter patient gender (Male/Female/Other): ").capitalize()
        self.register_patient(patient_name, gender)

    def register_patient(self, name, gender):
        try:
            sql = "INSERT INTO patients (name, gender) VALUES (%s, %s)"
            val = (name, gender)
            self.cursor.execute(sql, val)
            self.conn.commit()
            print("Patient registered successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def book_appointment(self, patient_id, doctor_name, appointment_type):
        try:
            appointment_date = input("Enter appointment date (YYYY-MM-DD): ")
            payment_method = input("Enter payment method: ")
            sql = "INSERT INTO appointments (patient_id, doctor_name, appointment_date, appointment_type, payment_method) VALUES (%s, %s, %s, %s, %s)"
            val = (patient_id, doctor_name, appointment_date, appointment_type, payment_method)
            self.cursor.execute(sql, val)
            self.conn.commit()
            print("Appointment booked successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

# Create an instance of the HealthcareSystem class
healthcare_system = HealthcareSystem()

# Prompt patient registration
healthcare_system.prompt_patient_registration()

# Book an appointment
patient_id = int(input("Enter patient ID: "))  # Assuming patient ID is already available
doctor_name = input("Enter doctor's name: ")
appointment_type = input("Enter appointment type: ")
healthcare_system.book_appointment(patient_id, doctor_name, appointment_type)
