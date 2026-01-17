class Client:
    def __init__(self, id: int, name: str, age: int, monthly_salary: float):
        self.id = id
        self.name = name
        self.age = age
        self.monthly_salary = monthly_salary
        self.yearly_salary = self.get_yearly_salary()
        self.loan_approved = self.get_loan_approval()

    def get_yearly_salary(self) -> float:
        return self.monthly_salary * 12

    def get_loan_approval(self) -> bool:
        return self.yearly_salary > 3500

    def show_info(self):
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
        print(display)
