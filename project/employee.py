from dataclasses import dataclass
from datetime import time
from uuid import UUID
from project.exam_type_enum import ExamTypeEnum

from project.weekday_enum import Weekday

@dataclass
class Employee:
    employee_id: UUID
    name: str
    working_days: list[Weekday]  # List of weekdays the employee works
    opening_time: time
    closing_time: time
    exam_types: list[ExamTypeEnum]

    def can_perform_exam(self, exam_type: ExamTypeEnum) -> bool:
        return exam_type in self.exam_types
