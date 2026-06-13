from pprint import pprint
from pathlib import Path
from graph.startup_graph import graph
from utils.pdf_generator import generate_pdf

def main():

    startup_name = input(
    "Startup Name: "
    )

    description = input(
    "Startup Description: "
    )
    
    startup_input = {
        "startup_name": startup_name,
        "description": description
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

    print("\nSWOT Analysis:\n")

    pprint(
        result["swot_result"]
    )

    print("\nInvestment Analysis:\n")

    pprint(
        result["investment_result"]
    )

    print("\nREPORT\n")
    print(result["report_result"])

    # Save Report to reports folder # ---------------------------------
    reports_dir = Path("reports") 
    reports_dir.mkdir( exist_ok=True ) 
    report_path = reports_dir / "startup_report.md" 
    with open(
        report_path, 
        "w", 
        encoding="utf-8" 
    ) as file: 
        
        file.write( 
            result["report_result"] 
        ) 
    print( f"\nReport saved successfully: {report_path}" )
    pdf_path = reports_dir / "startup_report.pdf"

    generate_pdf(
        result["report_result"],
        str(pdf_path)
    )

    print(
        f"PDF saved successfully: {pdf_path}"
    )

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()