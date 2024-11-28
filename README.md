# Flight Reservation System

This is a simple **Flight Reservation System** built using Python. It allows users to:

- Add flights
- Book flights
- Cancel reservations
- Display flights and reservations
- Search for flights by source, destination, and date
- Generate reports
- View a dashboard with analytics

## Features

- **Flight Management**: Add, view, and manage available flights.
- **Booking**: Users can book available flights by providing their name and email.
- **Reservations**: Users can view and cancel their reservations.
- **Reports**: Generates a detailed report of flight bookings and revenue.
- **Dashboard**: Provides insights on total flights, bookings, available seats, and revenue.

## Setup and Installation

### Prerequisites:

- Python 3.x
- `tabulate` library for displaying data in tables. (This is installed automatically if you use the included `requirements.txt` file.)

### Steps to Set Up:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flight-reservation-system.git
   ```
2. Navigate into the project directory:
   ```bash
   cd flight-reservation-system
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## File Structure

```bash
flight-reservation-system/
│
├── dashboard.py
├── sample_flights.py
├── report.py
├── flight.py
├── reservation.py
├── main.py
├── utils.py
├── requirements.txt
└── README.md
```


### Notes:
- Replace `https://github.com/yourusername/flight-reservation-system.git` with your actual GitHub repository URL.
- If you don’t have a `requirements.txt` yet, you can generate it by running:
  ```bash
  pip freeze > requirements.txt
