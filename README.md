# Clinic Scheduling System

This project implements a scheduling system for clinics, where the clinic's operating hours and the types of exams offered do not depend on the employees. The system is designed to handle scheduling of appointments while avoiding time conflicts and ensuring the requested exam types are offered by the clinic.

## Project Structure

- `appointment.py`: Defines the `Appointment` class, which represents an appointment in the system.
- `clinic.py`: Defines the `Clinic` class, which represents a clinic and its properties.
- `employee.py`: Defines the `Employee` class, which represents an employee and their properties.
- `exam_scheduler.py`: Contains the `ExamSchedulerClass` which handles the scheduling logic.
- `exam_type_enum.py`: Defines the `ExamTypeEnum` enum for different types of exams.
- `weekday_enum.py`: Defines the `Weekday` enum for days of the week.
- `main.py`: Entry point for running the scheduling examples.
- `tests/test_exam_scheduler.py`: Contains unit tests for the `ExamSchedulerClass`.
- `tests/test_clinic.py`: Contains unit tests for the `Clinic` class.

## Main Functions and Classes

### `Appointment` Class
Defines an appointment with the following attributes:
- `appointment_id`: Unique identifier for the appointment.
- `employee_id`: Unique identifier for the employee handling the appointment.
- `clinic_id`: Unique identifier for the clinic where the appointment is scheduled.
- `exam_type`: Type of the exam.
- `start_time`: Start time of the appointment.
- `end_time`: End time of the appointment (automatically set to one hour after the start time).

### `Clinic` Class
Represents a clinic with the following attributes:
- `clinic_id`: Unique identifier for the clinic.
- `name`: Name of the clinic.
- `operating_days`: List of days the clinic operates.
- `opening_time`: Opening time of the clinic.
- `closing_time`: Closing time of the clinic.
- `offered_exam_types`: List of exam types offered by the clinic.

Includes methods:
- `is_within_operating_hours(start_time)`: Checks if a given time is within the clinic's operating hours.
- `is_exam_type_offered(exam_type)`: Checks if a given exam type is offered by the clinic.

### `Employee` Class
Represents an employee with the following attributes:
- `employee_id`: Unique identifier for the employee.
- `name`: Name of the employee.
- `working_days`: List of days the employee works.
- `opening_time`: Opening time of the employee's work hours.
- `closing_time`: Closing time of the employee's work hours.
- `exam_types`: List of exam types the employee can perform.

Includes methods:
- `can_perform_exam(exam_type)`: Checks if the employee can perform a given exam type.

### `ExamSchedulerClass`
Handles the scheduling of appointments with the following methods:
- `is_time_slot_available(employee_id, clinic_id, start_time)`: Checks if a time slot is available for scheduling.
- `execute(employee_id, clinic_id, exam_type, start_time)`: Schedules an appointment if all conditions are met (e.g., no conflicts, within operating hours).

## How to Run

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/clinic-scheduling-system.git
   cd clinic-scheduling-system

2. **Run the Scheduling Example:**
   ```sh
   python main.py

3. **Run unit tests:**
   ```sh
   python -m unittest discover
   
