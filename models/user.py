"""
User Model

Defines the User data model used throughout the Orvixa application.

This class stores personal and financial information entered by the user.
It does not perform any financial calculations.All business logic is handled separately by the FinancialAnalyzer service.
"""

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class User:
    """
    Represents a user's personal and financial profile.
    
    The User class acts as a data container for information that is 
    used by other services within the application.
    """
 
    name: str
    age: int
    occupation: str
    income: float
    expenses: float
    savings: float
    debt: float
    emergency_fund: float
    investments: float
 
    # Optional notes provided by the user.
    notes: Optional[str] = field(default=None)
 
    def to_dict(self) -> dict:
        """
        Convert the User object into a dictionary.

        Returns:
            dict:Dictionary containing all user attributes.

        This method is useful when exporting data,
        passing information to the UI, or generating reports.
        """
        return {
            "name": self.name,
            "age": self.age,
            "occupation": self.occupation,
            "income": self.income,
            "expenses": self.expenses,
            "savings": self.savings,
            "debt": self.debt,
            "emergency_fund": self.emergency_fund,
            "investments": self.investments,
            "notes": self.notes,
        }
 
    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """
        Create a User object from a dictionary.

        Args:
            data(dict):Dictionary containing user information.

        Returns:
            User: A new User instance.

        This method simplifies object creation from
        form inputs or JSON data.
        """
        return cls(
            name=data["name"],
            age=data["age"],
            occupation=data["occupation"],
            income=data["income"],
            expenses=data["expenses"],
            savings=data["savings"],
            debt=data["debt"],
            emergency_fund=data["emergency_fund"],
            investments=data["investments"],
            notes=data.get("notes"),
        )
 
    def __str__(self) -> str:
        """
        Return a readable string representation of the User object.
        
        Useful for debugging and logging.
        """
        return f"User({self.name}, age={self.age}, occupation={self.occupation})"
 