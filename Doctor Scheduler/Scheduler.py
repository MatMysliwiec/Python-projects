class Patient:
    def __init__(self, name, appointment_time):
        self.name = name
        self.appointment_time = appointment_time


class Doctor:
    def __init__(self, name, work_time=(8, 16)):
        self.name = name
        self.patients = []
        self.work_time = [i for i in range(work_time)]

    def add_patient(self, patient):
        if len(self.patients) < 16:

                self.patients.append(patient)
                print(f"{patient.name}'s appointment scheduled with Dr.{self.name} at {patient.appointment_time}")
        else:
            print(f"Sorry, Dr.{self.name} is fully booked for today.")


class Scheduler:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_patient(self, patient):
        scheduled = False
        for doctor in self.doctors:
            if len(doctor.patients) < 16:
                doctor.add_patient(patient)
                scheduled = True
                break
        if not scheduled:
            print(f"All doctors are fully bocked for today")


if __name__ == "__main__":
    scheduler = Scheduler()

    doctor1 = Doctor("John Brasko")
    doctor2 = Doctor("Jane Halla")
    scheduler.add_doctor(doctor1)
    scheduler.add_doctor(doctor2)

    patient1 = Patient("Alice", "9:00 AM")
    patient2 = Patient("Bob", "10:00 AM")
    patient3 = Patient("Charlie", "11:00 AM")
    patient4 = Patient("David", "12:00 PM")

    scheduler.schedule_patient(patient1)
    scheduler.schedule_patient(patient2)
    scheduler.schedule_patient(patient3)
    scheduler.schedule_patient(patient4)
