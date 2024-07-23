from enum import Enum

class SortOrder(Enum):
    ASCENDING = 'ascending'
    DESCENDING = 'descending'

def get_all_countries_(data, page: int = 1, page_size: int = 10):
    countries_list = sorted((data['country_name'].fillna('')).tolist())
    countries_length = len(countries_list)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    paginated_countries_list = countries_list[start_index:end_index]

    response_data = {
        "Number of Countries": countries_length,
        "Countries": paginated_countries_list,
        "Page": page,
        "Page Size": page_size,
        "Total Pages": (countries_length + page_size - 1) // page_size
    }

    return response_data


def get_all_languages_(data):
    languages_list = (data['languages'].fillna('')).tolist()
    
    unique_languages = set()
    for entry in languages_list:
        languages = entry.split(',')
        for language in languages:
            cleaned_language = language.strip()
            if cleaned_language:
                unique_languages.add(cleaned_language)

    unique_languages = sorted(unique_languages)

    languages_length = len(unique_languages)

    response_data = {
        "Number of Unique Languages": languages_length,
        "Languages": unique_languages
    }

    return response_data


def get_language_by_country_(data, country: str):
    countries_data = data[data['country_name'].fillna('').str.contains(country, case=False, na=False)]
    countries = countries_data['country_name'].unique().tolist()
    languages_list = countries_data['languages'].tolist()

    languages_length = len(languages_list)

    response_data = {
        "Number of Languages": languages_length,
        "Country": countries,
        "Languages": languages_list
    }

    return response_data


def get_countries_by_language_(data, language: str):
    countries_data = data[data['languages'].fillna('').str.contains(language)]

    countries_list = sorted(countries_data['country_name'].tolist())

    countries_length = len(countries_list)

    response_data = {
        "Language": language,
        "Number of Countries": countries_length,
        "Countries": countries_list
    }

    return response_data

def get_countries_with_multiple_languages_(data):
    languages_data = data[data['languages'].fillna('').str.contains(',')]
    countries_list = languages_data['country_name'].tolist()
    countries_length = len(countries_list)

    response_data = {}

    response_data['Total Number of Countries'] = countries_length

    for _, row in languages_data.iterrows():
        country_name = row['country_name']
        languages_list = [lang.strip() for lang in row['languages'].split(',')]
        count = len(languages_list)
        
        response_data[country_name] = {
            'languages': languages_list,
            'count': count
        }

    return response_data

def get_countries_by_currency_(data, currency: str):
    currency_data = data[data['currency_name'].fillna('').str.contains(currency)]
    countries_list = sorted(currency_data['country_name'].tolist())
    countries_length = len(countries_list)

    response_data = {
        "Currency": currency,
        "Number of Countries": countries_length,
        "Countries": countries_list
    }

    return response_data

def get_countries_by_region_(data, sub_region: str):
    countries_data = data[data['sub_region'].fillna('').str.contains(sub_region)]
    countries_list = sorted(countries_data['country_name'].tolist())
    countries_length = len(countries_list)

    response_data = {
        "Sub Region": sub_region,
        "Number of Countries": countries_length,
        "Countries": countries_list
    }

    return response_data

def get_countries_by_independence_(data, has_independence: bool):
    countries_data = data[data['independence'] == has_independence]
    countries_list = sorted(countries_data['country_name'].tolist())
    countries_length = len(countries_list)

    response_data = {
        "Has Independence": has_independence,
        "Number of Countries": countries_length,
        "Countries": countries_list
    }

    return response_data

def get_continent_country_counts_(data):
    continent_country_counts = {}

    for _, row in data.iterrows():
        continents = row['continent'].split(', ')
        
        for continent in continents:
            if continent in continent_country_counts:
                continent_country_counts[continent] += 1
            else:
                continent_country_counts[continent] = 1

    num_distinct_continents = len(continent_country_counts)
    
    response_data = {
        "Number of Distinct Continents": num_distinct_continents
    }

    sorted_continents = sorted(continent_country_counts.keys())
    
    for continent in sorted_continents:
        response_data[continent] = continent_country_counts[continent]
    
    return response_data

def get_country_by_week_start_(data, start_on_mon: bool):
    if start_on_mon:
        countries_data = data[data['startOfWeek'] == 'monday']
    else:
        countries_data = data[data['startOfWeek'] != 'monday']

    countries_list = sorted(countries_data['country_name'].tolist())
    countries_length = len(countries_list)

    response_data = {
        "Week Day Starts on Monday": start_on_mon,
        "Number of Countries": countries_length,
        "Countries": countries_list
    }

    return response_data

def get_country_by_un_membership_(data, is_un_member: bool):
    countries_data = data[data['united_nation_members'] == is_un_member]

    countries_list = sorted(countries_data['country_name'].tolist())
    countries_length = len(countries_list)

    response_data = {
        "Members of UN": is_un_member,
        "Number of Countries": countries_length,
        "Countries": countries_list
    }

    return response_data

def sort_continents_countries_(data, sort_item, sort_order=SortOrder.ASCENDING, countries_count=2):
    continent_country_populations = {}

    for _, row in data.iterrows():
        country_name = row['country_name']
        sort_col = row[sort_item]
        continents = row['continent'].split(', ')
        
        for continent in continents:
            if continent not in continent_country_populations:
                continent_country_populations[continent] = []
            continent_country_populations[continent].append((country_name, sort_col))
    
    result = {}
    
    for continent, countries in continent_country_populations.items():
        sorted_countries = sorted(countries, key=lambda x: x[1], reverse=(sort_order == SortOrder.DESCENDING))
        result[continent] = [{"country_name": country, sort_item: item} for country, item in sorted_countries[:countries_count]]
    
    sorted_result = {continent: result[continent] for continent in sorted(result.keys())}
    
    return sorted_result

def sort_countries_(data, sort_item, sort_order=SortOrder.ASCENDING, countries_count=2):
    if sort_order == SortOrder.ASCENDING:
        df_sorted = data.sort_values(by=sort_item, ascending=True)
    else:
        df_sorted = data.sort_values(by=sort_item, ascending=False)
    
    top = df_sorted.head(countries_count)
    
    result = {row["country_name"]: row[sort_item] for _, row in top.iterrows()}
    
    return result