## Table of Contents

1. [Introduction](#officeops-workforce-productivity-suite)
   - [Deployed Website](#deployed-website)
   - [Default Credentials](#default-credentials)
2. [Features](#features)
   - [CEO Features](#ceo-can)
   - [Manager Features](#manager-can)
   - [Employee Features](#employee-can)
3. [Screenshots](#screenshots)
4. [Installation](#installation)
5. [Contributions](#contributions)
6. [License](#license)

# OfficeOps: Workforce Productivity Suite

OfficeOps is a powerful Workforce Productivity Suite built using Django, designed to streamline HR and office management processes within your organization. This project allows CEOs, Managers, and Employees to manage various aspects of HR, including employee information, attendance, feedback, and leave requests.

## Deployed Website

You can access the deployed OfficeOps website at [officeops.onrender.com](https://officeops.onrender.com/).

## Default Credentials

For CEO:
- Email: admin@admin.com
- Password: admin

For Manager:
- Email: manager@manager.com
- Password: manager

For Employee:
- Email: employee@employee.com
- Password: employee

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

| CEO                                        | Manager                                         | Employee                                     |
|:------------------------------------------:|:-----------------------------------------------:|:--------------------------------------------:|
| ![CEO_Home](/visuals/ss/CEO_Home.png) | ![Manager_Home](/visuals/ss/Manager_Home.png) | ![Employee_Home](/visuals/ss/Employee_Home.png)   |
| DashBoard                           | DashBoard                            | DashBoard                              |
| ![CEO_ManageEmployee](/visuals/ss/CEO_ManageEmployee.png) | ![Manager_AddSalary](/visuals/ss/Manager_AddSalary.png) | ![Employee_ViewSalary](/visuals/ss/Employee_ViewSalary.png)   |
| Manage Employee                            | Add Salary                            | View Salary                             |
| ![CEO_ManageManager](/visuals/ss/CEO_ManageManager.png) | ![Manager_TakeAttendance](/visuals/ss/Manager_TakeAttendance.png) | ![Employee_EditProfile](/visuals/ss/Employee_EditProfile.png)   |
| Manage Manager                            | Take Attendance                            | Edit Profile      
| ![CEO_EmployeeLeave](/visuals/ss/CEO_EmployeeLeave.png) | ![Manager_ViewAttendance](/visuals/ss/Manager_ViewAttendance.png) | ![Employee_Attendence](/visuals/ss/Employee_Attendence.png)   |
| Leave Application Reply                           | Update Attendance                            | View Attendance                             |
| ![CEO_ManagerLeave](/visuals/ss/CEO_ManagerLeave.png) | ![Manager_ApplyForLeave](/visuals/ss/Manager_ApplyForLeave.png) | ![Employee_ApplyForLeave](/visuals/ss/Employee_ApplyForLeave.png)   |
| Leave Application Response                           | Apply For Leave                           | Apply For Leave                             |
| ![CEO_EmployeeFeedbackReply](/visuals/ss/CEO_EmployeeFeedbackReply.png) | ![Manager_Feedback](/visuals/ss/Manager_Feedback.png) | ![Employee_Feedback](/visuals/ss/Employee_Feedback.png)   |
| Feedback                            | Feedback                            | Feedback                             |
| ![CEO_NotifyManager](/visuals/ss/CEO_NotifyManager.png) | ![Manager_Notification](/visuals/ss/Manager_Notification.png) | ![Employee_Notification](/visuals/ss/Employee_Notification.png)   |
| Send Notification                            | View Notification                            | View Notification                            |

## Installation

To set up this project on your local machine, follow these steps:

1. Clone the repository:
```
git clone https://github.com/Gaurav241/OfficeOps-WPS.git
```
2. Create a virtual environment and activate it:
```
python -m venv venv
venv\Scripts\activate
```
3. Navigate to the project directory and setup environment:
```
cd OfficeOps-WPS
```
Create .env File: Create a file named .env in the project directory. Add the following content to the .env file:
or just rename .env.example to .env
```
DATABASE_URL = "postgres://USER:PASSWORD@localhost:5432/DB_NAME"
SECRET_KEY = "your_secret_key"
```
NOTE: Make sure to replace YOUR_USER, YOUR_PASSWORD, YOUR_DB_NAME with your actual database credentials. 
Also, substitute YOUR_SECRET_KEY with your desired secret key.

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

This project is licensed under the [MIT License](LICENSE.txt).
