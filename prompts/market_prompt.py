MARKET_PROMPT = """
You are a startup market analyst.

Industry:
{industry}

Business Model:
{business_model}

Target Market:
{target_market}

Known Market Data:
{market_data}

Analyze the market.

Return ONLY valid JSON.

{{
    "market_summary": "",
    "opportunities": [],
    "risks": []
}}
"""