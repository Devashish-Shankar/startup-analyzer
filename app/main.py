from pprint import pprint
from pathlib import Path
from unittest import result

from services.analyzer_service import run_analysis
from utils.pdf_generator import generate_pdf

def main():
    
    print("\n" + "=" * 60)
    print("MULTI-AGENT STARTUP ANALYZER")
    print("=" * 60)

    startup_name = input(
        "\nStartup Name: "
    )

    description = input(
        "\nStartup Description: "
    )

    print("\nAnalyzing startup...\n")

    result = run_analysis(
        startup_name,
        description
    )

    if "error" in result:

        print(
            f"\nError: {result['error']}"
        )

        return

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

    if "market_sources" in result:

        print("\nMarket Sources:\n")

        for source in result["market_sources"]:

            print(
                f"- {source}"
            )

    print("\nCompetitor Analysis:\n")

    pprint(
        result["competitor_result"]
    )

    if "competitor_sources" in result:

        print("\nCompetitor Sources:\n")

        for source in result["competitor_sources"]:

            print(
                f"- {source}"
            )

    print("\nSWOT Analysis:\n")

    pprint(
        result["swot_result"]
    )

    print("\nInvestment Analysis:\n")

    pprint(
        result["investment_result"]
    )

    print("\nFINAL REPORT:\n")

    print(
        result["report_result"]
    )

    # -----------------------------
    # Create Reports Folder
    # -----------------------------

    reports_dir = Path(
        "reports"
    )

    reports_dir.mkdir(
        exist_ok=True
    )

    # -----------------------------
    # Save Markdown Report
    # -----------------------------

    report_path = (
        reports_dir /
        "startup_report.md"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            result["report_result"]
        )

    print(
        f"\n✅ Markdown report saved: {report_path}"
    )

    # -----------------------------
    # Save PDF Report
    # -----------------------------

    pdf_path = (
        reports_dir /
        "startup_report.pdf"
    )

    generate_pdf(
        result["report_result"],
        str(pdf_path)
    )

    print(
        f"✅ PDF report saved: {pdf_path}"
    )

    print("\n" + "=" * 60)
    print("Analysis Completed Successfully")
    print("=" * 60)

if __name__ == "__main__":
    main()
