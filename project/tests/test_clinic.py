import unittest
from datetime import datetime, time
from uuid import uuid4
from project.clinic import Clinic
from project.employee import Employee
from project.exam_type_enum import ExamTypeEnum
from project.weekday_enum import Weekday

class TestClinic(unittest.TestCase):

    def setUp(self):
        self.employee_id = uuid4()
        self.employee = Employee(
            employee_id=self.employee_id,
            name="John Doe",
            working_days=[Weekday.MONDAY, Weekday.TUESDAY, Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY],  # Monday to Friday
            opening_time=time(8, 0),
            closing_time=time(17, 0),
            exam_types=[ExamTypeEnum.GENERAL_CHECKUP]
        )

        self.clinic_id = uuid4()
        self.clinic = Clinic(
            clinic_id=self.clinic_id,
            name="Healthy Life Clinic",
            employees=[self.employee]
        )

    def test_is_within_operating_hours(self):
        # Test a valid time within operating hours
        self.assertTrue(self.clinic.is_within_operating_hours(self.employee_id, datetime(2023, 10, 13, 14, 0)))
        # Test a time outside operating hours (early morning)
        self.assertFalse(self.clinic.is_within_operating_hours(self.employee_id, datetime(2023, 10, 13, 6, 0)))
        # Test a time outside operating hours (late evening)
        self.assertFalse(self.clinic.is_within_operating_hours(self.employee_id, datetime(2023, 10, 13, 18, 0)))
        # Test a time on a weekend
        self.assertFalse(self.clinic.is_within_operating_hours(self.employee_id, datetime(2023, 10, 14, 14, 0)))  # Saturday

    def test_is_exam_type_offered(self):
        self.assertTrue(self.clinic.is_exam_type_offered(self.employee_id, ExamTypeEnum.GENERAL_CHECKUP))
        self.assertFalse(self.clinic.is_exam_type_offered(self.employee_id, ExamTypeEnum.VISION_TEST))

if __name__ == '__main__':
    unittest.main()
