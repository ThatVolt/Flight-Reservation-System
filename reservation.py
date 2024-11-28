# reservation.py
import datetime
from flight import display_flights, flights, reservations
from tabulate import tabulate


def book_flight():
    """Books a flight."""
    display_flights()  # Call the display_flights function from flight.py
    flight_number = input("Enter the flight number to book: ")

    # Check if the flight exists in the flights data
    if flight_number not in flights:
        print("Flight not found.\n")
        return

    flight = flights[flight_number]

    # Check if there are seats available on the flight
    if flight["booked_seats"] >= flight["seats"]:
        print("Sorry, no seats available.\n")
        return

    passenger_name = input("Enter the passenger's name: ")
    passenger_email = input("Enter the passenger's email: ")

    # Book the flight and update the flight and reservation data
    flight["booked_seats"] += 1
    reservation_id = f"{flight_number}-{flight['booked_seats']}"
    reservations[reservation_id] = {
        "flight_number": flight_number,
        "passenger_name": passenger_name,
        "passenger_email": passenger_email,
        "booking_date": datetime.date.today().isoformat(),
    }

    # Display booking confirmation
    print(f"Booking successful! Reservation ID: {reservation_id}")
    print(f"Total price: ${flight['price']:.2f}\n")


def cancel_reservation():
    """Cancels a reservation."""
    reservation_id = input("Enter your reservation ID to cancel: ")

    # Check if the reservation ID exists
    if reservation_id not in reservations:
        print("Reservation ID not found.\n")
        return

    # Retrieve flight number from the reservation and update booked seats
    flight_number = reservations[reservation_id]["flight_number"]
    flights[flight_number]["booked_seats"] -= 1

    # Delete the reservation from the global reservations dictionary
    del reservations[reservation_id]
    print(f"Reservation {reservation_id} canceled successfully.\n")


def display_reservations():
    """Displays all reservations in a tabular format."""
    print("\n--- All Reservations ---")
    reservations_table = []

    # Loop through all reservations to display the details
    for res_id, details in reservations.items():
        reservations_table.append(
            [
                res_id,
                details["flight_number"],
                details["passenger_name"],
                details["passenger_email"],
                details["booking_date"],
            ]
        )

    # If there are reservations, display them in a table
    if reservations_table:
        headers = [
            "Reservation ID",
            "Flight Number",
            "Passenger Name",
            "Passenger Email",
            "Booking Date",
        ]
        print(
            tabulate(
                reservations_table,
                headers=headers,
                tablefmt="grid",
                colalign=("center",) * len(headers),
            )
        )
    else:
        print("No reservations found.\n")
    print()
