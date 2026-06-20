from graph.startup_graph import graph

def run_analysis(
startup_name,
description
):
    try:

        startup_input = {
            "startup_name": startup_name,
            "description": description
        }

        result = graph.invoke(
            startup_input
        )

        return result

    except Exception as e:

        print(
            f"\nAnalysis Error: {e}\n"
        )

        return {
            "error": str(e)
        }
