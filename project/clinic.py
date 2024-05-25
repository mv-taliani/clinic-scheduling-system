from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import UUID

from project.employee import Employee

@dataclass
class Clinic:
    clinic_id: UUID
    name: str
    employees: list[Employee] = None

    def is_within_operating_hours(self, employee_id: UUID, start_time: datetime) -> bool:
        employee = self.get_employee(employee_id)
        if not employee:
            return False
        exam_end_time = start_time + timedelta(hours=1)
        return (start_time.weekday() in [day.value for day in employee.working_days] and 
                employee.opening_time <= start_time.time() < employee.closing_time and 
                exam_end_time.time() <= employee.closing_time)

    def is_exam_type_offered(self, employee_id: UUID, exam_type: str) -> bool:
        employee = self.get_employee(employee_id)
        if not employee:
            return False
        return exam_type in employee.exam_types

    def get_employee(self, employee_id: UUID) -> Employee:
        return next((emp for emp in self.employees if emp.employee_id == employee_id), None)
