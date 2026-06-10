RESEARCH_PROMPT = """
You are an expert startup analyst.

Analyze the startup description.

Return ONLY valid JSON.

{{
    "industry": "",
    "business_model": "",
    "target_market": ""
}}

Startup Description:
{startup_description}
"""