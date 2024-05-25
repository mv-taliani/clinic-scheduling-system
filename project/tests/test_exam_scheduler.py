import unittest
from datetime import datetime, time
from uuid import uuid4

from project.exam_scheduler import ExamSchedulerClass
from project.exam_type_enum import ExamTypeEnum
from project.clinic import Clinic, Weekday
from project.employee import Employee

class TestExamScheduler(unittest.TestCase):

    def setUp(self):
        self.scheduler = ExamSchedulerClass()

        self.clinic_id = uuid4()
        self.clinic = Clinic(
            clinic_id=self.clinic_id,
            name="Healthy Life Clinic",
            operating_days=[Weekday.MONDAY, Weekday.TUESDAY, Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY],
            opening_time=time(8, 0),
            closing_time=time(17, 0),
            offered_exam_types=[ExamTypeEnum.GENERAL_CHECKUP, ExamTypeEnum.DENTAL_EXAM]
        )

        self.employee_id_1 = uuid4()
        self.employee_id_2 = uuid4()
        self.employee_1 = Employee(employee_id=self.employee_id_1, name="John Doe")
        self.employee_2 = Employee(employee_id=self.employee_id_2, name="Jane Smith")

    def test_successful_scheduling(self):
        result, message = self.scheduler.execute(self.employee_id_1, self.clinic, ExamTypeEnum.GENERAL_CHECKUP, datetime(2023, 10, 13, 14, 0))
        self.assertTrue(result)
        self.assertEqual(message, "Exam scheduled successfully for 2023-10-13 14:00:00.")

    def test_scheduling_outside_clinic_hours(self):
        result, message = self.scheduler.execute(self.employee_id_1, self.clinic, ExamTypeEnum.GENERAL_CHECKUP, datetime(2023, 10, 15, 6, 0))
        self.assertFalse(result)
        self.assertEqual(message, "Exam cannot be scheduled outside working hours.")

    def test_scheduling_with_time_conflicts(self):
        # Schedule the first appointment
        self.scheduler.execute(self.employee_id_1, self.clinic, ExamTypeEnum.GENERAL_CHECKUP, datetime(2023, 10, 13, 14, 0))
        # Attempt to schedule an overlapping appointment
        result, message = self.scheduler.execute(self.employee_id_1, self.clinic, ExamTypeEnum.GENERAL_CHECKUP, datetime(2023, 10, 13, 14, 30))
        self.assertFalse(result)
        self.assertEqual(message, "Exam cannot be scheduled due to a time conflict.")

    def test_invalid_exam_type_for_clinic(self):
        result, message = self.scheduler.execute(self.employee_id_1, self.clinic, ExamTypeEnum.DENTAL_EXAM, datetime(2023, 10, 13, 14, 0))
        self.assertTrue(result)

    def test_multiple_employees_scheduling(self):
        # Schedule an appointment for the first employee
        self.scheduler.execute(self.employee_id_1, self.clinic, ExamTypeEnum.GENERAL_CHECKUP, datetime(2023, 10, 13, 14, 0))
        # Schedule a non-conflicting appointment for the second employee
        result, message = self.scheduler.execute(self.employee_id_2, self.clinic, ExamTypeEnum.GENERAL_CHECKUP, datetime(2023, 10, 13, 15, 0))
        self.assertTrue(result)
        self.assertEqual(message, "Exam scheduled successfully for 2023-10-13 15:00:00.")

    def test_scheduling_on_weekend(self):
        result, message = self.scheduler.execute(self.employee_id_1, self.clinic, ExamTypeEnum.GENERAL_CHECKUP, datetime(2023, 10, 14, 14, 0))  # Saturday
        self.assertFalse(result)
        self.assertEqual(message, "Exam cannot be scheduled outside working hours.")

if __name__ == '__main__':
    unittest.main()
