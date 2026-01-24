from accounting import Accounting
from client import Client


def main():
    print("Hello from python-oop-example!")
    print()

    accounting = Accounting(12, 3500.0)  # Example instantiation; adjust as needed

    clients = [
        Client(1, "Alice", 30, 250.0, accounting),
        Client(2, "Bob", 25, 300.0, accounting),
        Client(3, "Ted", 27, 200.0, accounting),
        Client(4, "Kimberly", 32, 600.0, accounting),
        Client(5, "Susie", 23, 150.0, accounting),
    ]

    for client in clients:
        print(client)


if __name__ == "__main__":
    main()
