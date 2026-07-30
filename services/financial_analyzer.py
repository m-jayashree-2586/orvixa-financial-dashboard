"""
Financial Analyzer Module

This module contains the business logic for analyzing a user's financial health.

Responsibilities:
----------------
- Calculate financial metrics.
- Generate an overall financial wellness score.
- Classify the user's financial personality.
- Return a consolidated financial analysis.

Design Principle:
-----------------
The FinancialAnalyzer does not store user information.
It only performs calculations using a User object.

Author: Jayashree M
Project: Orvixa - Personal Financial Wellness Dashboard
"""



from models.user import User
from typing import Dict,Any


class FinancialAnalyzer:
    """
    
    Performs financial analysis for a User.
    
    This class calculates key financial metrics and produces
    an overall financial health assessment.
    
    Attributes:
        user(User):The user whose financial information is analysed.
        
    """
    def __init__(self,user:User):
        """
        Initialize the FinancialAnalyzer.
        
        Args:
            user(User): User object containing financial information.
            
        """
        self.user=user

    def savings_rate(self)->float:
        """
        Calculate the percentage of monthly income that is saved.
        
        Formula:
            Savings Rate=((Income-Expenses)/Income) x 100
            
        Returns:
            float:Savings rate as a percentage.
            
        """
        monthly_savings = self.user.income - self.user.expenses
        return round((monthly_savings / self.user.income) * 100, 2)

    def debt_ratio(self)->float:

        """
        Calculate the debt-to-income ratio.
        
        Formula:
            Debt Ratio = (Debt/Income)x100
        
        Returns:
            float: Debt ratio as a percentage.
        """
        if self.user.income<=0:
            return 0.0
        return round((self.user.debt/self.user.income)*100,2)

    def emergency_fund_coverage(self)->float:
        """
        Calculate how many months the emergency fund can cover.
        
        Formula:
            Emergency Fund Coverage=Emergency Fund/Monthly Expenses
            
        Returns:
            float:Number of months of expense coverage.
            
        """
        if self.user.expenses <= 0:
            return 0.0
        return round(self.user.emergency_fund / self.user.expenses, 2)

    def investment_rate(self)->float:
        """
        Calculate the percentage of income invested every month.

        Formula:
            Investment Rate = (Investments / Income) × 100

        Returns:
            float: Investment rate as a percentage.
    
        """
        if self.user.income<=0:
            return 0.0
        return round((self.user.investments/self.user.income)*100,2)

    def overall_score(self)->int:
        """Calculate the user's overall financial health score.

        The overall score is calculated on a scale of 0 to 100 by
        combining four key financial metrics using a weighted scoring
        model.

        Weight Distribution:
            - Savings Rate: 30%
            - Debt-to-Income Ratio: 25%
            - Emergency Fund Coverage: 25%
            - Investment Rate: 20%

        Each metric contributes a predefined number of points based on
        commonly accepted personal finance guidelines. The weighted
        scores are summed to produce the final financial health score.

        Returns:
            int: Overall financial health score ranging from 0 to 100.

        Notes:
            The current scoring thresholds are based on general financial
            best practices and can be adjusted in future versions to
            accommodate different financial planning strategies.
        """
        savings_score = min(self.savings_rate() / 20, 1.0) * 30
        debt_score = max(1 - (self.debt_ratio() / 36), 0) * 25
        ef_score = min(self.emergency_fund_coverage() / 6, 1.0) * 25
        investment_score = min(self.investment_rate() / 15, 1.0) * 20
        total = savings_score + debt_score + ef_score + investment_score
        return round(total)

    def financial_personality(self) -> str:
        """Determine the user's financial personality.

        The financial personality is derived from the overall financial
        health score and provides an easy-to-understand interpretation
        of the user's financial standing.

        Personality Categories:
            - 85-100 : Financial Powerhouse
            - 70-84  : Smart Saver
            - 50-69  : Steady Builder
            - 30-49  : Getting Started
            - Below 30 : Needs a Plan

        Returns:
            str: Financial personality corresponding to the user's
            overall financial health score.
        """
        score = self.overall_score()
        if score >= 85:
            return "Financial Powerhouse"
        elif score >= 70:
            return "Smart Saver"
        elif score >= 50:
            return "Steady Builder"
        elif score >= 30:
            return "Getting Started"
        else:
            return "Needs a Plan"

    def analyze(self) -> Dict[str,Any]:

        """Generate a complete financial analysis for the user.

        Executes all financial calculations and consolidates the results
        into a single dictionary. This method serves as the primary
        interface between the business logic and the user interface.

        Returns:
            ict: Dictionary containing the calculated financial metrics,
            overall financial health score, and financial personality.

        Example:
            {
                "savings_rate": 25.0,
                "debt_ratio": 15.5,
                "emergency_fund_coverage": 5.2,
                "investment_rate": 12.0,
                "overall_score": 82,
                "financial_personality": "Smart Saver"
            }
        """
        return {
            "name":self.user.name,
            "savings_rate": self.savings_rate(),
            "debt_ratio": self.debt_ratio(),
            "emergency_fund_coverage": self.emergency_fund_coverage(),
            "investment_rate": self.investment_rate(),
            "overall_score": self.overall_score(),
            "financial_personality": self.financial_personality(),
        }

    
