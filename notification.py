from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'b.mugwadi1@alustudent.com'
app.config['MAIL_PASSWORD'] = 'beverlytashinga.15'

mail = Mail(app)

# Assuming you have a list of registered users with their emails
registered_users = ['user1@example.com', 'user2@example.com', 'user3@example.com']

@app.route('/send_notification')
def send_notification():
    for user_email in registered_users:
        msg = Message('Notification Subject', sender='your_email@example.com', recipients=[user_email])
        msg.body = 'Notification message goes here.'
        mail.send(msg)
    return 'Notification sent to all registered users.'

class HealthcareSystem:
    def __init__(self):
        self.patients = {}
        self.queue = []
        self.resources = {}

    def prompt_patient_registration(self):
        patient_name = input("Enter patient name: ")
        patient_id = input("Enter patient ID: ")
        patient_info = {"name": patient_name}
        self.register_and_check_in_patient(patient_id, patient_info)

    def register_and_check_in_patient(self, patient_id, patient_info):
        if patient_id in self.patients:
            print(f"Patient {patient_id} is already registered.")
        else:
            self.patients[patient_id] = patient_info
            print(f"Patient {patient_id} has been registered and checked in.")

    def book_appointment(self, patient_id, doctor_type="General"):
        if patient_id not in self.patients:
            print(f"Patient {patient_id} is not registered.")
        else:
            print(f"Appointment booked for patient {patient_id} with {doctor_type} Doctor.")

    def place_in_queue(self, patient_id):
        if patient_id not in self.patients:
            print(f"Patient {patient_id} is not registered.")
        elif patient_id in self.queue:
            print(f"Patient {patient_id} is already in the queue.")
        else:
            self.queue.append(patient_id)
            print(f"Patient {patient_id} has been placed in the queue.")

    def send_notification(self, patient_id):
        if patient_id in self.queue:
            queue_status = self.queue.index(patient_id) + 1
            print(f"Notification sent to patient {patient_id}. Queue status: {queue_status}")
        else:
            print(f"Patient {patient_id} is not in the queue.")

    def track_queue_and_allocate_resources(self):
        if not self.queue:
            print("The queue is empty.")
        else:
            for i, patient_id in enumerate(self.queue):
                self.resources[patient_id] = "Resource Allocated"
                print(f"Tracking Queue: Patient {patient_id} is number {i+1} in the queue.")

    def ask_payment_method(self, patient_id):
        payment_method = input(f"Enter payment method for patient {patient_id}: ")
        print(f"Payment method {payment_method} recorded for patient {patient_id}.")

if __name__ == '__main__':
    app.run(debug=True)
