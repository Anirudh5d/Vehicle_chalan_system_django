# Two Wheeler Vehicle Registration and Challan Management Web App

This web application allows users to register two-wheeler vehicles and manage challans associated with them. Registered users can add, edit, and delete vehicle registrations and associated challans.

## Features

- User authentication: Users can register, login, and logout.
- Vehicle registration: Users can register two-wheeler vehicles by providing details such as registration number, owner name, model, color, and registration date.
- Challan management: Users can add, edit, and delete challans for registered vehicles, specifying the chalan date, amount, and description.
- Dashboard: Users can view a dashboard showing registered vehicles along with total number of challans and total amount due for each vehicle.
- Responsive UI: The application is built using HTML, CSS, and Django, providing a responsive user interface for desktop and mobile devices.

## Technologies Used

- Python
- Django
- HTML
- CSS
- MySQL (as specified in the task requirements)

## Project Structure

The project structure is organized as follows:


## Getting Started

1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up MySQL database and update settings in `vehicle_challan_management/settings.py`.
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Contributing

Contributions are welcome! Please create a new branch and submit a pull request for any enhancements or bug fixes.
