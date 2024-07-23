# travel-agency-hackathon

## Table of Contents
- Overview
- Architecture
- [Project Structure]
- Prerequisites
- Setup Instructions
    - Setting up GCS Bucket
    - Creating a Service Account
    - Inserting your Configurations 
    - Creating the Cloud Function
    - Setting up BigQuery
- Transformation Logic
- Testing the Pipeline
- Testing the API Endpoint 
- Monitoring and Logging
- Analysis/ Insights
- Contributing
- License


## Overview
This project is a submission by team-3(Data Natives) for the DEC countries_information_ingestion hackathon where data is extracted from a REST API to a data lake, transformed and loaded into a data warehouse.


## Architecture


## Project Structure

- `utils`:
- `config.py`:
- `delpoy.sh`:
- `raw_data_loader.py`:
- `main.py`:
- `constants.sh`:
- `api`:
- `requirements.txt`:
- `Travel_Agency.ipynb`:


## Prerequisites
- Google Cloud Platform account
- Google Cloud SDK installed
- Python 3.10 or above installed

## Setup Instructions


### Setting up GCS Bucket

### Creating a Service Account


### Inserting your Configurations


### Setting up BigQuery


## Transformation Logic


## Testing the Pipeline

## Testing the API Endpoint  
A FastAPI implementation was included to perform inference on the loaded dataset to help answer the questions raised in the task's description.    
  
To start the API application, simply run the command below from the project parent directory.  
  
```BASH
python api/main.py
```  
  
This starts the application on port 8000, as shown in the screenshot below.  

![API Server Startup](./screenshots/api_server_startup.PNG)  
  
To access the endpoints from the browser, open the page `http://localhost:8000/docs` for the Swagger UI. This opens up a page similar to the image below.  
  
![Swagger UI](./screenshots/swagger_ui.PNG)  
  
You can test all the endpoints from the Swagger UI.

## Analysis/ Insights
The data was used to answer the following questions.

1. **How many countries speak french?**
    ```python
    # Filter for countries where 'languages' column contains 'French'

    french_speaking_countries = df[df['languages'].fillna('').str.contains('French')]

    # Display the results
    print("Number of countries that speak French:", len(french_speaking_countries))
Number of countries that speak French: 46

2. **How many countries speak English?**
   ```python
   # Filter for countries where 'languages' column contains 'English'

    english_speaking_countries = df[df['languages'].fillna('').str.contains('English')]

    # Display the results
    print("Number of countries that speak English:", len(english_speaking_countries))
Number of countries that speak English: 91

3. **How many countries have more than one official language?**
    ```python
   # Count countries with more than one official language
    more_than_one_offLan = df[df['languages'].fillna('').str.contains(',')]

    print("Number of countries with more that one official language:", len(more_than_one_offLan))
Number of countries with more that one official language: 96

4. **How many countries have the Euro as their official currency?**
   ```python
   # Count countries with Euro as official currency
    num_countries_with_euro = df[df['currency_name'] == 'Euro'].shape[0]

    # Display the results
    print("Number of countries with Euro as official currency:", num_countries_with_euro)
Number of countries with Euro as official currency: 36

5. **How many countries are from West Europe?**
   ```python
   # Count countries from west europe
    Countries_west_eur = df[df['sub_region'] == 'Western Europe']
    
    print("Number of countries from Western Europe:", len(Countries_west_eur))
Number of countries from Western Europe: 8

6. **How many countries have not gained Independence?**
   ```python
   # Filter countries that have not gained independence
    Countries_no_ind = df[df['independence'] == False]
                                                      
    print("Number of countries that have not gained independence:", len(Countries_no_ind))
Number of countries that have not gained independence: 55

7. **How many distinct continent and how many countries from each?**
   ```python
   # Aggregate to find number of countries per continent
    continent_counts = df.groupby('continent')['country_name'].agg(['count']).reset_index()
    
    continent_counts = continent_counts.rename(columns={'count': 'No of countries'})
    
    # Count distinct continents
    num_distinct_continents = len(continent_counts)
    
    # Display results
    print("Number of distinct continents:", num_distinct_continents)
    print("\nCountries per continent:")
    
    continent_counts
Number of distinct continents: 8
Countries per continent:
    | continent| No of countries | 
    |-----------------|-----------------|
    | Africa	 | 58|
    | Antarctica | 5|
    | Asia | 50|
    | Europe| 52|
    | Europe, Asia| 3|
    | North America| 41|
    | Oceania	 | 27|
    | South America| 14|

8. **No. of countries where the week does not start on Monday**
   ```python
   # Filter countries with startOfWeek not monday
    Country_week_start = df[df['startOfWeek'] != 'monday']
    
    print("Number of countries where the week does not start on Monday:", len(Country_week_start))
Number of countries where the week does not start on Monday: 21

