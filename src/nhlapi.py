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

    def getTeam(self, abbreviation):
        return self.teamService.getNextGameForTeam(abbreviation)


# Main function
if __name__ == "__main__":
    dataSource = json_api.Api()
    nhlapi = NhlApi(dataSource)
    
    # teams = nhlapi.getTeamsList()
    # for team in teams:
    #     print team.getTeamName()

    print nhlapi.getTeam("DET")
    # api.getGame("10")
