# import sys
# from pathlib import Path

# ROOT_DIR = Path(__file__).resolve().parent.parent

# if str(ROOT_DIR) not in sys.path:
#     sys.path.insert(0, str(ROOT_DIR))
    
# import streamlit as st

# from services.analyzer_service import run_analysis


# st.set_page_config(
#     page_title="Startup Analyzer",
#     page_icon="🚀",
#     layout="wide"
# )

# st.title(
#     "🚀 Multi-Agent Startup Analyzer"
# )

# st.markdown(
#     """
#     Analyze startup ideas using:

#     - Research Agent
#     - Market Agent
#     - Competitor Agent
#     - SWOT Agent
#     - Investment Agent
#     """
# )

# st.divider()

# startup_name = st.text_input(
#     "Startup Name"
# )

# description = st.text_area(
#     "Startup Description",
#     height=200
# )

# analyze_button = st.button(
#     "Analyze Startup",
#     use_container_width=True
# )

# if analyze_button:

#     if not startup_name or not description:

#         st.warning(
#             "Please enter startup name and description."
#         )

#     else:

#         with st.spinner(
#             "Running Multi-Agent Analysis..."
#         ):

#             result = run_analysis(
#                 startup_name,
#                 description
#             )

#         if "error" in result:

#             st.error(
#                 result["error"]
#             )

#         else:

#             st.success(
#                 "Analysis Completed Successfully!"
#             )

#             # Research
#             with st.expander(
#                 "Research Analysis",
#                 expanded=True
#             ):
#                 st.json(
#                     result["research_result"]
#                 )

#             # Market
#             with st.expander(
#                 "Market Analysis"
#             ):
#                 st.json(
#                     result["market_result"]
#                 )

#             # Competitor
#             with st.expander(
#                 "Competitor Analysis"
#             ):
#                 st.json(
#                     result["competitor_result"]
#                 )

#             # SWOT
#             with st.expander(
#                 "SWOT Analysis"
#             ):
#                 st.json(
#                     result["swot_result"]
#                 )

#             # Investment
#             with st.expander(
#                 "Investment Analysis"
#             ):
#                 st.json(
#                     result["investment_result"]
#                 )

#             st.divider()

#             st.subheader(
#                 "Final Report"
#             )

#             st.markdown(
#                 result["report_result"]
#             )
            
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st

from services.analyzer_service import run_analysis

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Multi-Agent Startup Analyzer",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:
    st.title(
        "🚀 Startup Analyzer"
    )

    st.markdown(
        """
        ### Multi-Agent Workflow

        ✅ Research Agent

        ✅ Market Agent

        ✅ Competitor Agent

        ✅ SWOT Agent

        ✅ Investment Agent

        ✅ Report Agent
        """
    )

    st.divider()

    st.info(
        """
        Powered by:

        - LangGraph
        - Gemini
        - Tavily Search
        - Streamlit
        """
    )

# --------------------------------------------------
# Main Header
# --------------------------------------------------

st.title(
    "🚀 Multi-Agent Startup Analyzer"
)

st.markdown(
    """
        Analyze startup ideas using AI agents, real web research,
        competitor intelligence, SWOT analysis and investment evaluation.
    """
)

st.divider()

# --------------------------------------------------
# Input Section
# --------------------------------------------------

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

# --------------------------------------------------
# Analysis Section
# --------------------------------------------------

if analyze_button:
    if not startup_name or not description:

        st.warning(
            "Please enter startup name and description."
        )

    else:

        with st.spinner(
            "Running Multi-Agent Analysis..."
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

            # ----------------------------------------
            # Investment Dashboard
            # ----------------------------------------

            investment = result.get(
                "investment_result",
                {}
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

            # ----------------------------------------
            # Tabs
            # ----------------------------------------

            (
                tab1,
                tab2,
                tab3,
                tab4,
                tab5,
                tab6
            ) = st.tabs(
                [
                    "Research",
                    "Market",
                    "Competitors",
                    "SWOT",
                    "Investment",
                    "Report"
                ]
            )

            # ----------------------------------------
            # Research
            # ----------------------------------------

            with tab1:

                st.subheader(
                    "Research Analysis"
                )

                st.json(
                    result["research_result"]
                )

            # ----------------------------------------
            # Market
            # ----------------------------------------

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
                            source
                        )

            # ----------------------------------------
            # Competitors
            # ----------------------------------------

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
                            source
                        )

            # ----------------------------------------
            # SWOT
            # ----------------------------------------

            with tab4:

                st.subheader(
                    "SWOT Analysis"
                )

                st.json(
                    result["swot_result"]
                )

            # ----------------------------------------
            # Investment
            # ----------------------------------------

            with tab5:

                st.subheader(
                    "Investment Analysis"
                )

                st.json(
                    result["investment_result"]
                )

            # ----------------------------------------
            # Report
            # ----------------------------------------

            with tab6:

                st.subheader(
                    "Final Startup Report"
                )

                st.markdown(
                    result["report_result"]
                )

                st.download_button(
                    label="📥 Download Report",
                    data=result[
                        "report_result"
                    ],
                    file_name="startup_report.md",
                    mime="text/markdown"
                )