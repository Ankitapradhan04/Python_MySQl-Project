# Smart Parking System

## Overview

The Smart Parking System is a Python project that leverages MySQL to manage and store data related to a smart parking system. The system efficiently handles parking space allocation, occupancy tracking, and user management.

## Features

- **User Management**: Register and manage users with their parking preferences.
- **Parking Space Allocation**: Dynamically allocate parking spaces based on user preferences and availability.
- **Occupancy Tracking**: Monitor and track the occupancy status of parking spaces in real-time.
- **MySQL Database Integration**: Utilizes MySQL as the backend database to store and retrieve data.

## Setup

### Prerequisites

- Python 3.x
- MySQL server installed and running

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/smart-parking-system.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd smart-parking-system
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up MySQL Database:**
   
    - Create a MySQL database and update the `config.py` file with your database credentials.

    ```python
    # config.py
    DB_HOST = 'your_mysql_host'
    DB_USER = 'your_mysql_user'
    DB_PASSWORD = 'your_mysql_password'
    DB_NAME = 'your_database_name'
    ```

5. **Run the application:**

    ```bash
    python main.py
    ```

## Usage

1. Register users and their parking preferences.
2. Allocate parking spaces based on user preferences and availability.
3. Monitor real-time occupancy status.
4. Update user information and parking allocations.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please submit a pull request.
