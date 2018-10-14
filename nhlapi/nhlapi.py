#!/usr/bin/env python

from services.team_service import TeamService
from services.game_service import GameService
from data_source import api
from data_source import json_api

import time



class NhlApi(object):
    def __init__(self):
        dataSource = json_api.Api()
        self.dataSource = dataSource
        self.teamService = TeamService(self.dataSource)
        self.gameService = GameService(self.dataSource)

    def getTeamsList(self):
        return self.teamService.getTeamsList()

    def getNextGameForTeam(self, abbrev):
        team = self.teamService.getTeamByAbbreviation(abbrev)
        return self.gameService.getNextGameForTeam(team)

    def getUpdatedGame(self, game):
        return self.gameService.updateGame(game)

    def getTodaysGames(self):
        return self.gameService.getTodaysGames()


# Main function
if __name__ == "__main__":
    
    # nhlapi = NhlApi(dataSource)


    
    # teams = nhlapi.getTeamsList()
    # for team in teams:
    #     print team.getTeamName()

    game = nhlapi.getNextGameForTeam("TOR")
    print(game.getStartTime())

    i = 0
    while (i < 8):
        game = nhlapi.getUpdatedGame(game)

        if (game.getHasChanges()):
            print(game.getHomeTeam().getScore())
            game.setHasChanges(False)
        time.sleep(5)
        i += 1
