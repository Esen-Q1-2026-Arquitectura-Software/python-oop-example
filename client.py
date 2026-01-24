from typing import Protocol


class AccountingService(Protocol):
    def calculate_yearly_salary(self, monthly_salary: float) -> float: ...
    def evaluate_loan_eligibility(self, yearly_salary: float) -> bool: ...


class Client:
    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        monthly_salary: float,
        accounting_service: AccountingService,
    ):
        self.id = id
        self.name = name
        self.age = age
        self.monthly_salary = monthly_salary
        self._accounting = accounting_service

    def calculate_yearly_salary(self) -> float:
        """Business logic in methods, not constructor"""
        return self._accounting.calculate_yearly_salary(self.monthly_salary)

    def check_loan_eligibility(self) -> bool:
        """Business logic in methods, not constructor"""
        yearly = self.calculate_yearly_salary()
        return self._accounting.evaluate_loan_eligibility(yearly)

    def __str__(self):
        display = f"""
        Client
        id: {self.id}
        Name: {self.name}
        Age: {self.age}
        Monthly Salary: ${self.monthly_salary}
        Yearly Salary: ${self.calculate_yearly_salary()}
        Loan Approved: {self.check_loan_eligibility()}
        -------------------------------
        """
        return display
