def main():
    print("Hello from python-oop-example!")
    print()

    client001_name = "Alice"
    client001_age = 30
    client001_monthly_salary = 250.0
    print(f"Client Name: {client001_name}")
    print(f"Client Age: {client001_age}")
    print(f"Client Monthly Salary: ${client001_monthly_salary}")
    print(f"Client Yearly Salary: ${client001_monthly_salary * 12}")
    print(f"loan approved: {client001_monthly_salary * 12 > 3500}")
    print("-------------------------------")
    print()

    client002_name = "Bob"
    client002_age = 25
    client002_monthly_salary = 300.0
    print(f"Client Name: {client002_name}")
    print(f"Client Age: {client002_age}")
    print(f"Client Monthly Salary: ${client002_monthly_salary}")
    print(f"Client Yearly Salary: ${client002_monthly_salary * 12}")
    print(f"loan approved: {client002_monthly_salary * 12 > 3500}")
    print("-------------------------------")
    print()

    client003_name = "Ted"
    client003_age = 27
    client003_monthly_salary = 200.0
    print(f"Client Name: {client003_name}")
    print(f"Client Age: {client003_age}")
    print(f"Client Monthly Salary: ${client003_monthly_salary}")
    print(f"Client Yearly Salary: ${client003_monthly_salary * 12}")
    print(f"loan approved: {client003_monthly_salary * 12 > 3500}")
    print("-------------------------------")
    print()


if __name__ == "__main__":
    main()
