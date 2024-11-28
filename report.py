# report.py
from tabulate import tabulate
from flight import flights  # Import global flights variable


def generate_report():
    """Generates a report for all flights."""
    total_bookings = sum(flight["booked_seats"] for flight in flights.values())
    total_revenue = sum(
        flight["booked_seats"] * flight["price"] for flight in flights.values()
    )

    print("\n--- Flight Report ---")
    report_data = []
    for flight_num, details in flights.items():
        bookings = details["booked_seats"]
        revenue = bookings * details["price"]
        report_data.append(
            [
                flight_num,
                details["source"],
                details["destination"],
                bookings,
                f"${revenue:.2f}",
            ]
        )

    headers = ["Flight Number", "Source", "Destination", "Bookings", "Revenue"]
    print(
        tabulate(
            report_data,
            headers=headers,
            tablefmt="grid",
            colalign=("center",) * len(headers),
        )
    )
    print(f"\nTotal Bookings: {total_bookings}")
    print(f"Total Revenue: ${total_revenue:.2f}\n")
