import json
import re

from services.llm_service import get_llm
from tools.tavily_search import web_search
from prompts.competitor_prompt import COMPETITOR_PROMPT


def extract_json(text):

    match = re.search(
        r"```json\s*(.*?)\s*```",
        text,
        re.DOTALL
    )

    if match:
        return json.loads(match.group(1))

    return json.loads(text)


def competitor_agent(state):

    research = state["research_result"]

    industry = research["industry"]

    search_results = web_search(
        f"top competitors in {industry} industry market leaders companies"
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

    return {
        "competitor_result": competitor_data
    }