9. **How many countries are not UN members?**
    ```python
    # Filter countries not UN members
    Country_notUN_members = df[df['united_nation_members'] != True]
    
    print("Number of countries that are not UN members:", len(Country_notUN_members))
Number of countries that are not UN members: 58

10. **How many countries are UN members?**
    ```python
    # Filter countries that are UN members
    Country_UN_members = df[df['united_nation_members'] == True]
    
    print("Number of countries that are UN members:", len(Country_UN_members))
Number of countries that are UN members: 192

11. **List 2 countries with the lowest population for each continent**
    ```python
    # Sort DataFrame by population within each continent
    df_sorted = df.sort_values(by=['continent', 'population'])
    
    # Group by continent and select top 2 countries with lowest population
    top_countries_per_continent = df_sorted.groupby('continent').head(2)
    
    # Display the results
    print("Two countries with lowest population for each continent:")
    top_countries_per_continent[['continent', 'country_name', 'population']].reset_index(drop = True)
Two countries with lowest population for each continent:

| Continent       | Country Name                            | Population |
|-----------------|-----------------------------------------|------------|
| Africa          | Saint Helena, Ascension and Tristan da Cunha | 53,192|
| Africa          | Seychelles                              | 98,462     |
| Antarctica      | Bouvet Island                           | 0          |
| Antarctica      | Heard Island and McDonald Islands       | 0          |
| Asia            | Cocos (Keeling) Islands                 | 544        |
| Asia            | Christmas Island                        | 2,072      |
| Europe          | Vatican City                            | 451        |
| Europe          | Svalbard and Jan Mayen                  | 2,562      |
| Europe, Asia    | Azerbaijan                              | 10,110,116 |
| Europe, Asia    | Turkey                                  | 84,339,067 |
| North America   | Saint Barthélemy                        | 4,255      |
| North America   | Montserrat                              | 4,922      |
| Oceania         | Pitcairn Islands                        | 56         |
| Oceania         | United States Minor Outlying Islands    | 300        |
| South America   | Falkland Islands                        | 2,563      |
| South America   | French Guiana                           | 254,541    |


12. **List 2 countries with the largest Area for each Continent**
    ```python
    # Sort DataFrame by population within each continent
    df_sorted = df.sort_values(by=['continent', 'area'], ascending= [True, False])
    
    # Group by continent and select 2 countries with Largest Area
    countries_per_continent = df_sorted.groupby('continent').head(2)
    
    # Display the results
    print("Two countries with largest area for each continent:")
    countries_per_continent[['continent', 'country_name', 'area']].reset_index(drop=True)
  Two countries with lowest population for each continent:

| Continent       | Country Name                              | Area         |
|-----------------|-------------------------------------------|--------------|
| Africa          | Algeria                                   | 2,381,741    |
| Africa          | DR Congo                                  | 2,344,858    |
| Antarctica      | Antarctica                                | 14,000,000   |
| Antarctica      | French Southern and Antarctic Lands       | 7,747        |
| Asia            | China                                     | 9,706,961    |
| Asia            | India                                     | 3,287,590    |
| Europe          | Ukraine                                   | 603,500      |
| Europe          | France                                    | 551,695      |
| Europe, Asia    | Russia                                    | 17,098,242   |
| Europe, Asia    | Turkey                                    | 783,562      |
| North America   | Canada                                    | 9,984,670    |
| North America   | United States                             | 9,372,610    |
| Oceania         | Australia                                 | 7,692,024    |
| Oceania         | Papua New Guinea                          | 462,840      |
| South America   | Brazil                                    | 8,515,767    |
| South America   | Argentina                                 | 2,780,400    |


13. **Top 5 countries with the Largest Area**
    ```python
    # Sort the DataFrame by 'Area' column in descending order and select top 5
    top_5_countries = df.nlargest(5, 'area').reset_index()
    
    # Result
    print('Top 5 countries with the largest Area:')
    top_5_countries[['country_name', 'area']]
Top 5 countries with the largest Area:

| Country Name         | Area         |
|----------------------|--------------|
| Russia               | 17,098,242   |
| Antarctica           | 14,000,000   |
| Canada               | 9,984,670    |
| China                | 9,706,961    |
| United States        | 9,372,610    |

14. **Top 5 countries with the lowest Area**
    ```python
    # Sort the DataFrame by 'Area' column in ascending order and select bottom 5
    bottom_5_countries = df.nsmallest(5, 'area').reset_index()
    
    print('Top 5 countries with the lowest Area:')
    bottom_5_countries[['country_name', 'area']]
Top 5 countries with the lowest Area:

| Country Name               | Area   |
|----------------------------|--------|
| Vatican City               | 0.44   |
| Monaco                     | 2.02   |
| Gibraltar                  | 6.00   |
| Tokelau                    | 12.00  |
| Cocos (Keeling) Islands    | 14.00  |



## Contributing

## License 
