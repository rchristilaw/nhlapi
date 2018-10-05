#!/usr/bin/env python
import urllib2
import json
import time
import requests
# import platform


from constants import url_constants
from constants import team_constants
from services.team_service import TeamService
import api
import json_api



class NhlApi(object):
    def __init__(self, dataSource):
        self.dataSource = dataSource
        self.teamService = TeamService(self.dataSource)

    def getTeamsList(self):
        return self.teamService.getTeamsList()

    def getGame(self, teamName): 
        url = url_constants.NHL_API_BASE_URL + "api/v1/teams/" + teamName + "?expand=team.schedule.next"

        r = requests.get(url)
        nextGame = r.json()

        print nextGame

        return

        liveFeedUrl = nextGame['teams'][0]['nextGameSchedule']['dates'][0]['games'][0]['link']
        feedUrl = url_constants.NHL_API_BASE_URL + liveFeedUrl

        r = requests.get(feedUrl)
        gameData = r.json()

        print gameData

        # awayTeam = Team(gameData['gameData']['teams']['away'])
        # homeTeam = Team(gameData['gameData']['teams']['home'])
        # utcStartTime = gameData['gameData']['datetime']['dateTime']

    def testPrint(self):
        print self.test

    def readFromJson(self, fileName):
        with open(fileName) as json_data:
            d = json.load(json_data)
            print(d)

# Main function
if __name__ == "__main__":
    dataSource = json_api.Api()
    nhlapi = NhlApi(dataSource)
    # nhlapi.readFromJson('../data/teams.json')
    
    teams = nhlapi.getTeamsList()
    for team in teams:
        print team.getTeamName()
    # api.getGame("10")
