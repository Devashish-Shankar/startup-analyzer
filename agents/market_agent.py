import json
import re

from services.llm_service import get_llm
from tools.tavily_search import web_search
from prompts.market_prompt import MARKET_PROMPT


def extract_json(text):

    match = re.search(
        r"```json\s*(.*?)\s*```",
        text,
        re.DOTALL
    )

    if match:
        return json.loads(match.group(1))

    return json.loads(text)


def market_agent(state):

    research = state["research_result"]

    industry = research["industry"]

    search_results = web_search(
        f"{industry} market size growth rate trends"
    )

    llm = get_llm()

    prompt = MARKET_PROMPT.format(
        industry=research["industry"],
        business_model=research["business_model"],
        target_market=research["target_market"],
        market_research=json.dumps(
            search_results,
            indent=2
        )
    )

    response = llm.invoke(prompt)

    # LLM Analysis
    analysis_data = extract_json(
        response.content
    )

    return {
        "market_result": analysis_data
    }