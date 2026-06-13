def search_competitors(industry):

    competitor_db = {
        "Environmental Technology": [
            "Xylem",
            "Hach",
            "Aquamonix"
        ],

        "FinTech": [
            "Stripe",
            "PayPal",
            "Razorpay"
        ],

        "HealthTech": [
            "Practo",
            "Teladoc",
            "Healthify"
        ]
    }

    return competitor_db.get(
        industry,
        []
    )