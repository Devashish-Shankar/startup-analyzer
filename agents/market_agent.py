import json
import re

from services.llm_service import get_llm
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

    llm = get_llm()

    prompt = MARKET_PROMPT.format(
        industry=research["industry"],
        business_model=research["business_model"],
        target_market=research["target_market"]
    )

    response = llm.invoke(prompt)

    market_data = extract_json(response.content)

    return {
        "market_result": market_data
    }