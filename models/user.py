"""
This is the User model - basically a container that holds everything
we know about one person's finances.
"""

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class User:
    """One person's profile and financial snapshot."""
 
    name: str
    age: int
    occupation: str
    income: float
    expenses: float
    savings: float
    debt: float
    emergency_fund: float
    investments: float
 
    # Not everyone will fill this in, so it defaults to nothing.
    notes: Optional[str] = field(default=None)
 
    def to_dict(self) -> dict:
        """
        Turns the user into a plain dictionary.
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
        return f"User({self.name}, age={self.age}, occupation={self.occupation})"
 