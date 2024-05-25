from dataclasses import dataclass, field
from datetime import datetime, timedelta
from uuid import uuid4, UUID

from project.exam_type_enum import ExamTypeEnum

@dataclass
class Appointment:
    employee_id: UUID
    clinic_id: UUID
    exam_type: ExamTypeEnum
    start_time: datetime
    end_time: datetime = field(init=False)
    appointment_id: UUID = field(default_factory=uuid4)


    def __post_init__(self):
        self.end_time = self.start_time + timedelta(hours=1)
