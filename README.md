# OfficeOps: Workforce Productivity Suite

OfficeOps is a powerful Workforce Productivity Suite built using Django, designed to streamline HR and office management processes within your organization. This project allows CEOs, Managers, and Employees to manage various aspects of HR, including employee information, attendance, feedback, and leave requests.

## Features

### CEO Can:

- **Manage Your Team:** CEOs have full control to add, update, and remove Managers and Employees within the organization.

- **Organize Company Structure:** CEOs can create and manage Divisions and Departments to structure the company efficiently.

- **Track Employee Attendance:** Monitor employee attendance to ensure a productive workforce.

- **Engage with Feedback:** Review and respond to feedback from both employees and managers to foster a collaborative workplace.

- **Manage Leave Requests:** Approve or reject leave requests from Managers and Employees, ensuring operational continuity.

### Manager Can:

- **Maintain Attendance:** Managers can record and update employee attendance, making it easier to track team productivity.

- **Handle Salaries:** Add or update salary information for employees, streamlining payroll processes.

- **Apply for Leave:** Managers can request time off and have it reviewed by the CEO.

- **Communicate with CEO:** Managers can share feedback and important information directly with the CEO.

### Employee Can:

- **Check Attendance:** Employees can view their attendance records to stay on top of their work hours.

- **Access Salary Information:** Check salary details for transparency and financial planning.

- **Request Leave:** Submit leave requests to the CEO, ensuring seamless time-off management.

- **Connect with CEO:** Employees can provide feedback and share important concerns with the CEO, fostering a culture of open communication.

## Screenshots

SOON

## Installation

To set up this project on your local machine, follow these steps:

1. Clone the repository:
```
git clone https://github.com/Gaurav241/OfficeOps-WPS.git
```
2. Navigate to the project directory:
```
cd OfficeOps-WPS
```
3. Create a virtual environment and activate it:
```
python -m venv venv
source venv\Scripts\activate
```
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Configure the database settings in settings.py and run migrations:
```
python manage.py makemigrations main_app
python manage.py migrate
```
6. Create a superuser account:
```
python manage.py createsuperuser
```
7. Start the development server:
```
python manage.py runserver
```
8. Access the admin panel at http://localhost:8000/ and log in with the superuser credentials.

## Contributing

Contributions are welcome! If you'd like to contribute to OfficeOps-WPS, feel free to open a pull request. We value your input and appreciate your help in making the app even better.

## License

This project is licensed under the MIT License.
