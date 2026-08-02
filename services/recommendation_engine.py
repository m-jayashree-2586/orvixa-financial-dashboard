"""
Recommendation engine for the Orvixa application.

This module generates personalized financial recommendations
based on the financial metrics produced by the FinancialAnalyzer.

The recommendation engine follows a rule-based approach using
predefined financial thresholds to provide practical and
easy-to-understand guidance for improving financial health.

Each recommendation is generated independently, allowing the
application to provide both improvement suggestions and positive
reinforcement where appropriate.
"""


class RecommendationEngine:
    """Generate personalized financial recommendations.

    This class analyzes the financial metrics produced by the
    FinancialAnalyzer and generates actionable recommendations
    to help users improve their financial well-being.
    """

    def __init__(self, analysis: dict):
        """Initialize the recommendation engine.

        Args:
            analysis (dict): Dictionary containing the calculated
                financial metrics produced by the FinancialAnalyzer.
        """
        self.analysis = analysis

        
    def _savings_recommendation(self) -> str:
        """Generate a recommendation based on the user's savings rate.

        Returns:
            str: Recommendation for improving or maintaining
            monthly savings habits.
        """
        rate = self.analysis.get("savings_rate", 0)
        if rate < 10:
            return "Your savings rate is quite low - try to save at least 10-20% of your income each month."
        elif rate < 20:
            return "You're saving, but there's room to grow - aim to push your savings rate closer to 20%."
        else:
            return "Great job - your savings rate is healthy. Keep this habit consistent."


    def _debt_recommendation(self) -> str:
        """Generate a recommendation based on the user's debt ratio.

        Returns:
            str: Recommendation for managing debt effectively and
            improving financial stability.
        """
        ratio = self.analysis.get("debt_ratio", 0)
        if ratio > 36:
            return "Your debt payments are taking up a large share of your income - consider prioritizing debt repayment before other goals."
        elif ratio > 15:
            return "Your debt is manageable, but paying it down faster would free up more room in your budget."
        else:
            return "Your debt load looks healthy relative to your income."


    def _emergency_fund_recommendation(self) -> str:
        """Generate a recommendation based on emergency fund coverage.

        Returns:
            str: Recommendation for building or maintaining an
                adequate emergency fund.
        """
        months = self.analysis.get("emergency_fund_coverage", 0)
        if months < 3:
            return "Build an emergency fund covering at least three months of expenses - this is your safety net if income stops suddenly."
        elif months < 6:
            return "Your emergency fund covers a few months - consider growing it toward a 6-month cushion for extra security."
        else:
            return "Your emergency fund is in great shape and covers a solid safety margin."

    def _investment_recommendation(self) -> str:
        """Generate a recommendation based on the user's investment rate.

        Returns:
            str: Recommendation for improving or maintaining
            long-term investment habits.
        """
        rate = self.analysis.get("investment_rate", 0)
        if rate < 5:
            return "You're investing very little of your income - even starting small can compound significantly over time."
        elif rate < 15:
            return "You're investing consistently - increasing this gradually will strengthen your long-term wealth."
        else:
            return "You're investing a strong portion of your income - keep it up."

    def generate(self) -> list[str]:
        """Generate all financial recommendations.

        Executes each recommendation rule and combines the results
        into a single list of personalized financial guidance.

        Returns:
            list[str]: Collection of financial recommendations
                covering savings, debt, emergency funds, and
                investment habits.
        """
        return [
            self._savings_recommendation(),
            self._debt_recommendation(),
            self._emergency_fund_recommendation(),
            self._investment_recommendation(),
        ]
    