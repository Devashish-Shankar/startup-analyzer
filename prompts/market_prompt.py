MARKET_PROMPT = """
You are a market research analyst.

Industry:
{industry}

Research Data:
{market_research}

Analyze:

1. Market Size
2. Growth Rate
3. Opportunities
4. Risks

Return ONLY JSON.

{{
    "market_size": "",
    "growth_rate": "",
    "market_summary": "",
    "opportunities": [],
    "risks": []
}}
"""