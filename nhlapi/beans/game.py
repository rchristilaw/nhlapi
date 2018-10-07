class Game(object):
    def __init__(self, awayTeam, homeTeam, startTime, feedUrl):
        self.awayTeam = awayTeam
        self.homeTeam = homeTeam
        self.startTime = startTime
        self.feedUrl = feedUrl
        self.currentTime = "20:00"
        self.period = ""
        self.hasChanges = False

    def getHomeTeam(self):
        return self.homeTeam

    def getAwayTeam(self):
        return self.awayTeam

    def getStartTime(self):
        return self.startTime

    def getFeedUrl(self):
        return self.feedUrl

    def getCurrentTime(self):
        return self.currentTime

    def setCurrentTime(self, time):
        self.currentTime = time

    def getPeriod(self):
        return self.period

    def setPeriod(self, period):
        self.period = period

    def getHasChanges(self):
        return self.hasChanges

    def setHasChanges(self, hasChanges):
        self.hasChanges = hasChanges

    
