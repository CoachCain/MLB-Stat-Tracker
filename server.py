from flask import Flask, render_template
from teams import TeamData
from roster import Roster
from player_stats import PlayerStats
import statsapi

app = Flask(__name__)


TEAM_LOGOS = {
 
 133: 'images/athletics.png',
 134: 'images/pirates.png',
 135: 'images/padres.png', 
 136: 'images/mariners.png',
 137: 'images/giants.png',
 138: 'images/cardinals.png',
 139: 'images/rays.png',
 140: 'images/rangers.png',
 141: 'images/blue_jays.png',
 142: 'images/twins.png',
 143: 'images/phillies.png',
 144: 'images/braves.png',
 145: 'images/white_sox.png',
 146: 'images/marlins.png',
 147: 'images/yankees.png',
 158: 'images/brewers.png',
 108: 'images/angels.png',
 109: 'images/diamondbacks.png',
 110: 'images/orioles.png',
 111: 'images/red_sox.png',
 112: 'images/cubs.png',
 113: 'images/reds.png',
 114: 'images/indians.png',
 115: 'images/rockies.png',
 116: 'images/tigers.png',
 117: 'images/astros.png',
 118: 'images/royals.png',
 119: 'images/dodgers.png',
 120: 'images/nationals.png',
 121: 'images/mets.png'

}


@app.route('/')
def index():
    teams = TeamData()
    teams_list = teams.teams_list
    return render_template('index.html', teams=teams_list)

@app.route('/roster/<team_id>')
def show_roster(team_id):
    roster_data = Roster(team_id).look_up_roster()
    roster = [player.split() for player in roster_data.split('\n')]
    team_name = statsapi.lookup_team(team_id)[0]['name']
    team_logo = TEAM_LOGOS.get(int(team_id))
    return render_template('roster.html', roster=roster, team_name=team_name, team_logo=team_logo)

@app.route('/player_stats/<player_name>')
def show_player_stats(player_name):
    player = PlayerStats(player_name)
    player_statistics = player.get_player_stats()
    return render_template('player_stats.html',player_name=player_name, player_statistics=player_statistics)


if __name__ == "__main__":
    app.run(debug=True)

