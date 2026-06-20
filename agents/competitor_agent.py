import json
import re

from services.llm_service import get_llm
from tools.tavily_search import web_search
from prompts.competitor_prompt import COMPETITOR_PROMPT


def extract_json(text):

    text = text.strip()

    match = re.search(
        r"```json\s*(.*?)\s*```",
        text,
        re.DOTALL
    )

    if match:
        text = match.group(1)

    return json.loads(text)


def competitor_agent(state):
    try:
        research = state["research_result"]
        industry = research["industry"]
        search_results = web_search(
            f"top competitors in {industry} industry leading companies startups market leaders 2025"
        )

        llm = get_llm()

        prompt = COMPETITOR_PROMPT.format(
            industry=research["industry"],
            business_model=research["business_model"],
            target_market=research["target_market"],
            competitor_research=json.dumps(
                search_results,
                indent=2
            )
        )

        response = llm.invoke(prompt)

        competitor_data = extract_json(
            response.content
        )

        # Extract source URLs
        sources = [
            result.get("url")
            for result in search_results.get(
                "results",
                []
            )
            if result.get("url")
        ]

        return {
            "competitor_result": competitor_data,
            "competitor_sources": sources
        }
    except Exception as e:

        print(
            f"\nCompetitor Agent Error: {e}\n"
        )

        return {
            "competitor_result": {
                "competitor_analysis": [],
                "competitive_threats": [],
                "error": str(e)
            },
            "competitor_sources": []
        }
