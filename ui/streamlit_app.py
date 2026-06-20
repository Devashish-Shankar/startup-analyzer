import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

from services.analyzer_service import run_analysis


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Multi-Agent Startup Analyzer",
    page_icon="🚀",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 3.5rem;
    font-weight: 800;
    color: #4F8BF9;
}

.subtitle {
    text-align: center;
    color: #A0AEC0;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

.section-header {
    color: #60A5FA;
    font-size: 26px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 10px;
}

.metric-card {
    background: #111827;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #374151;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("🚀 Startup Analyzer")

    st.markdown("""
    ### Multi-Agent Workflow

    ✅ Research Agent

    ✅ Market Agent

    ✅ Competitor Agent

    ✅ SWOT Agent

    ✅ Investment Agent

    ✅ Report Agent
    """)

    st.divider()

    st.info("""
Powered By

• LangGraph

• Gemini

• Tavily Search

• Streamlit
""")

# ==================================================
# HEADER
# ==================================================

st.markdown("""
<div class="main-title">
🚀 Multi-Agent Startup Analyzer
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
AI-Powered Startup Research, Market Intelligence,
Competitor Analysis, SWOT Evaluation and Investment Insights
</div>
""", unsafe_allow_html=True)

st.divider()

# ==================================================
# INPUT SECTION
# ==================================================

startup_name = st.text_input(
    "Startup Name"
)

description = st.text_area(
    "Startup Description",
    height=200
)

analyze_button = st.button(
    "Analyze Startup",
    use_container_width=True
)

# ==================================================
# ANALYSIS
# ==================================================

if analyze_button:

    if not startup_name or not description:

        st.warning(
            "Please enter Startup Name and Description."
        )

    else:

        with st.spinner(
            "🤖 Running Multi-Agent Analysis..."
        ):

            result = run_analysis(
                startup_name,
                description
            )

        if "error" in result:

            st.error(
                result["error"]
            )

        else:

            st.success(
                "Analysis Completed Successfully!"
            )

            # ==========================================
            # STARTUP SUMMARY
            # ==========================================

            research = result.get(
                "research_result",
                {}
            )

            st.markdown(
                '<div class="section-header">📌 Startup Summary</div>',
                unsafe_allow_html=True
            )

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(
                    "🏭 Industry",
                    research.get(
                        "industry",
                        "N/A"
                    )
                )

            with c2:

                st.metric(
                    "💼 Business Model",
                    research.get(
                        "business_model",
                        "N/A"
                    )
                )

            with c3:

                st.metric(
                    "🎯 Target Market",
                    research.get(
                        "target_market",
                        "N/A"
                    )
                )

            st.divider()

            # ==========================================
            # INVESTMENT DASHBOARD
            # ==========================================

            investment = result.get(
                "investment_result",
                {}
            )

            st.markdown(
                '<div class="section-header">💰 Investment Dashboard</div>',
                unsafe_allow_html=True
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Investment Score",
                    investment.get(
                        "investment_score",
                        "N/A"
                    )
                )

            with col2:

                st.metric(
                    "Risk Score",
                    investment.get(
                        "risk_score",
                        "N/A"
                    )
                )

            with col3:

                st.metric(
                    "Recommendation",
                    investment.get(
                        "recommendation",
                        "N/A"
                    )
                )

            st.divider()

            # ==========================================
            # TABS
            # ==========================================

            (
                tab1,
                tab2,
                tab3,
                tab4,
                tab5,
                tab6
            ) = st.tabs([
                "🔍 Research",
                "📈 Market",
                "🏆 Competitors",
                "⚡ SWOT",
                "💰 Investment",
                "📝 Report"
            ])

            # ==========================================
            # RESEARCH
            # ==========================================

            with tab1:

                st.subheader(
                    "Research Analysis"
                )

                st.json(
                    result["research_result"]
                )

            # ==========================================
            # MARKET
            # ==========================================

            with tab2:

                st.subheader(
                    "Market Analysis"
                )

                st.json(
                    result["market_result"]
                )

                if result.get(
                    "market_sources"
                ):

                    st.subheader(
                        "Market Sources"
                    )

                    for source in result[
                        "market_sources"
                    ]:

                        st.write(
                            f"🔗 {source}"
                        )

            # ==========================================
            # COMPETITORS
            # ==========================================

            with tab3:

                st.subheader(
                    "Competitor Analysis"
                )

                st.json(
                    result["competitor_result"]
                )

                if result.get(
                    "competitor_sources"
                ):

                    st.subheader(
                        "Competitor Sources"
                    )

                    for source in result[
                        "competitor_sources"
                    ]:

                        st.write(
                            f"🔗 {source}"
                        )

            # ==========================================
            # SWOT
            # ==========================================

            with tab4:

                st.subheader(
                    "SWOT Analysis"
                )

                st.json(
                    result["swot_result"]
                )

            # ==========================================
            # INVESTMENT
            # ==========================================

            with tab5:

                st.subheader(
                    "Investment Analysis"
                )

                st.json(
                    result["investment_result"]
                )

            # ==========================================
            # REPORT
            # ==========================================

            with tab6:

                st.subheader(
                    "Final Startup Report"
                )

                st.markdown(
                    result["report_result"]
                )

                st.download_button(
                    label="📥 Download Markdown Report",
                    data=result["report_result"],
                    file_name="startup_report.md",
                    mime="text/markdown"
                )

                pdf_path = Path(
                    "reports/startup_report.pdf"
                )

                if pdf_path.exists():

                    with open(
                        pdf_path,
                        "rb"
                    ) as pdf_file:

                        st.download_button(
                            label="📄 Download PDF Report",
                            data=pdf_file,
                            file_name="startup_report.pdf",
                            mime="application/pdf"
                        )