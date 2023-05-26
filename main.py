import pandas as pd
import requests as re
import config
import json
import argparse
import sys
import warnings
import datetime as dt
import shutil
import os
import numpy as np

from pandas.errors import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
warnings.simplefilter(action="ignore", category=FutureWarning)


class API:

    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'User-Agent': 'PostmanRuntime/7.29.2',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    def __init__(self, apiEndPoint, apiKey, json_body):
        self.apiEndPoint = apiEndPoint
        self.apiKey = apiKey
        self.json_body = json_body
        self.headers["apiKey"] = apiKey

    def __str__(self):
        return f"API Endpoint: {self.apiEndPoint}\nAPI Key: {self.apiKey}\nQuery:\n[{self.query}]\nVariables:\n[{self.variables}]"

    def fetch_data(self):
        res = re.post(
            url=self.apiEndPoint,
            headers=self.headers,
            json=self.json_body
        )
        if res.status_code == 200:
            print(res.text)
            return res.json()
        else:
            print("Failed calling API!")
            print(res.text)
            exit()


def searchAthlete(weapon, level, type, gender, season, country, name="", isTeam="false", isSearch="false", fetchPage=1):
    json_body = {
        "weapon": weapon,
        "level": level,
        "type": type,
        "gender": gender,
        "isTeam": isTeam,
        "isSearch": isSearch,
        "season": season,
        "name": name,
        "country": country,
        "fetchPage": fetchPage
    }
    api = API(config.APIsearchAthlete, config.dictAPIkey[config.APIsearchAthlete], json_body)
    res = api.fetch_data()

    return

def getAthletesByCountry(gender, country="SIN", isTeam="false", isSearch="true", name=""):
    json_body = {
        "gender": gender,
        "country": country,
        "isTeam": isTeam,
        "isSearch": isSearch,
        "name": name
    }
    api = API(config.APIgetAtheletesByCountry, config.dictAPIkey[config.APIgetAtheletesByCountry], json_body)
    res = api.fetch_data()
    return

def getResultsByCompetitionID(season, competitionID):
    json_body = {
        "season": season,
        "id": competitionID
    }
    api = API(config.APIgetResultsByCompetitionID, config.dictAPIkey[config.APIgetResultsByCompetitionID], json_body)
    res = api.fetch_data()
    return

def getRankingsByAthleteID(athleteID):
    return

def getCompetitions(gender, weapon, type, level, competitionCategory="", season="-1", status="passed", name="", fromDate="", toDate="", fetchPage = 1):
    json_body = {
        "name": name,
        "status": status,
        "gender": gender,
        "weapon": weapon,
        "type": type,
        "season": season,
        "level": level,
        "competitionCategory": competitionCategory,
        "fromDate": fromDate,
        "toDate": toDate,
        "fetchPage": fetchPage
    }
    print(json_body)
    api = API(config.APIgetCompetitions, config.dictAPIkey[config.APIgetCompetitions], json_body)
    res = api.fetch_data()
    print(res)
    return

def main():
    config.importAPIs()
    #searchAthlete(weapon="e", level="s", type="i", gender="m", season="2022", name="", country="", fetchPage=1)
    getCompetitions(gender=["m", "f"], weapon=["e", "f"], type=["i"], level="", competitionCategory="", season="-1", status="passed", name="", fromDate="", toDate="", fetchPage = 1)
    return

if __name__ == "__main__":
    main()