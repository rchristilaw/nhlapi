from beans.team import Team
from beans.game import Game
from beans.live_game_data import LiveGameData
from util import time_util

class GameService(object):
    def __init__(self, dataSource):
        self.dataSource = dataSource

    def getNextGameFeedUrlForTeam(self, team):
        nextGame = self.dataSource.getNextGameDataForTeam(team.getId())
        
        feedUrl = nextGame['teams'][0]['nextGameSchedule']['dates'][0]['games'][0]['link']
        return feedUrl

    def getNextGameForTeam(self, team):
        feedUrl = self.getNextGameFeedUrlForTeam(team)

        gameData = self.dataSource.getLiveGameData(feedUrl)

        awayTeam = Team(gameData['gameData']['teams']['away'])
        homeTeam = Team(gameData['gameData']['teams']['home'])
        utcStartTime = gameData['gameData']['datetime']['dateTime']

        return Game(awayTeam, homeTeam, time_util.convertToUtcDatetime(utcStartTime), feedUrl)

    def updateGame(self, game):

        if (time_util.isBeforeCurrentTime(game.getStartTime()) is False):
            print("Game Hasnt started")
            return game

        gamedata = LiveGameData(self.dataSource.getLiveGameData(game.getFeedUrl()))
                    
        homeScore = gamedata.getHomeScore()
        awayScore = gamedata.getAwayScore()

        period = gamedata.getCurrentPeriod()
        periodTimeRemaining = gamedata.getPeriodTimeRemaining()

        if (awayScore != game.getAwayTeam().getScore()):
            game.getAwayTeam().setScore(awayScore)
            game.setHasChanges(True)

        if (homeScore != game.getHomeTeam().getScore()):
            game.getHomeTeam().setScore(homeScore)
            game.setHasChanges(True)
            
        
        if (period is not None and game.getCurrentTime() != periodTimeRemaining):
            game.setCurrentTime(periodTimeRemaining)
            game.setHasChanges(True)

        return game
        
        