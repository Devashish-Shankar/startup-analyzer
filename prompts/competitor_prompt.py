COMPETITOR_PROMPT = """
You are a startup competitor analyst.

Startup Industry:
{industry}

Business Model:
{business_model}

Target Market:
{target_market}

Known Competitors:
{competitors}

Analyze competitors.

Return ONLY valid JSON.

{{
    "competitor_analysis": [
        {{
            "name": "",
            "strength": "",
            "weakness": ""
        }}
    ]
}}
"""