import json
import re

from services.llm_service import get_llm
from prompts.investment_prompt import INVESTMENT_PROMPT


def extract_json(text):

    match = re.search(
        r"```json\s*(.*?)\s*```",
        text,
        re.DOTALL
    )

    if match:
        return json.loads(match.group(1))

    return json.loads(text)


def investment_agent(state):

    llm = get_llm()

    prompt = INVESTMENT_PROMPT.format(
        research=json.dumps(state["research_result"], indent=2),
        market=json.dumps(state["market_result"], indent=2),
        competitors=json.dumps(state["competitor_result"], indent=2),
        swot=json.dumps(state["swot_result"], indent=2)
    )

    response = llm.invoke(prompt)


    investment_data = extract_json(
        response.content
    )

    return {
        "investment_result": investment_data
    }