"""Chart generation utilities for the Orvixa application.

This module provides Plotly chart generators used by the Orvixa
financial wellness dashboard.

The charts support both light and dark themes so that their appearance
remains consistent with the application's selected theme.
"""

import plotly.graph_objects as go

from models.user import User


class ChartGenerator:
    """Build Plotly figures used on the Orvixa report card."""

    @staticmethod
    def _chart_theme(dark_mode: bool) -> dict:
        """Return chart colors based on the selected theme.

        Args:
            dark_mode: Whether the application is using dark mode.

        Returns:
            dict: Theme colors for Plotly charts.
        """
        if dark_mode:
            return {
                "background": "#111C2E",
                "paper": "#111C2E",
                "text": "#F8FAFC",
                "grid": "#26364D",
            }

        return {
            "background": "#FFFFFF",
            "paper": "#FFFFFF",
            "text": "#172033",
            "grid": "#DCE6F2",
        }

    @staticmethod
    def income_vs_expenses_chart(
        user: User,
        dark_mode: bool = False,
    ) -> go.Figure:
        """Build a bar chart comparing monthly income and expenses.

        Args:
            user: User instance containing income and expense data.
            dark_mode: Whether the application is using dark mode.

        Returns:
            go.Figure: Plotly bar chart comparing income and expenses.
        """
        theme = ChartGenerator._chart_theme(dark_mode)

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
            plot_bgcolor=theme["background"],
            paper_bgcolor=theme["paper"],
            font={"color": theme["text"]},
            xaxis={"gridcolor": theme["grid"]},
            yaxis={"gridcolor": theme["grid"]},
        )

        return fig

    @staticmethod
    def income_allocation_chart(
        user: User,
        dark_mode: bool = False,
    ) -> go.Figure:
        """Build a donut chart showing monthly income allocation.

        Args:
            user: User instance containing financial data.
            dark_mode: Whether the application is using dark mode.

        Returns:
            go.Figure: Plotly donut chart showing income allocation.
        """
        theme = ChartGenerator._chart_theme(dark_mode)

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

        fig.update_layout(
            title="Income Allocation",
            plot_bgcolor=theme["background"],
            paper_bgcolor=theme["paper"],
            font={"color": theme["text"]},
        )

        return fig

    @staticmethod
    def financial_score_chart(
        score: int,
        dark_mode: bool = False,
    ) -> go.Figure:
        """Build a gauge chart showing the overall financial score.

        Args:
            score: Overall financial health score from 0 to 100.
            dark_mode: Whether the application is using dark mode.

        Returns:
            go.Figure: Plotly gauge chart displaying the financial score.
        """
        theme = ChartGenerator._chart_theme(dark_mode)

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=score,
                title={"text": "Financial Health Score"},
                number={"font": {"color": theme["text"]}},
                gauge={
                    "axis": {
                        "range": [0, 100],
                        "tickcolor": theme["text"],
                    },
                    "bar": {"color": "#2563EB"},
                    "steps": [
                        {"range": [0, 40], "color": "#e74c3c"},
                        {"range": [40, 70], "color": "#f1c40f"},
                        {"range": [70, 100], "color": "#2ecc71"},
                    ],
                },
            )
        )

        fig.update_layout(
            plot_bgcolor=theme["background"],
            paper_bgcolor=theme["paper"],
            font={"color": theme["text"]},
        )

        return fig