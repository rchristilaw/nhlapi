class Team(object):
    def __init__(self, teamData):
        self.id = teamData['id']
        self.city = teamData['locationName']
        self.nickName = teamData['teamName']
        self.abbreviation = teamData['abbreviation']

    def getTeamName(self):
        return self.city + " " + self.nickName

    def getId(self):
        return self.id

    def getAbbreviation(self):
        return self.abbreviation