from tabulate import tabulate
from sample_flights import SAMPLE_FLIGHTS

flights = SAMPLE_FLIGHTS.copy()

reservations = {}


def display_flights():
    """Displays current flights in a tabular format."""
    print("\n--- Current Flights ---")
    flights_table = []
    for flight_num, details in flights.items():
        available_seats = details["seats"] - details["booked_seats"]
        flights_table.append(
            [
                flight_num,
                details["source"],
                details["destination"],
                details["date"],
                available_seats,
                f"${details['price']:.2f}",
            ]
        )

    headers = [
        "Flight Number",
        "Source",
        "Destination",
        "Date",
        "Available Seats",
        "Price",
    ]
    print(
        tabulate(
            flights_table,
            headers=headers,
            tablefmt="grid",
            colalign=("center",) * len(headers),
        )
    )
    print()


def add_flight():
    """Adds a new flight."""
    flight_number = input("Enter a new flight number: ")
    flight_details = {
        "source": input("Enter the departure location: "),
        "destination": input("Enter the destination: "),
        "seats": int(input("Enter the number of seats available: ")),
        "booked_seats": 0,
        "date": input("Enter the flight date (YYYY-MM-DD): "),
        "price": float(input("Enter the ticket price: ")),
    }
    flights[flight_number] = flight_details
    print(f"Flight {flight_number} added successfully!\n")


def search_flights():
    """Searches for flights based on criteria."""
    source = input("Enter departure location: ").lower()
    destination = input("Enter destination location: ").lower()
    date = input("Enter preferred date (YYYY-MM-DD, or press Enter to skip): ")

    print(f"\nFlights from {source.capitalize()} to {destination.capitalize()}:")
    found_flights = False
    search_results = []
    for flight_num, details in flights.items():
        if (
            details["source"].lower() == source
            and details["destination"].lower() == destination
            and (not date or details["date"] == date)
        ):
            available_seats = details["seats"] - details["booked_seats"]
            search_results.append(
                [
                    flight_num,
                    details["date"],
                    available_seats,
                    f"${details['price']:.2f}",
                ]
            )
            found_flights = True

    if search_results:
        headers = ["Flight Number", "Date", "Available Seats", "Price"]
        print(
            tabulate(
                search_results,
                headers=headers,
                tablefmt="grid",
                colalign=("center",) * len(headers),
            )
        )
    else:
        print("No flights found for this route and date.\n")
