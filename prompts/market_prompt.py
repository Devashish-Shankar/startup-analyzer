MARKET_PROMPT = """
You are a startup market analyst.

Analyze the startup profile.

Industry:
{industry}

Business Model:
{business_model}

Target Market:
{target_market}

Return ONLY valid JSON.

{{
    "market_size": "",
    "growth_rate": "",
    "opportunities": [],
    "risks": []
}}
"""