from typing import TypedDict, Dict, Any

from langgraph.graph import StateGraph, START, END

from agents.research_agent import research_agent
from agents.market_agent import market_agent
from agents.competitor_agent import competitor_agent
from agents.swot_agent import swot_agent

class StartupState(TypedDict):
    startup_name: str
    description: str

    research_result: Dict[str, Any]
    market_result: Dict[str, Any]
    competitor_result: Dict[str, Any]
    swot_result: Dict[str, Any]


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
    END
)

graph = builder.compile()