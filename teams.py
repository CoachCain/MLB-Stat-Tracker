import statsapi

class TeamData:
    def __init__(self):
        # create empty list to append to
        self.teams_list = []
        # return all team data from the api
        self.teams = statsapi.lookup_team('')
        # call below method to get the team data we want
        self.get_team_data()
    
    def get_team_data(self):
        # loop through each team
        for team in self.teams:
            # create dictionary that will hold the values we want from the data returned fromm self.teams
            team_dict = {
                "team_ID": team["id"],
                "team_name": team["name"]
            }
            # append that data to our self.teams_list 
            self.teams_list.append(team_dict)



   # want to add a feature that renders the team's overall stats to the 
   # webpage this data will sit above the players on the active roster 
    
    def get_team_stats(self):
        pass
    













