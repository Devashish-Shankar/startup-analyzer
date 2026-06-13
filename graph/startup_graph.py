from typing import TypedDict, Dict, Any

from langgraph.graph import StateGraph, START, END

from agents.research_agent import research_agent
from agents.market_agent import market_agent
from agents.competitor_agent import competitor_agent
from agents.swot_agent import swot_agent
from agents.investment_agent import investment_agent
from agents.report_agent import report_agent

class StartupState(TypedDict):
    startup_name: str
    description: str

    research_result: Dict[str, Any]
    market_result: Dict[str, Any]
    competitor_result: Dict[str, Any]
    swot_result: Dict[str, Any]
    investment_result: Dict[str, Any]
    report_result: str


builder = StateGraph(StartupState)

builder.add_node(
    "research_agent",
    research_agent
)

builder.add_node(
    "market_agent",
    market_agent
)

builder.add_node(
    "competitor_agent",
    competitor_agent
)

builder.add_node(
    "swot_agent",
    swot_agent
)

builder.add_node(
    "investment_agent",
    investment_agent
)

builder.add_node(
    "report_agent",
    report_agent
)

builder.add_edge(
    START,
    "research_agent"
)

builder.add_edge(
    "research_agent",
    "market_agent"
)

builder.add_edge(
    "market_agent",
    "competitor_agent"
)

builder.add_edge(
    "competitor_agent",
    "swot_agent"
)

builder.add_edge(
    "swot_agent",
    "investment_agent"
)

builder.add_edge(
    "investment_agent",
    "report_agent"
)

builder.add_edge(
    "report_agent",
    END
)

graph = builder.compile()