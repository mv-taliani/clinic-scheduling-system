import unittest
from datetime import datetime, time
from uuid import uuid4

from project.clinic import Clinic, Weekday
from project.exam_type_enum import ExamTypeEnum

class TestClinic(unittest.TestCase):

    def setUp(self):
        self.clinic_id = uuid4()
        self.clinic = Clinic(
            clinic_id=self.clinic_id,
            name="Healthy Life Clinic",
            operating_days=[Weekday.MONDAY, Weekday.TUESDAY, Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY],
            opening_time=time(8, 0),
            closing_time=time(17, 0),
            offered_exam_types=[ExamTypeEnum.GENERAL_CHECKUP, ExamTypeEnum.DENTAL_EXAM]
        )

    def test_is_within_operating_hours(self):
        # Test a valid time within operating hours
        self.assertTrue(self.clinic.is_within_operating_hours(datetime(2023, 10, 13, 14, 0)))
        # Test a time outside operating hours (early morning)
        self.assertFalse(self.clinic.is_within_operating_hours(datetime(2023, 10, 13, 6, 0)))
        # Test a time outside operating hours (late evening)
        self.assertFalse(self.clinic.is_within_operating_hours(datetime(2023, 10, 13, 18, 0)))
        # Test a time on a weekend
        self.assertFalse(self.clinic.is_within_operating_hours(datetime(2023, 10, 14, 14, 0)))  # Saturday

    def test_is_exam_type_offered(self):
        self.assertTrue(self.clinic.is_exam_type_offered(ExamTypeEnum.GENERAL_CHECKUP))
        self.assertTrue(self.clinic.is_exam_type_offered(ExamTypeEnum.DENTAL_EXAM))
        self.assertFalse(self.clinic.is_exam_type_offered(ExamTypeEnum.VISION_TEST))

if __name__ == '__main__':
    unittest.main()
