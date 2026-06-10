import json
import re

from services.llm_service import get_llm
from prompts.research_prompt import RESEARCH_PROMPT


def extract_json(text):

    match = re.search(
        r"```json\s*(.*?)\s*```",
        text,
        re.DOTALL
    )

    if match:
        return json.loads(match.group(1))

    return json.loads(text)


def research_agent(state):

    llm = get_llm()

    prompt = RESEARCH_PROMPT.format(
        startup_description=state["description"]
    )

    response = llm.invoke(prompt)

    data = extract_json(response.content)

    normalized_data = {
        "industry": data.get("industry") or data.get("Industry"),
        "business_model": data.get("business_model") or data.get("Business Model"),
        "target_market": data.get("target_market") or data.get("Target Market")
    }

    return {
        "research_result": normalized_data
    }