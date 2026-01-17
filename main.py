from client import Client


def main():
    print("Hello from python-oop-example!")
    print()

    client = Client(1, "Alice", 30, 250.0)
    client.show_info()

    client = Client(2, "Bob", 25, 300.0)
    client.show_info()

    client = Client(3, "Ted", 27, 200.0)
    client.show_info()

    client = Client(4, "Kimberly", 32, 600.0)
    client.show_info()


if __name__ == "__main__":
    main()
