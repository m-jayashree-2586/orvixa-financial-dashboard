"""
Streamlit presentation layer for the Orvixa application.

This module is the application's entry point. It collects financial
information from the user, delegates validation and analysis to the
appropriate service classes, and displays the resulting financial
wellness report.

The module contains no financial calculation or validation logic.
Those responsibilities are handled by the User, Validator,
FinancialAnalyzer, RecommendationEngine, and ChartGenerator classes.

The dashboard supports both light and dark visual themes.
"""

import streamlit as st

from models.user import User
from services.validator import Validator
from services.financial_analyzer import FinancialAnalyzer
from services.recommendation_engine import RecommendationEngine
from utils.chart_generator import ChartGenerator


# -------------------------------------------------------------------
# Page configuration
# -------------------------------------------------------------------

st.set_page_config(
    page_title="Orvixa - Financial Wellness",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# -------------------------------------------------------------------
# Theme state
# -------------------------------------------------------------------

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False


# -------------------------------------------------------------------
# Custom styling
# -------------------------------------------------------------------

if st.session_state.dark_mode:
    background = "#0B1220"
    card_background = "#111C2E"
    secondary_background = "#17243A"
    text_color = "#F8FAFC"
    secondary_text = "#A9B7C9"
    border_color = "#26364D"
    accent_color = "#60A5FA"
    input_background = "#162235"
else:
    background = "#F4F8FC"
    card_background = "#FFFFFF"
    secondary_background = "#EAF3FF"
    text_color = "#172033"
    secondary_text = "#64748B"
    border_color = "#DCE6F2"
    accent_color = "#2563EB"
    input_background = "#FFFFFF"


st.markdown(
    f"""
    <style>

    /* Main application */
    .stApp {{
        background-color: {background};
        color: {text_color};
    }}

    /* Main content width */
    .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }}

    /* Hide Streamlit branding */
    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    /* Headings */
    h1, h2, h3 {{
        color: {text_color} !important;
    }}

    /* Paragraphs */
    p {{
        color: {secondary_text};
    }}

    /* Input labels */
    label {{
        color: {text_color} !important;
    }}

    /* Input fields */
    div[data-baseweb="input"],
    div[data-baseweb="select"] {{
        background-color: {input_background};
        border-radius: 10px;
    }}

    /* Buttons */
    .stButton > button,
    .stFormSubmitButton > button {{
        border-radius: 12px;
        border: none;
        background-color: {accent_color};
        color: white;
        font-weight: 600;
        padding: 0.65rem 1.4rem;
    }}

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {{
        opacity: 0.9;
    }}

    /* Cards */
    .orvixa-card {{
        background-color: {card_background};
        border: 1px solid {border_color};
        border-radius: 18px;
        padding: 1.4rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 18px rgba(0, 0, 0, 0.05);
    }}

    .metric-card {{
        background-color: {card_background};
        border: 1px solid {border_color};
        border-radius: 16px;
        padding: 1.2rem;
        min-height: 125px;
    }}

    .metric-label {{
        color: {secondary_text};
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }}

    .metric-value {{
        color: {text_color};
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 0.35rem;
    }}

    .metric-description {{
        color: {secondary_text};
        font-size: 0.8rem;
        margin-top: 0.3rem;
    }}

    /* Hero section */
    .hero {{
        background: linear-gradient(
            135deg,
            {accent_color},
            #7C3AED
        );
        border-radius: 24px;
        padding: 2rem;
        margin: 1.5rem 0 2rem 0;
        color: white;
    }}

    .hero h2 {{
        color: white !important;
        margin-bottom: 0.4rem;
    }}

    .hero p {{
        color: rgba(255,255,255,0.85);
        margin-bottom: 0;
    }}

    /* Score */
    .score {{
        text-align: center;
        padding: 1.2rem;
    }}

    .score-number {{
        font-size: 3.5rem;
        font-weight: 800;
        color: {accent_color};
        line-height: 1;
    }}

    .score-label {{
        color: {secondary_text};
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 0.5rem;
    }}

    .personality {{
        text-align: center;
        padding: 1.5rem;
    }}

    .personality-title {{
        color: {accent_color};
        font-size: 1.5rem;
        font-weight: 700;
    }}

    .personality-description {{
        color: {secondary_text};
        margin-top: 0.5rem;
    }}

    /* Recommendation cards */
    .recommendation {{
        background-color: {card_background};
        border: 1px solid {border_color};
        border-radius: 16px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
        color: {text_color};
    }}

    /* Progress */
    .progress-label {{
        color: {text_color};
        font-weight: 600;
        margin-bottom: 0.25rem;
    }}

    .progress-container {{
        background-color: {secondary_background};
        border-radius: 20px;
        height: 10px;
        overflow: hidden;
        margin-bottom: 1rem;
    }}

    .progress-bar {{
        background-color: {accent_color};
        height: 100%;
        border-radius: 20px;
    }}

    /* Divider */
    hr {{
        border-color: {border_color};
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# -------------------------------------------------------------------
# Header
# -------------------------------------------------------------------

header_col1, header_col2 = st.columns([4, 1])

with header_col1:
    st.markdown(
        f"""
        <div>
            <h1 style="margin-bottom:0;">💙 Orvixa</h1>
            <p style="font-size:1.05rem;">
                Your Personal Financial Wellness Dashboard
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with header_col2:
    dark_mode = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state.dark_mode,
    )

    if dark_mode != st.session_state.dark_mode:
        st.session_state.dark_mode = dark_mode
        st.rerun()


# -------------------------------------------------------------------
# Hero section
# -------------------------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <h2>Understand your money. Improve your future. ✨</h2>
        <p>
            Enter your financial details and let Orvixa help you
            understand your financial health with simple metrics,
            visual insights, and personalized recommendations.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# -------------------------------------------------------------------
# Input form
# -------------------------------------------------------------------

with st.form("user_input_form"):

    st.subheader("👤 Your Financial Profile")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Name",
            placeholder="Enter your name",
        )

        age = st.number_input(
            "Age",
            min_value=0,
            max_value=120,
            step=1,
        )

        occupation = st.text_input(
            "Occupation",
            placeholder="e.g. Student, Engineer",
        )

    with col2:
        income = st.number_input(
            "Monthly Income (₹)",
            min_value=0.0,
            step=1000.0,
        )

        expenses = st.number_input(
            "Monthly Expenses (₹)",
            min_value=0.0,
            step=1000.0,
        )

    st.subheader("💰 Your Financial Snapshot")

    col3, col4 = st.columns(2)

    with col3:
        savings = st.number_input(
            "Monthly Savings (₹)",
            min_value=0.0,
            step=500.0,
        )

        debt = st.number_input(
            "Monthly Debt Payments (₹)",
            min_value=0.0,
            step=500.0,
        )

    with col4:
        emergency_fund = st.number_input(
            "Emergency Fund (₹)",
            min_value=0.0,
            step=1000.0,
        )

        investments = st.number_input(
            "Monthly Investments (₹)",
            min_value=0.0,
            step=500.0,
        )

    submitted = st.form_submit_button(
        "💙 Analyze My Finances",
        use_container_width=True,
    )


