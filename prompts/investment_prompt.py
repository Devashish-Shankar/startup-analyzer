INVESTMENT_PROMPT = """
You are a venture capital analyst.

Analyze the startup using:

Research Data:
{research}

Market Data:
{market}

Competitor Data:
{competitors}

SWOT Data:
{swot}

Return ONLY valid JSON.

{{
    "investment_score": 0,
    "risk_score": 0,
    "recommendation": "",
    "reasoning": ""
}}
"""