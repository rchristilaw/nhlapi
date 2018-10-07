class LiveGameData(object):
    def __init__(self, gameJson):
        self.homeScore = gameJson['liveData']['linescore']['teams']['home']['goals']
        self.awayScore = gameJson['liveData']['linescore']['teams']['away']['goals']
        
        periodData = gameJson['liveData']['linescore']

        if 'currentPeriodOrdinal' in periodData:
            self.currentPeriod = periodData['currentPeriodOrdinal']
        else:
            self.currentPeriod = None

        if 'currentPeriodTimeRemaining' in periodData:
            self.periodTimeRemaining = periodData['currentPeriodTimeRemaining']
        else:
            self.periodTimeRemaining = None

    def getHomeScore(self):
        return self.homeScore

    def getAwayScore(self):
        return self.awayScore

    def getCurrentPeriod(self):
        return self.currentPeriod

    def getPeriodTimeRemaining(self):
        return self.periodTimeRemaining  