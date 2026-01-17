class Client:
    def __init__(self, id: int, name: str, age: int, monthly_salary: float):
        self.id = id
        self.name = name
        self.age = age
        self.monthly_salary = monthly_salary

    def show_info(self):
        display = f"""
        Client
        id: {self.id}
        Name: {self.name}
        Age: {self.age}
        Monthly Salary: ${self.monthly_salary}
        Yearly Salary: ${self.monthly_salary * 12}
        Loan Approved: {self.monthly_salary * 12 > 3500}
        -------------------------------
        """
        print(display)
