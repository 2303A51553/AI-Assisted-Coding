#Create a Python class Patient using constructor.
#Store patient ID, name, age, doctor name, diagnosis, and medicines.
class Patient:
    def __init__(self, patient_id, name, age, doctor_name, diagnosis, medicines):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.doctor_name = doctor_name
        self.diagnosis = diagnosis
        self.medicines = medicines  
#In this code, we define a class called Patient with a constructor (__init__ method) that takes six parameters: patient_id, name, age, doctor_name, diagnosis, and medicines.
#The constructor initializes the instance variables with the values passed as arguments when creating an instance of the
#Patient class. This allows us to create patient objects with specific information about each patient.
# Write a function to take patient details from user and create a Patient object.
def create_patient():
    patient_id = input("Enter patient ID: ")
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    doctor_name = input("Enter doctor name: ")
    diagnosis = input("Enter diagnosis: ")
    medicines = input("Enter medicines (comma-separated): ").split(",")
    return Patient(patient_id, name, age, doctor_name, diagnosis, medicines)
#In this function, we prompt the user to enter the details of a patient, such as patient ID, name, age, doctor name, diagnosis, and medicines.
#We use the input() function to get the user input and convert the age to an integer
#Store patient details permanently in a text file using file handling.
def save_patient_to_file(patient):
    with open("patients.txt", "a") as file:
        file.write(f"Patient ID: {patient.patient_id}\n")
        file.write(f"Name: {patient.name}\n")
        file.write(f"Age: {patient.age}\n")
        file.write(f"Doctor Name: {patient.doctor_name}\n")
        file.write(f"Diagnosis: {patient.diagnosis}\n")
        file.write(f"Medicines: {', '.join(patient.medicines)}\n")
        file.write("\n")  # Add a newline for separation between patients
