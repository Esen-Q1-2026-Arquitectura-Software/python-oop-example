from client import Client


def main():
    print("Hello from python-oop-example!")
    print()

    clients = [
        Client(1, "Alice", 30, 250.0, 12, 3500.0),
        Client(2, "Bob", 25, 300.0, 12, 3500.0),
        Client(3, "Ted", 27, 200.0, 12, 3500.0),
        Client(4, "Kimberly", 32, 600.0, 12, 3500.0),
        Client(5, "Susie", 23, 150.0, 12, 3500.0),
    ]

    for client in clients:
        print(client)


if __name__ == "__main__":
    main()
