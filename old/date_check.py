from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from datetime import datetime

nba_teams = teams.get_teams()
# Select the dictionary for the Lakers, which contains their team ID
team = [team for team in nba_teams if team['abbreviation'] == 'POR'][0]
team_name = team['full_name']
team_id = team['id']

# current datetime
now = datetime.now()

current_date = now.date()

# Query for games where the team was playing
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
# The first DataFrame of those returned is what we want.
games = gamefinder.get_data_frames()[0]
season_id = games.head(1)['SEASON_ID']
game_date = games.head(1)['GAME_DATE']
games_2223 = games[games.SEASON_ID.str[-4:] == '2022']
all_games = games_2223.head(1)
last_team_game = games_2223.sort_values('GAME_DATE').iloc[-1]
game_id = last_team_game.GAME_ID
true_game_date = last_team_game.GAME_DATE

true_date_fmt = datetime.strptime(true_game_date, '%Y-%m-%d')

if (true_date_fmt.date() == datetime.today().date()):
    print("the Blazers played today!")
else:
    print("Rip City was off today.")
