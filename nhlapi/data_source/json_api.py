#!/usr/bin/env python
import json
import os

class Api:
    def getTeams(self):
        return self.getJsonFromFile(os.path.abspath(os.path.dirname(__file__) + '/../data/team/teams.json'))

    def getNextGameDataForTeam(self, teamCode):
        return self.getJsonFromFile(os.path.abspath(os.path.dirname(__file__) + '/../data/team/team10.json'))

    def getLiveGameData(self, gameCode):
        return self.getJsonFromFile(os.path.abspath(os.path.dirname(__file__) + '/../data/game/team10-game.json'))

    def getJsonFromFile(self, fileName):
        with open(fileName) as json_data:
            d = json.load(json_data)
            return d