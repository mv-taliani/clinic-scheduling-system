from dataclasses import dataclass
from uuid import UUID

@dataclass
class Employee:
    employee_id: UUID
    name: str
