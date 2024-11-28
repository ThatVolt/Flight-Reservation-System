# dashboard.py
from flight import flights  # Import the global flights variable
from tabulate import tabulate


def dashboard():
    """Displays analytics for the airline system."""
    total_flights = len(flights)
    total_bookings = sum(flight["booked_seats"] for flight in flights.values())
    total_seats = sum(flight["seats"] for flight in flights.values())
    total_revenue = sum(
        flight["booked_seats"] * flight["price"] for flight in flights.values()
    )

    dashboard_data = [
        ["Total Flights", total_flights],
        ["Total Bookings", total_bookings],
        ["Available Seats", total_seats - total_bookings],
        ["Total Revenue", f"${total_revenue:.2f}"],
    ]

    print("\n--- Dashboard ---")
    print(
        tabulate(
            dashboard_data,
            headers=["Metric", "Value"],
            tablefmt="grid",
            colalign=("center", "center"),
        )
    )
    print()
