import json
import re

from services.llm_service import get_llm
from prompts.swot_prompt import SWOT_PROMPT


def extract_json(text):

    match = re.search(
        r"```json\s*(.*?)\s*```",
        text,
        re.DOTALL
    )

    if match:
        return json.loads(match.group(1))

    return json.loads(text)


def swot_agent(state):

    research = state["research_result"]
    competitors = state["competitor_result"]

    llm = get_llm()

    prompt = SWOT_PROMPT.format(
        industry=research["industry"],
        business_model=research["business_model"],
        target_market=research["target_market"],
        competitors=json.dumps(
            competitors,
            indent=2
        )
    )

    response = llm.invoke(prompt)

    swot_data = extract_json(
        response.content
    )

    return {
        "swot_result": swot_data
    }