#In this function, we open a file called "patients.txt" in append mode ("a") to add new patient details without overwriting existing data.
#Write code to read all patient records from file and display them.
def read_patients_from_file():
    try:
        with open("patients.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("No patient records found.")
            else:
                print(content)
    except FileNotFoundError:
        print("No patient records found.")
#In this function, we attempt to open the "patients.txt" file in read mode ("r"). If the file does not exist, a FileNotFoundError is caught, and a message is printed indicating that no patient records are found.
#Write code to search a patient record by patient ID from file.
def search_patient_by_id(patient_id):
    try:
        with open("patients.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 7):  # Each patient record consists of 7 lines (including the newline)
                if lines[i].strip() == f"Patient ID: {patient_id}":
                    print("".join(lines[i:i+6]))  # Print the patient record
                    return
            print("Patient not found.")
    except FileNotFoundError:
        print("No patient records found.")
#In this function, we read the "patients.txt" file line by line and check for a matching patient ID. If a match is found, the corresponding patient record is printed. If no match is found after checking all records, a message is printed indicating that the patient was not found. If the file does not exist, a FileNotFoundError is caught, and a message is printed indicating that no patient records are found.
#Write code to update diagnosis or medicines of a patient using patient ID.
def update_patient_by_id(patient_id, new_diagnosis=None, new_medicines=None):
    try:
        with open("patients.txt", "r") as file:
            lines = file.readlines()
        updated_lines = []
        i = 0
        while i < len(lines):
            if lines[i].strip() == f"Patient ID: {patient_id}":
                updated_lines.append(lines[i])  # Keep the patient ID line
                updated_lines.append(f"Name: {lines[i+1].split(': ')[1].strip()}\n")  # Keep the name line
                updated_lines.append(f"Age: {lines[i+2].split(': ')[1].strip()}\n")  # Keep the age line
                updated_lines.append(f"Doctor Name: {lines[i+3].split(': ')[1].strip()}\n")  # Keep the doctor name line
                if new_diagnosis is not None:
                    updated_lines.append(f"Diagnosis: {new_diagnosis}\n")
                else:
                    updated_lines.append(lines[i+4])  # Keep existing diagnosis line if not updating
                if new_medicines is not None:
                    updated_lines.append(f"Medicines: {', '.join(new_medicines)}\n")
                else:
                    updated_lines.append(lines[i+5])  # Keep existing medicines line if not updating
                i += 6  # Move to next patient record (skip current patient record lines)
            else:
                updated_lines.append(lines[i])
                i += 1
        with open("patients.txt", "w") as file:
            file.writelines(updated_lines)
    except FileNotFoundError:
        print("No patient records found.")
#In this function, we read the "patients.txt" file and look for the patient record with the specified patient ID. If found, we update the diagnosis and/or medicines as provided in the function arguments. We then write the updated list of lines back to the file, effectively updating the patient record. If the file does not exist, a FileNotFoundError is caught, and a message is printed indicating that no patient records are found.
#Calculate total number of patients visited in a day.
def count_total_patients():
    try:
        with open("patients.txt", "r") as file:
            lines = file.readlines()
            patient_count = len(lines) // 7  # Each patient record consists of 7 lines (including the newline)
            print(f"Total number of patients visited: {patient_count}")
    except FileNotFoundError:
        print("No patient records found.")
#In this function, we read the "patients.txt" file and count the total number of patient records by dividing the total number of lines by 7 (since each patient record consists of 7 lines, including the newline). If the file does not exist, a FileNotFoundError is caught, and a message is printed indicating that no patient records are found.
#Find and display the doctor who is consulted most frequently.
def find_most_frequent_doctor():
    try:
        with open("patients.txt", "r") as file:
            lines = file.readlines()
            doctor_count = {}
            for i in range(0, len(lines), 7):  # Each patient record consists of 7 lines (including the newline)
                doctor_name = lines[i+3].split(': ')[1].strip()  # Extract doctor name
                if doctor_name in doctor_count:
                    doctor_count[doctor_name] += 1
                else:
                    doctor_count[doctor_name] = 1
            if doctor_count:
                most_frequent_doctor = max(doctor_count, key=doctor_count.get)
                print(f"The most frequently consulted doctor is: {most_frequent_doctor} with {doctor_count[most_frequent_doctor]} consultations.")
            else:
                print("No patient records found.")
    except FileNotFoundError:
        print("No patient records found.")
#In this function, we read the "patients.txt" file and count the number of consultations for each doctor by iterating through the patient records. We use a dictionary to keep track of the count for each doctor. After counting, we find the doctor with the maximum consultations and print their name along with the count. If there are no patient records or if the file does not exist, appropriate messages are printed.
#List all patients whose age is above 60 for priority care.
def list_patients_above_age(age_threshold=60):
    try:
        with open("patients.txt", "r") as file:
            lines = file.readlines()
            print(f"Patients above age {age_threshold}:")
            for i in range(0, len(lines), 7):  # Each patient record consists of 7 lines (including the newline)
                age = int(lines[i+2].split(': ')[1].strip())  # Extract age
                if age > age_threshold:
                    print("".join(lines[i:i+6]))  # Print the patient record
    except FileNotFoundError:
        print("No patient records found.")
#In this function, we read the "patients.txt" file and check the age of each patient. If a patient's age is above the specified age threshold (default is 60), their record is printed. If there are no patient records or if the file does not exist, appropriate messages are printed.
#Create a menu-driven program using loop.Allow user to repeat operations until exit is chosen.
def main():
    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Update Patient")
        print("3. Delete Patient")
        print("4. Count Total Patients")
        print("5. Find Most Frequent Doctor")
        print("6. List Patients Above Age 60")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_patient()
        elif choice == "2":
            update_patient()
        elif choice == "3":
            delete_patient()
        elif choice == "4":
            count_total_patients()
        elif choice == "5":
            find_most_frequent_doctor()
        elif choice == "6":
            list_patients_above_age()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")
#In this main function, we create a menu-driven program that allows the user to perform various operations related to patient management. The user can choose to add a patient, update a patient, delete a patient, count total patients, find the most frequent doctor, list patients above age 60, or exit the program. The loop continues until the user chooses to exit. Each choice corresponds to a specific function that performs the desired operation.
#Combine all functions into a complete Patient Appointment and Prescription Record System.
def add_patient():
    patient = create_patient()
    save_patient_to_file(patient)
    print("Patient added successfully.")
def update_patient():
    patient_id = input("Enter patient ID to update: ")
    new_diagnosis = input("Enter new diagnosis (leave blank to keep current): ")
    new_medicines_input = input("Enter new medicines (comma-separated, leave blank to keep current): ")
    new_medicines = new_medicines_input.split(",") if new_medicines_input else None
    update_patient_by_id(patient_id, new_diagnosis if new_diagnosis else None, new_medicines)
    print("Patient updated successfully.")
def delete_patient():
    patient_id = input("Enter patient ID to delete: ")
    try:
        with open("patients.txt", "r") as file:
            lines = file.readlines()
        updated_lines = []
        i = 0
        while i < len(lines):
            if lines[i].strip() == f"Patient ID: {patient_id}":
                i += 7  # Skip the current patient record (7 lines)
            else:
                updated_lines.append(lines[i])
                i += 1
        with open("patients.txt", "w") as file:
            file.writelines(updated_lines)
        print("Patient deleted successfully.")
    except FileNotFoundError:
        print("No patient records found.")
if __name__ == "__main__":
    main()
#In this complete code, we have defined all the necessary functions for managing patient records, including adding, updating, deleting patients, counting total patients, finding the most frequent doctor, and listing patients above a certain age. The main function provides a menu-driven interface for the user to interact with the system. Each operation is handled by its respective function, and the program continues to run until the user chooses to exit.
