"""
Validator module for the Orvixa application.

This module provides input validation utilities to ensure that all
user-provided financial information is complete, logically valid,
and suitable for financial analysis.

Validating inputs before creating a User object prevents invalid
data from propagating through the application and producing
incorrect financial insights.

Each validation method raises a ValueError with a descriptive
message whenever an invalid input is detected.
"""
class Validator:
    @staticmethod
    def validate_name(name:str)->None:
        """Validate the user's name.

        Args:
            name(str): User's name.
        
        
        Raises:
            ValueError: If the name is empty or contains only whitespace.
        """
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")

    @staticmethod
    def validate_age(age:int)->None:
        """Validate the user's age.

        Args:
            age (int): User's age.

        Raises:
            ValueError: If age is missing or outside the supported range
            of 16 to 100 years.
        """
        if age is None:
            raise  ValueError("Age is equired.")
        if age<16 or age>100:
            raise ValueError("Age must be between 16 and 100.")
        
@staticmethod
def validate_income(income:float)->None:
    """Validate the user's monthly income.

    Args:
        income (float): Monthly income.

    Raises:
        ValueError: If income is missing, negative, or equal to zero.
    """
    if income is None:
        raise ValueError("Income is required.")
    if income<0:
        raise ValueError("Income cannot be negative.")
    if income==0:
        raise ValueError("Income must be greater than zero to analyze finances.")

@staticmethod
def validate_expenses(expenses:float,income:float)->None:
    """Validate the user's monthly expenses.

    Args:
        expenses (float): Monthly expenses.
        income (float): Monthly income.

    Raises:
        ValueError: If expenses are missing, negative, or appear
            unrealistically high compared to income.
    """
    if expenses is None:
        raise ValueError("Expenses are required.")
    if expenses<0:
        raise ValueError("Expenses cannot be negative.")
    if income>0 and expenses>income*3:
        raise ValueError("Expenses seem unrealistically high compared to income."
                         "Please double-check the value.")


@staticmethod
def validate_non_negative(value:float,field_name:str)->None:
    """Validate that a financial value is non-negative.

    This method is used for financial fields that share the same
    validation rules, such as savings, debt, emergency fund, and
    investments.

    Args:
        value (float): Value to validate.
        field_name (str): Name of the financial field.

    Raises:
        ValueError: If the value is missing or negative.
    """
    if value is None:
        raise ValueError(f"{field_name} is required.")
    if value<0:
        raise ValueError(f"{Field_name} cannot be negative.")


@staticmethod
def validate_all(cls,data:dict)->None:
    """Validate all user inputs.

    Executes all validation methods to ensure that the provided
    financial information is complete and valid before creating a
    User object or performing financial analysis.

    Args:
        data (dict): Dictionary containing user input data.

    Raises:
        ValueError: If any validation rule fails.
    """
    cls.validate_name(data.get("name"))
    cls.validate_age(data.get("age"))
    cls.validate_occupation(data.get("occupation"))
    cls.validate_income(data.get("income"))
    cls.validate_expenses(data.get("expenses"), data.get("income"))
    cls.validate_non_negative(data.get("savings"), "Savings")
    cls.validate_non_negative(data.get("debt"), "Debt")
    cls.validate_non_negative(data.get("emergency_fund"), "Emergency fund")
    cls.validate_non_negative(data.get("investments"), "Investments")
        
    
