

Healthcare Appointment Booking Automation

Project Overview:
This project automates the healthcare appointment booking process using Selenium, Python, and the Page Object Model (POM) design pattern. The aim is to ensure smooth and accurate testing of critical functionalities like user registration, appointment scheduling, and booking confirmation. By automating these tasks, the project reduces manual testing efforts, improves accuracy, and accelerates testing cycles, making it easier to validate the appointment booking system under various scenarios.

Key Features:
User Registration Automation: Automates the process of patient registration by filling out necessary details like name, contact information, and medical history.
Appointment Scheduling: Automates the selection of available dates, times, and healthcare providers for appointments.
Booking Confirmation: Simulates the confirmation process to ensure a successful booking and notification flow.
Reusable Test Scripts: Implements the POM design pattern to create reusable, modular test scripts, making it easy to maintain and scale the automation suite for future updates.

Technologies Used:
Selenium WebDriver: For automating web browser interactions.
Python: For scripting the automation tests and implementing the framework.
Pytest: To execute test cases and provide a test report.
Page Object Model (POM): To separate test logic from web page elements, ensuring maintainability and scalability.

Project Structure:
/tests: Contains test cases that simulate different appointment booking scenarios.
/pages: Contains the Page Object Model classes representing various web pages involved in the appointment booking process (e.g., registration page, appointment page).
/data: Stores test data used for data-driven testing (e.g., patient details, appointment times).
/config: Contains configuration files for browser settings and test environment parameters.
