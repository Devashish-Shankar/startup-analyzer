import json

from services.llm_service import get_llm
from prompts.report_prompt import REPORT_PROMPT

def report_agent(state):
    try:

        llm = get_llm()

        prompt = REPORT_PROMPT.format(

            research=json.dumps(
                state["research_result"],
                indent=2
            ),

            market=json.dumps(
                state["market_result"],
                indent=2
            ),

            market_sources=json.dumps(
                state.get(
                    "market_sources",
                    []
                ),
                indent=2
            ),

            competitors=json.dumps(
                state["competitor_result"],
                indent=2
            ),

            competitor_sources=json.dumps(
                state.get(
                    "competitor_sources",
                    []
                ),
                indent=2
            ),

            swot=json.dumps(
                state["swot_result"],
                indent=2
            ),

            investment=json.dumps(
                state["investment_result"],
                indent=2
            )
        )

        response = llm.invoke(
            prompt
        )

        return {
            "report_result": response.content
        }

    except Exception as e:

        print(
            f"\nReport Agent Error: {e}\n"
        )

        return {
            "report_result":
            f"# Report Generation Failed\n\nError: {str(e)}"
        }