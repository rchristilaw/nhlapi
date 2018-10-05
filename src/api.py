#!/usr/bin/env python
import requests
import json

from constants import url_constants


class Api:
    def getTeams(self):
        url = url_constants.NHL_API_BASE_URL + "api/v1/teams/"
        return self.requestData(url)


    def getNextGame(self, teamCode):
        url = url_constants.NHL_API_BASE_URL + "api/v1/teams/" + teamCode + "?expand=team.schedule.next"
        return self.requestData(url)
        

    def requestData(self, url):
        r = requests.get(url)
        return r.json()
        