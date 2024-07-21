import pandas as pd

def flatten_country_data(countries):
    flattened_countries = []

    for country in countries:

        country_code = None
        if "idd" in country:
            idd = country["idd"]
            if "root" in idd and "suffixes" in idd and len(idd["suffixes"]) > 0:
                country_code = ", ".join([idd["root"] + suffix for suffix in idd["suffixes"]])
            elif "root" in idd:
                country_code = idd["root"]

        country_continents = None
        if "continents" in country:
            country_continents = ", ".join(country["continents"])

        currency_codes = None
        currency_names = None
        currency_symbols = None
        if "currencies" in country:
            currency_codes = ', '.join(country["currencies"].keys())
            currency_names = ', '.join([currency["name"] for currency in country["currencies"].values()])
            currency_symbols = ', '.join([currency["symbol"] for currency in country["currencies"].values()])

        country_capitals = None
        if "capital" in country:
            country_capitals = ', '.join(country["capital"])

        country_languages = None
        if "languages" in country:
            country_languages = ', '.join(country["languages"].values())

        common_native_name = country["name"]["nativeName"]["eng"]["common"] if "nativeName" in country and \
                             "eng" in country["name"]["nativeName"] else None

        flattened_country = {
            "Country name": country["name"]["common"],
            "Independence": country.get("independent", None),
            "United Nation members": country.get("unMember", None),
            "startOfWeek": country.get("startOfWeek", None),
            "Official country name": country["name"]["official"],
            "Common native name": common_native_name,
            "Currency code": currency_codes,
            "Currency name": currency_names,
            "Currency symbol": currency_symbols,
            "Country code": country_code,
            "Capital": country_capitals,
            "Region": country.get("region", None),
            "Sub region": country.get("subregion", None),
            "Languages": country_languages,
            "Area": country.get("area", None),
            "Population": country.get("population", None),
            "Continent": country_continents
        }
        flattened_countries.append(flattened_country)

    return flattened_countries


def extract_countries_data(countries):
    flattened_data = flatten_country_data(countries)
    
    data_df = pd.DataFrame(flattened_data)

    data_df.to_csv('data.csv', index=False)

    return data_df