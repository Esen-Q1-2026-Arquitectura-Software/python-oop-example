from typing import Protocol


class AccountingProtocol(Protocol):
    months: int
    loan_threshold: float

    def calculate_yearly_salary(self, monthly_salary: float) -> float: ...

    def evaluate_loan_eligibility(self, yearly_salary: float) -> bool: ...


class Accounting:
    def __init__(self, months: int, loan_threshold: float):
        self.months = months
        self.loan_threshold = loan_threshold

    def calculate_yearly_salary(self, monthly_salary: float) -> float:
        return monthly_salary * self.months

    def evaluate_loan_eligibility(self, yearly_salary: float) -> bool:
        return yearly_salary > self.loan_threshold
