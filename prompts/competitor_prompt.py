COMPETITOR_PROMPT = """
You are a startup competitor analyst.

Startup Industry:
{industry}

Business Model:
{business_model}

Target Market:
{target_market}

Competitor Research:
{competitor_research}

Analyze competitors and identify:

1. Top competitors
2. Their strengths
3. Their weaknesses
4. Competitive threats

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