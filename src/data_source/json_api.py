#!/usr/bin/env python
import json

class Api:
    def getTeams(self):
        return self.getJsonFromFile('../data/team/teams.json')

    def getNextGameDataForTeam(self, teamCode):
        return self.getJsonFromFile('../data/team/team10.json')

    def getLiveGameData(self, gameCode):
        return self.getJsonFromFile('../data/game/team10-game.json')

    def getJsonFromFile(self, fileName):
        with open(fileName) as json_data:
            d = json.load(json_data)
            return d