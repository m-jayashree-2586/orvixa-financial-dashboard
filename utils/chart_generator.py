"""
Chart generation utilities for the Orvixa application.

Defines the ChartGenerator class, which builds Plotly figure
objects for the Streamlit dashboard: an income-vs-expenses bar
chart, an income allocation donut chart, and a financial score
gauge.

This module contains no Streamlit-specific code. It focuses only
on converting user financial data into visual representations.
"""

import plotly.graph_objects as go

from models.user import User


class ChartGenerator:
    """Build Plotly figures used on the Orvixa report card."""

    @staticmethod
    def income_vs_expenses_chart(user: User) -> go.Figure:
        """Build a bar chart comparing monthly income and expenses.

        Args:
            user (User): The User instance to visualize.

        Returns:
            go.Figure: A Plotly figure containing a two-bar
                comparison chart.
        """
        fig = go.Figure(
            data=[
                go.Bar(
                    x=["Income", "Expenses"],
                    y=[user.income, user.expenses],
                    marker_color=["#2ecc71", "#e74c3c"],
                    text=[
                        f"₹{user.income:,.0f}",
                        f"₹{user.expenses:,.0f}",
                    ],
                    textposition="auto",
                )
            ]
        )

        fig.update_layout(
            title="Income vs Expenses",
            yaxis_title="Amount (₹)",
            showlegend=False,
        )

        return fig

    @staticmethod
    def income_allocation_chart(user: User) -> go.Figure:
        """Build a donut chart showing monthly income allocation.

        The chart divides monthly income into expenses, savings,
        debt payments, investments, and any remaining amount.

        Args:
            user (User): The User instance to visualize.

        Returns:
            go.Figure: A Plotly figure containing an income
                allocation donut chart.
        """
        leftover = max(
            user.income
            - user.expenses
            - user.savings
            - user.debt
            - user.investments,
            0,
        )

        labels = [
            "Expenses",
            "Savings",
            "Debt",
            "Investments",
            "Leftover",
        ]

        values = [
            user.expenses,
            user.savings,
            user.debt,
            user.investments,
            leftover,
        ]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=labels,
                    values=values,
                    hole=0.4,
                )
            ]
        )

        fig.update_layout(title="Income Allocation")

        return fig

    @staticmethod
    def financial_score_chart(score: int) -> go.Figure:
        """Build a gauge chart representing the financial health score.

        Args:
            score (int): Overall financial health score on a scale
                from 0 to 100.

        Returns:
            go.Figure: A Plotly figure containing a gauge indicator
                with different financial health zones.
        """
        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=score,
                title={"text": "Financial Health Score"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#2c3e50"},
                    "steps": [
                        {"range": [0, 40], "color": "#e74c3c"},
                        {"range": [40, 70], "color": "#f1c40f"},
                        {"range": [70, 100], "color": "#2ecc71"},
                    ],
                },
            )
        )

        return fig