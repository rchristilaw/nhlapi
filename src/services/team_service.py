from beans.team import Team

class TeamService(object):
    def __init__(self, dataSource):
        self.dataSource = dataSource
        self.teams = self.initTeamsList()

    def getTeamsList(self):
        return self.teams


    def initTeamsList(self):
        teamsData = self.dataSource.getTeams()
        teams = []
        for teamData in teamsData['teams']:
            teams.append(Team(teamData))
        
        return teams
