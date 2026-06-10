SWOT_PROMPT = """
You are an expert startup strategy consultant.

Startup Profile:

Industry:
{industry}

Business Model:
{business_model}

Target Market:
{target_market}

Competitor Information:
{competitors}

Generate SWOT Analysis.

Return ONLY valid JSON.

{{
    "strengths": [],
    "weaknesses": [],
    "opportunities": [],
    "threats": []
}}
"""