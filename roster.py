import statsapi


# class simply takes a team id and returns that teams active roster
# i.e roster = Roster(team_lookup) -> roster.look_up_roster()
# in the above ^ team_lookup = an input that allows you to change the team ID you want
# we are no longer using input for team lookup but the concept remains the same

class Roster:
    def __init__(self, id) -> None:
      self.id = id

    def look_up_roster(self):
      return statsapi.roster(self.id)



