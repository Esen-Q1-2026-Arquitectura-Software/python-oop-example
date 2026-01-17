class Client:
    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        monthly_salary: float,
        months: int,
        loan_threshold: float,
    ):
        self.id = id
        self.name = name
        self.age = age
        self.monthly_salary = monthly_salary
        self.months = months
        self.loan_threshold = loan_threshold
        # Tarea: dependency injection
        self.yearly_salary = self.get_yearly_salary()
        self.loan_approved = self.get_loan_approval()

    def get_yearly_salary(self) -> float:
        return self.monthly_salary * self.months

    def get_loan_approval(self) -> bool:
        return self.yearly_salary > self.loan_threshold

    def __str__(self):
        display = f"""
        Client
        id: {self.id}
        Name: {self.name}
        Age: {self.age}
        Monthly Salary: ${self.monthly_salary}
        Yearly Salary: ${self.yearly_salary}
        Loan Approved: {self.loan_approved}
        -------------------------------
        """
        return display
