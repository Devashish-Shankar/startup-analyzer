COMPETITOR_PROMPT = """
You are a startup competitor analyst.

Analyze the startup profile.

Industry:
{industry}

Business Model:
{business_model}

Target Market:
{target_market}

Identify top competitors.

Return ONLY valid JSON.

{{
    "competitors": [
        {{
            "name": "",
            "description": "",
            "strength": ""
        }}
    ]
}}
"""