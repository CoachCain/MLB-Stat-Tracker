import statsapi
import pandas as pd

class PlayerStats:
    def __init__(self, player) -> None:
        self.player = statsapi.lookup_player(player)
        self.player_id = self.player[0]['id']
        
    
    def get_player_stats(self):
        player_stats = statsapi.player_stat_data(self.player_id)
        return player_stats

        



# this class initializes a new player's stats with the player's name and also their associated ID number
# we pass that id to the get_player_stats() method and it returns their stats in json format

# EXAMPLE:
# player_stats = PlayerStats('Hunter Renfroe')
# print(player_stats.get_player_stats())
# we dont call data like this in the webpage, but this is an example of how you might use this class in a vaccuum.


# in the webpage, we pass in the player's name though the get_player_stats method, where their name is a url variable
# the link to that is first seen in the roster.html and then once we are taken to the url with the players name as 
# a parameter we use the .getitems() to return/render the data