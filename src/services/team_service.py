from beans.team import Team

class TeamService(object):
    def __init__(self, dataSource):
        self.dataSource = dataSource
        self.teams = self.initTeamsList()

    def initTeamsList(self):
        teamsData = self.dataSource.getTeams()
        teams = []
        for teamData in teamsData['teams']:
            teams.append(Team(teamData))
        
        return teams

    def getTeamsList(self):
        return self.teams

    def getTeamByAbbreviation(self, abbreviation):
        return next((team for team in self.teams if team.getAbbreviation() == abbreviation), None)
        
