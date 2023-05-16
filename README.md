# Django Car Sharing

This repository contains a Django-based web application for car sharing. The application allows users to share and rent cars from other users, facilitating a convenient and cost-effective means of transportation.

## Features

- User registration and authentication(using email verification)
- Car listing and search functionality
- Booking and reservation system(single seats and multiple)
- Admin dashboard for managing users, cars, and bookings

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bajpaiayush0128/django-car-sharing.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django-car-sharing
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```bash
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application at `http://localhost:8000` in your web browser.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

Please ensure that your code adheres to the existing coding style and conventions used in the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- The Django framework
- [Bootstrap](https://getbootstrap.com) for the front-end design
- Other open-source libraries and dependencies used in this project