# -------------------------------------------------------------------
# Analysis
# -------------------------------------------------------------------

if submitted:

    form_data = {
        "name": name,
        "age": int(age),
        "occupation": occupation,
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "debt": debt,
        "emergency_fund": emergency_fund,
        "investments": investments,
    }

    try:

        # Validate all user input before creating the User object.
        Validator.validate_all(form_data)

        # Convert validated data into a User model.
        user = User.from_dict(form_data)

        # Analyze the user's financial health.
        analysis = FinancialAnalyzer(user).analyze()

        # Generate personalized recommendations.
        recommendations = RecommendationEngine(analysis).generate()

        st.success(
            f"Analysis complete for {user.name}! 💙"
        )

        # -----------------------------------------------------------
        # Financial health overview
        # -----------------------------------------------------------

        st.subheader("📊 Your Financial Health")

        score_col, personality_col = st.columns(2)

        with score_col:
            st.markdown(
                f"""
                <div class="orvixa-card score">
                    <div class="score-number">
                        {analysis["overall_score"]}
                    </div>
                    <div class="score-label">
                        Financial Health Score / 100
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with personality_col:

            personality = analysis["financial_personality"]

            st.markdown(
                f"""
                <div class="orvixa-card personality">
                    <div class="score-label">
                        YOUR FINANCIAL PERSONALITY
                    </div>
                    <div class="personality-title">
                        💙 {personality}
                    </div>
                    <div class="personality-description">
                        Your score reflects your savings, debt,
                        emergency fund, and investment habits.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # -----------------------------------------------------------
        # Metric cards
        # -----------------------------------------------------------

        st.subheader("💰 Your Money Habits")

        col_a, col_b, col_c, col_d = st.columns(4)

        metrics = [
            (
                col_a,
                "Savings Rate",
                f'{analysis["savings_rate"]}%',
                "Target: 20%",
            ),
            (
                col_b,
                "Debt Ratio",
                f'{analysis["debt_ratio"]}%',
                "Lower is better",
            ),
            (
                col_c,
                "Emergency Fund",
                f'{analysis["emergency_fund_coverage"]} mo',
                "Target: 3–6 months",
            ),
            (
                col_d,
                "Investment Rate",
                f'{analysis["investment_rate"]}%',
                "Target: 15%",
            ),
        ]

        for column, label, value, description in metrics:
            with column:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-label">
                            {label}
                        </div>
                        <div class="metric-value">
                            {value}
                        </div>
                        <div class="metric-description">
                            {description}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.write("")

        # -----------------------------------------------------------
        # Progress toward financial targets
        # -----------------------------------------------------------

        st.subheader("🎯 Progress Toward Healthy Targets")

        savings_progress = min(
            analysis["savings_rate"] / 20 * 100,
            100,
        )

        investment_progress = min(
            analysis["investment_rate"] / 15 * 100,
            100,
        )

        emergency_progress = min(
            analysis["emergency_fund_coverage"] / 6 * 100,
            100,
        )

        progress_data = [
            ("Savings Rate", savings_progress),
            ("Investment Rate", investment_progress),
            ("Emergency Fund", emergency_progress),
        ]

        for label, progress in progress_data:

            st.markdown(
                f"""
                <div class="progress-label">
                    {label} — {progress:.0f}%
                </div>

                <div class="progress-container">
                    <div
                        class="progress-bar"
                        style="width:{progress}%;">
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # -----------------------------------------------------------
        # Charts
        # -----------------------------------------------------------

        st.subheader("📈 Visual Breakdown")

        st.plotly_chart(
            ChartGenerator.financial_score_chart(
                analysis["overall_score"],
                dark_mode=st.session_state.dark_mode,
            ),
            use_container_width=True,
        )

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.plotly_chart(
                ChartGenerator.income_vs_expenses_chart(
                    user,
                    dark_mode=st.session_state.dark_mode,
                ),   
                use_container_width=True,
            )

        with chart_col2:
            st.plotly_chart(
                ChartGenerator.income_allocation_chart(
                    user,
                    dark_mode=st.session_state.dark_mode,
                ),
                use_container_width=True,
            )

        # -----------------------------------------------------------
        # Recommendations
        # -----------------------------------------------------------

        st.subheader("💡 Personalized Insights")

        recommendation_icons = [
            "💰",
            "💳",
            "🛡️",
            "📈",
        ]

        for icon, recommendation in zip(
            recommendation_icons,
            recommendations,
        ):
            st.markdown(
                f"""
                <div class="recommendation">
                    {icon} &nbsp; {recommendation}
                </div>
                """,
                unsafe_allow_html=True,
            )

        # -----------------------------------------------------------
        # Closing message
        # -----------------------------------------------------------

        st.markdown(
            """
            <div class="hero">
                <h2>Keep building your financial future. 💙</h2>
                <p>
                    Small, consistent financial habits can make a
                    meaningful difference over time.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    except ValueError as error:
        # Validation errors are displayed as user-friendly
        # messages instead of exposing Python tracebacks.
        st.error(str(error))