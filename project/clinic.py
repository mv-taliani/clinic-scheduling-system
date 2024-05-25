from dataclasses import dataclass
from datetime import datetime, time, timedelta
from uuid import UUID
from enum import Enum

from project.exam_type_enum import ExamTypeEnum

class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

@dataclass
class Clinic:
    clinic_id: UUID
    name: str
    operating_days: list[Weekday]
    opening_time: time
    closing_time: time
    offered_exam_types: list[ExamTypeEnum]

    def is_within_operating_hours(self, start_time: datetime) -> bool:
        exam_end_time = start_time + timedelta(hours=1)
        return (start_time.weekday() in [day.value for day in self.operating_days] and 
                self.opening_time <= start_time.time() < self.closing_time and 
                exam_end_time.time() <= self.closing_time)

    def is_exam_type_offered(self, exam_type: ExamTypeEnum) -> bool:
        return exam_type in self.offered_exam_types
