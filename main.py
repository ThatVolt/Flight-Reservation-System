# main.py
from flight import display_flights, add_flight, search_flights
from reservation import book_flight, cancel_reservation, display_reservations
from dashboard import dashboard
from report import generate_report
from utils import clear_screen


def main():
    """Main driver function for the system."""
    menu_options = {
        "1": ("Add Flight", add_flight),
        "2": ("Book Flight", book_flight),
        "3": ("Cancel Reservation", cancel_reservation),
        "4": ("Display Flights", display_flights),
        "5": ("Display All Reservations", display_reservations),
        "6": ("Search Flights", search_flights),
        "7": ("Generate Report", generate_report),
        "8": ("Dashboard", dashboard),  # No need to pass flights here
        "9": ("Exit", None),
    }

    while True:
        print("\nAirline Reservation System")
        for key, (option, _) in menu_options.items():
            print(f"{key}. {option}")

        choice = input("Choose an option (1-9): ")
        if choice == "9":
            print("Thank you for using the Airline Reservation System!")
            break
        elif choice in menu_options:
            menu_options[choice][1]()  # This calls the function directly
            input("\nPress Enter to continue...")
            clear_screen()
        else:
            print("Invalid choice. Please try again.\n")
            input("\nPress Enter to continue...")
            clear_screen()


if __name__ == "__main__":
    main()
