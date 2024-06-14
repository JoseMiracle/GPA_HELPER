# GPA Helper

GPA Helper is a web application built with Django and Django Rest Framework (DRF) designed to help students calculate and manage their Grade Point Average (GPA). It not only calculates your GPA but also provides personalized recommendations to help you boost your academic performance.

## Features

- **GPA Calculation**: Quickly calculate your GPA based on your grades and credit hours.
- **Grade Management**: Store and manage your grades for multiple semesters.
- **User Authentication**: Secure user registration and login system.
- **GPA Improvement Recommendations**: Get personalized steps to help improve your GPA.
- **REST API**: Robust API for integrating with other applications.

## Installation

To get started with GPA Helper, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/JoseMiracle/GPA_HELPER.git
    cd GPA_HELPER
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

## Usage

Once the server is running, you can access the application at `http://127.0.0.1:8000/`. You can register a new user, log in, and start adding your courses and grades. The system will then provide recommendations to help you improve your GPA.

## Contributing

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) before getting started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
