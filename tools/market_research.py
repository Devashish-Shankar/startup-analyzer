def get_market_data(industry):

    market_db = {

        "Environmental Technology": {
            "market_size": "$12B",
            "growth_rate": "12%"
        },

        "FinTech": {
            "market_size": "$180B",
            "growth_rate": "15%"
        },

        "HealthTech": {
            "market_size": "$250B",
            "growth_rate": "14%"
        },

        "EdTech": {
            "market_size": "$120B",
            "growth_rate": "13%"
        }
    }

    return market_db.get(
        industry,
        {
            "market_size": "Unknown",
            "growth_rate": "Unknown"
        }
    )