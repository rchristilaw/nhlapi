class Team(object):
    def __init__(self, teamData):
        self.id = teamData['id']
        self.name = teamData['name']
        self.abbreviation = teamData['abbreviation']
        self.score = 0

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def getTeamName(self):
        return self.name

    def getId(self):
        return self.id

    def getAbbreviation(self):
        return self.abbreviation