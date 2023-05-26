import time
now = time.strftime("%H%M%S", time.localtime())

# filename = now + ".xlsx"
scrappedRawFileName = "scrappedRawResults.xlsx"

# filename = "finalFilteredCleanedResults_" + now + ".xlsx"
finalFilteredCleanedFileName = "finalFilteredCleanedResults.xlsx"

# This file will be used For filtering names from scrapped cleaned data.
namelistFileName = "namelist.csv"

# This is where all files will be compiled to if compiled switch was provided as CLI argument.
compiledFolderName = "Filtered"

# Define disciplines to scrape
disciplines_list = [
    "100 Metres",
    "Pole Vault",
    "200 Metres",
    "1500 Metres"
]

# Define Countries to get results from
countries_list = [
    "Singapore",
    "Philippines",
    "Malaysia",
    "Vietnam",
    "Indonesia",
    "Thailand",
    "Myanmar",
    "Cambodia",
    "Laos",
    "Brunei",
    "Timor Leste",
]

# Define which years to get results for
years_list = [
    2019,
    2020,
    2021,
    2022,
    2023,
]


import json

def importAPIs(apiJSONfile="api.json"):
    global APIsearchAthlete
    global APIgetAtheletesByCountry
    global APIgetResultsByCompetitionID
    global APIgetCompetitions

    global dictAPIkey
    global dictAPIMethod

    apiJSONdata = json.load(open(apiJSONfile))
    APIsearchAthlete = apiJSONdata['apiEndPoint_searchAthlete']
    APIgetAtheletesByCountry= apiJSONdata['apiEndPoint_getAthletesByCountry']
    APIgetResultsByCompetitionID = apiJSONdata['apiEndPoint_getResultsByCompetitionID']
    APIgetCompetitions = apiJSONdata['apiEndPoint_getCompetitions']

    dictAPIkey = {}
    dictAPIkey[APIsearchAthlete] = ""
    dictAPIkey[APIgetAtheletesByCountry] = ""
    dictAPIkey[APIgetResultsByCompetitionID] = ""
    dictAPIkey[APIgetCompetitions] = ""

    dictAPIMethod = {}
    dictAPIMethod[APIsearchAthlete] = "POST"
    dictAPIMethod[APIgetAtheletesByCountry] = "POST"
    dictAPIMethod[APIgetResultsByCompetitionID] = "POST"
    dictAPIMethod[APIgetCompetitions] = "POST"

    return