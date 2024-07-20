import pandas as pd

def flatten_country_data(countries):
    flattened_countries = []

    for country in countries:
        flattened_country = {
            "Country name": country["name"]["common"],
            "Independence": country.get("independent", None),
            "United Nation members": country.get("unMember", None),
            "startOfWeek": country.get("startOfWeek", None),
            "Official country name": country["name"]["official"],
            "Common native name": country["name"]["nativeName"]["eng"]["common"] if "nativeName" in country and "eng" in country["name"]["nativeName"] else None,
            "Currency code": list(country["currencies"].keys())[0] if "currencies" in country else None,
            "Currency name": list(country["currencies"].values())[0]["name"] if "currencies" in country else None,
            "Currency symbol": list(country["currencies"].values())[0]["symbol"] if "currencies" in country else None,
            # "Country code": country["idd"]["root"] + country["idd"]["suffixes"][0] if "idd" in country else None,
            "Capital": country["capital"][0] if "capital" in country else None,
            "Region": country.get("region", None),
            "Sub region": country.get("subregion", None),
            "Languages": ", ".join(list(country["languages"].values())) if "languages" in country else None,
            "Area": country.get("area", None),
            "Population": country.get("population", None),
            "Continent": country["continents"][0] if "continents" in country else None
        }
        flattened_countries.append(flattened_country)

    return flattened_countries


def extract_countries_data(countries):
    flattened_data = flatten_country_data(countries)
    
    data_df = pd.DataFrame(flattened_data)

    return data_df