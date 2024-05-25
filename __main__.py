from datetime import datetime, time
from uuid import uuid4

from project.exam_scheduler import ExamSchedulerClass
from project.exam_type_enum import ExamTypeEnum
from project.clinic import Clinic
from project.employee import Employee
from project.weekday_enum import Weekday

if __name__ == "__main__":
    scheduler = ExamSchedulerClass()

    # Example employees
    employee_id_1 = uuid4()
    employee_id_2 = uuid4()
    employee_1 = Employee(
        employee_id=employee_id_1,
        name="John Doe",
        working_days=[Weekday.MONDAY, Weekday.TUESDAY, Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY],  # Monday to Friday
        opening_time=time(8, 0),
        closing_time=time(17, 0),
        exam_types=[ExamTypeEnum.GENERAL_CHECKUP]
    )
    employee_2 = Employee(
        employee_id=employee_id_2,
        name="Jane Smith",
        working_days=[Weekday.MONDAY, Weekday.TUESDAY, Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY, Weekday.SATURDAY],  # Monday to Saturday
        opening_time=time(9, 0),
        closing_time=time(18, 0),
        exam_types=[ExamTypeEnum.GENERAL_CHECKUP, ExamTypeEnum.DENTAL_EXAM]
    )

    # Example clinic setup
    clinic_id = uuid4()
    clinic = Clinic(
        clinic_id=clinic_id,
        name="Healthy Life Clinic",
        employees=[employee_1, employee_2]
    )

    # Successful scheduling
    result, message = scheduler.execute(employee_id_1, clinic, ExamTypeEnum.GENERAL_CHECKUP, datetime(2023, 10, 13, 14, 0))  # Friday
    print(message)  # Expected output: "Exam scheduled successfully for 2023-10-13 14:00:00."

    # Scheduling outside clinic hours
    result, message = scheduler.execute(employee_id_1, clinic, ExamTypeEnum.GENERAL_CHECKUP, datetime(2023, 10, 15, 6, 0))  # Sunday
    print(message)  # Expected output: "Exam cannot be scheduled outside working hours."

    # Scheduling with time conflicts
    result, message = scheduler.execute(employee_id_1, clinic, ExamTypeEnum.GENERAL_CHECKUP, datetime(2023, 10, 13, 14, 30))  # Friday, overlapping
    print(message)  # Expected output: "Exam cannot be scheduled due to a time conflict."

    # Scheduling with an employee not working in the clinic
    result, message = scheduler.execute(uuid4(), clinic, ExamTypeEnum.GENERAL_CHECKUP, datetime(2023, 10, 13, 14, 0))
    print(message)  # Expected output: "The employee does not work in this clinic."

    # Scheduling with an employee not qualified for the exam type
    result, message = scheduler.execute(employee_id_1, clinic, ExamTypeEnum.DENTAL_EXAM, datetime(2023, 10, 13, 14, 0))
    print(message)  # Expected output: "The employee cannot perform the required exam type."
