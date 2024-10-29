from datetime import datetime

# Клас для користувача (User)
class User:
    def __init__(self, user_id, first_name, last_name, role, birthday):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role.lower()
        self.birthday = birthday

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_user_info(self):
        return f"ID: {self.user_id}, Користувач: {self.full_name}, Роль: {self.role}"

# Клас для лікаря (Doctor)
class Doctor(User):
    def __init__(self, user_id, first_name, last_name, birthday, profession, years_work):
        super().__init__(user_id, first_name, last_name, "doctor", birthday)
        self.profession = profession
        self.years_work = years_work

    def get_doctor_info(self):
        return f"Лікар - {self.full_name}\nПрофесія - {self.profession}\nДосвід роботи - {self.years_work} років"

# Клас для пацієнта (Patient)
class Patient(User):
    def __init__(self, user_id, first_name, last_name, blood_type, birthday):
        super().__init__(user_id, first_name, last_name, "patient", birthday)
        self.blood_type = blood_type

    def get_patient_info(self):
        return f"Пацієнт {self.full_name} має тип крові {self.blood_type}."

# Клас для прийому (Appointment)
class Appointment:
    # Зберігаємо всі прийоми у списку
    all_appointments = []

    def __init__(self, appointment_id, doctor, patient, room, appointment_date):
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.patient = patient
        self.room = room
        self.appointment_date = appointment_date
        self.creation_date = datetime.now()
        Appointment.all_appointments.append(self)

    def get_appointment_info(self):
        return (f"ID прийома: {self.appointment_id}\n"
                f"Лікар: {self.doctor.full_name} ({self.doctor.profession})\n"
                f"Пацієнт: {self.patient.full_name}\n"
                f"Кімната: {self.room}\n"
                f"Дата прийому: {self.appointment_date}\n"
                f"Дата створення: {self.creation_date}")

    @classmethod
    def schedule_appointment(cls, doctor, patient, room, appointment_date):
        appointment_id = len(cls.all_appointments) + 1
        new_appointment = cls(appointment_id, doctor, patient, room, appointment_date)
        print("Прийом створений успішно")
        return new_appointment

    @classmethod
    def get_all_appointments(cls):
        return [appo.get_appointment_info() for appo in cls.all_appointments]

    @classmethod
    def get_appointments_by_patient(cls, patient):
        return [appo.get_appointment_info() for appo in cls.all_appointments if appo.patient == patient]

    @classmethod
    def get_appointments_by_doctor(cls, doctor):
        return [appo.get_appointment_info() for appo in cls.all_appointments if appo.doctor == doctor]

# Функція для створення користувача з роллю лікаря або пацієнта
def create_user(user_id, first_name, last_name, role, birthday, **kwargs):
    if role.lower() == "doctor":
        return Doctor(user_id, first_name, last_name, birthday, kwargs['profession'], kwargs['years_work'])
    elif role.lower() == "patient":
        return Patient(user_id, first_name, last_name, kwargs['blood_type'], birthday)

# Приклад використання
doctor1 = create_user(1, "Джон", "Сміт",
                      "doctor", "2000-6-12", profession="Психолог", years_work=5)
patient1 = create_user(2, "Іван", "Іванович",
                       "patient", "2003-03-08", blood_type="B")
patient2 = create_user(3, "Андрій", "Цинцар",
                       "patient", "2004-11-19", blood_type="A+")
doctor2 = create_user(4, "Олена", "Шевчук",
                      "doctor", "2000-07-01", profession="Терапевт", years_work=2)

# Записуємо пацієнта на прийом

print(doctor1.get_doctor_info())
room1 = "Кімната 101"
appointment_date1 = "2025-06-04 11:00"
appointment1 = Appointment.schedule_appointment(doctor1, patient1, room1, appointment_date1)

room2 = "Кімната 102"
appointment_date2 = "2022-04-20 17:00"
appointment2 = Appointment.schedule_appointment(doctor1, patient2, room2, appointment_date2)
print("\n")
# Виведемо інформацію про записи
print(appointment1.get_appointment_info())
print(appointment2.get_appointment_info())

# Виводимо всі записи для певного пацієнта
print("\nВсі записи на прийом до лікарів в пацієнта:")
appointments_for_patient = Appointment.get_appointments_by_patient(patient1)
for appo_info in appointments_for_patient:
    print(appo_info)

# Виводимо всі записи для певного лікаря
print("\nВсі записи на прийом пацієнтів в лікаря:")
appointments_for_doctor = Appointment.get_appointments_by_doctor(doctor1)
for appo_info in appointments_for_doctor:
    print(appo_info)
