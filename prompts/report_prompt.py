REPORT_PROMPT = """
You are a professional startup consultant.

Create a professional startup analysis report using the provided data.

Research Data:
{research}

Market Analysis:
{market}

Market Sources:
{market_sources}

Competitor Analysis:
{competitors}

Competitor Sources:
{competitor_sources}

SWOT Analysis:
{swot}

Investment Analysis:
{investment}

Generate a detailed report in MARKDOWN format.

The report must contain the following sections:

# Startup Analysis Report

## Startup Overview

* Industry
* Business Model
* Target Market

## Market Analysis

* Market Size
* Growth Rate
* Market Summary
* Opportunities
* Risks

## Competitor Analysis

* Major Competitors
* Competitor Strengths
* Competitor Weaknesses
* Competitive Threats

## SWOT Analysis

### Strengths

### Weaknesses

### Opportunities

### Threats

## Investment Recommendation

* Investment Score
* Risk Score
* Recommendation
* Reasoning

## Sources

### Market Research Sources

List all market source URLs.

### Competitor Research Sources

List all competitor source URLs.

IMPORTANT:

* Use professional consulting style.
* Use markdown headings and bullet points.
* Keep the report structured and readable.
* Do not output JSON.
  """