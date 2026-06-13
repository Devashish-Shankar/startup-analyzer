import json
import re

from services.llm_service import get_llm
from tools.market_research import get_market_data
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

    # Tool Output
    market_data = get_market_data(
        industry
    )

    llm = get_llm()

    prompt = MARKET_PROMPT.format(
        industry=research["industry"],
        business_model=research["business_model"],
        target_market=research["target_market"],
        market_data=json.dumps(
            market_data,
            indent=2
        )
    )

    response = llm.invoke(prompt)

    # LLM Analysis
    analysis_data = extract_json(
        response.content
    )

    return {
        "market_result": {
            **market_data,
            **analysis_data
        }
    }