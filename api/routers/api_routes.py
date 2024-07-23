from fastapi import APIRouter, Query
from data.countries_data import read_data
from dependencies.countries import SortOrder
from dependencies.countries import (get_all_countries_, get_countries_by_language_, get_all_languages_, get_language_by_country_, 
                                    get_countries_with_multiple_languages_, get_countries_by_currency_, get_countries_by_region_,
                                    get_countries_by_independence_, get_continent_country_counts_, get_country_by_week_start_,
                                    get_country_by_un_membership_, sort_continents_countries_, sort_countries_)

router = APIRouter()

data_path_ = './api/data/data.csv'

@router.get("/countries")
def get_all_countries(page: int = Query(1, alias="page", ge=1), page_size: int = Query(10, alias="page_size", ge=1)):
    data_path = data_path_
    data = read_data(data_path)
    return get_all_countries_(data, page, page_size)

@router.get("/countries/language")
def get_countries_by_languange(language: str = Query('English', alias="language")):
    data_path = data_path_
    data = read_data(data_path)
    return get_countries_by_language_(data, language)

@router.get("/languages")
def get_all_languages():
    data_path = data_path_
    data = read_data(data_path)
    return get_all_languages_(data)

@router.get("/languages/country")
def get_language_by_country(country: str = Query('Nigeria', alias="country")):
    data_path = data_path_
    data = read_data(data_path)
    return get_language_by_country_(data, country)

@router.get("/country/multi_languages")
def get_countries_with_multiple_languages():
    data_path = data_path_
    data = read_data(data_path)
    return get_countries_with_multiple_languages_(data)

@router.get("/country/currency")
def get_countries_by_currency(currency_name: str = Query('Euro', alias="currency_name")):
    data_path = data_path_
    data = read_data(data_path)
    return get_countries_by_currency_(data, currency_name)

@router.get("/country/sub_region")
def get_countries_by_region(sub_region: str = Query('Western Europe', alias='sub_region')):
    data_path = data_path_
    data = read_data(data_path)
    return get_countries_by_region_(data, sub_region)

@router.get("/country/independence")
def get_countries_by_independence(has_independence: bool = Query(False, alias='has_independence')):
    data_path = data_path_
    data = read_data(data_path)
    return get_countries_by_independence_(data, has_independence)

@router.get("/continent/country/count")
def get_continent_country_counts():
    data_path = data_path_
    data = read_data(data_path)
    return get_continent_country_counts_(data)

@router.get("/country/week_start")
def get_country_by_week_start(start_on_mon: bool = Query(False, alias='week_start_on_mon')):
    data_path = data_path_
    data = read_data(data_path)
    return get_country_by_week_start_(data, start_on_mon)

@router.get("/country/un_membership")
def get_country_by_un_membership(is_un_member: bool = Query(False, alias='is_un_member')):
    data_path = data_path_
    data = read_data(data_path)
    return get_country_by_un_membership_(data, is_un_member)

@router.get("/continent/sort/countries")
def sort_continents_countries(sort_order: SortOrder = Query(SortOrder.ASCENDING, alias='sort_order'), 
                              sort_column: str = Query('population', alias='sort_column'),
                              countries_count: int = Query(2, alias='countries_count')):
    data_path = data_path_
    data = read_data(data_path)
    return sort_continents_countries_(data, sort_column, sort_order, countries_count)

@router.get("/countries/sort")
def sort_countries(sort_order: SortOrder = Query(SortOrder.ASCENDING, alias='sort_order'), 
                              sort_column: str = Query('population', alias='sort_column'),
                              countries_count: int = Query(2, alias='countries_count')):
    data_path = data_path_
    data = read_data(data_path)
    return sort_countries_(data, sort_column, sort_order, countries_count)