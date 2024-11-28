import os


def clear_screen():
    """Clears the terminal screen."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
