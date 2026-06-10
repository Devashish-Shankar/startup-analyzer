from pprint import pprint

from graph.startup_graph import graph


def main():

    startup_input = {
        "startup_name": "EcoWater AI",
        "description": (
            "AI-powered water quality monitoring platform "
            "for municipalities and government agencies"
        )
    }

    result = graph.invoke(
        startup_input
    )

    print("\n" + "=" * 60)
    print("STARTUP ANALYSIS REPORT")
    print("=" * 60)

    print("\nResearch Analysis:\n")

    pprint(
        result["research_result"]
    )

    print("\nMarket Analysis:\n")

    pprint(
        result["market_result"]
    )

    print("\nCompetitor Analysis:\n")
    
    pprint(
        result["competitor_result"]
    )

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()