from datetime import datetime, timedelta
from project.appointment import Appointment
from project.clinic import Clinic
from uuid import UUID

from project.exam_type_enum import ExamTypeEnum

class ExamSchedulerClass:
    def __init__(self):
        self.appointments = []  # Replace with a proper database query

    def is_time_slot_available(self, employee_id: UUID, clinic_id: UUID, start_time: datetime) -> bool:
        end_time = start_time + timedelta(hours=1)
        for appointment in self.appointments:
            if appointment.employee_id == employee_id and appointment.clinic_id == clinic_id:
                if not (end_time <= appointment.start_time or start_time >= appointment.end_time):
                    return False
        return True

    def execute(self, employee_id: UUID, clinic: Clinic, exam_type: ExamTypeEnum, start_time: datetime):
        # Check if the employee works in the clinic
        employee = clinic.get_employee(employee_id)
        if not employee:
            return False, "The employee does not work in this clinic."

        # Check if the employee can perform the required exam type
        if not employee.can_perform_exam(exam_type):
            return False, "The employee cannot perform the required exam type."

        # Check if the appointment is within the clinic's operating hours
        if not clinic.is_within_operating_hours(employee_id, start_time):
            return False, "Exam cannot be scheduled outside working hours."

        # Check if the time slot is available
        if not self.is_time_slot_available(employee_id, clinic.clinic_id, start_time):
            return False, "Exam cannot be scheduled due to a time conflict."

        # Schedule the appointment
        new_appointment = Appointment(employee_id=employee_id, clinic_id=clinic.clinic_id, exam_type=exam_type.value, start_time=start_time)
        self.appointments.append(new_appointment)
        return True, f"Exam scheduled successfully for {start_time}."
