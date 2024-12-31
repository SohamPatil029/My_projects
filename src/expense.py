"""
Dataclass to create a class. Datetime module for dates.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Expense:
    """
    Dataclass to represent an expense. It is immutable.
    """

    name: str
    amount: float
    date: datetime
    category: str
    description: str
    currency: str

    def __str__(self):
        return (
            f"{self.name} {self.amount:.2f} {self.currency} \n"
            f"on {self.date} for {self.category} ({self.description})"
        )

    def updateCSV(self):
        # Update CSV file with new expense
        pass


if __name__ == "__main__":
    # Test Expense class
    expense = Expense("Soham", 10.50, datetime.now(), "Food", "McDonalds", "$")
    print(expense)
