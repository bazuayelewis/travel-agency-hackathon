import pandas as pd
import logging


def _transformation(country_data) -> list:
    flattened_countries = []

    for country in country_data:

        country_code = None
        if "idd" in country:
            idd = country["idd"]
            if "root" in idd and "suffixes" in idd:
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

        common_native_name = None
        if "name" in country:
            names = country['name']
            if 'nativeName' in names:
                native_names = names['nativeName']
                common_native_name = ", ".join(
                [v["common"] for v in native_names.values()]
                )

        flattened_country = {
            "country_name": country["name"]["common"],
            "independence": country.get("independent", None),
            "united_nation_members": country.get("unMember", None),
            "startOfWeek": country.get("startOfWeek", None),
            "official_country_name": country["name"]["official"],
            "common_native_name": common_native_name,
            "currency_code": currency_codes,
            "currency_name": currency_names,
            "currency_symbol": currency_symbols,
            "country_code": country_code,
            "capital": country_capitals,
            "region": country.get("region", None),
            "sub_region": country.get("subregion", None),
            "languages": country_languages,
            "area": country.get("area", None),
            "population": country.get("population", None),
            "continent": country_continents
        }
        flattened_countries.append(flattened_country)

    return flattened_countries


def extract_countries_data(country_data):
    flattened_data = _transformation(country_data)
    data_df = pd.DataFrame(flattened_data)
    logging.info(f"{len(data_df)} records in dataframe!")
    return data_df