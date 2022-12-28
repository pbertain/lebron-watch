import datetime

from nba_api.stats.static import teams

nba_teams = teams.get_teams()
# Select the dictionary for the Lakers, which contains their team ID
team = [team for team in nba_teams if team['abbreviation'] == 'LAL'][0]
team_name = team['full_name']
team_id = team['id']
#print("%s have ID = %d" % (team_name, team_id))
#nba_date = '12/26/2022'

#try:
#    datetime.datetime.strptime(nba_date,"%m/%d/%y")
#except ValueError as err:
#    print(err)

from nba_api.stats.endpoints import leaguegamefinder

# import only datetime class
from datetime import datetime

# current datetime
now = datetime.now()

current_date = now.date()
#current_date = '2022-12-25'
#print('Date:', current_date)


# Query for games where the Celtics were playing
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
# The first DataFrame of those returned is what we want.
games = gamefinder.get_data_frames()[0]
season_id = games.head(1)['SEASON_ID']
game_date = games.head(1)['GAME_DATE']
games_2223 = games[games.SEASON_ID.str[-4:] == '2022']
all_games = games_2223.head(1)
#print("SEASON_ID = %s\nGAME_DATE = %s\nALL_GAMES[1] = %s" % (season_id, game_date, all_games))
last_team_game = games_2223.sort_values('GAME_DATE').iloc[-1]
game_id = last_team_game.GAME_ID
true_game_date = last_team_game.GAME_DATE

#print(true_game_date)

sample_date = '2022-12-26'

true_date_fmt = datetime.strptime(true_game_date, '%Y-%m-%d')
sample_date_fmt = datetime.strptime(sample_date, '%Y-%m-%d')

if (true_date_fmt.date() == datetime.today().date()):
    print("The Lakers played today!")
else:
    print("The Lakers were off today.")

#if (sample_date_fmt.date() == datetime.today().date()):
#    print("Sample games match")
#else:
#    print("Another sample day")

#print("The latest game date is %s" % game_data)
#latest_game = games_1718[games_1718.MATCHUP.str.contains('TOR')]
#try:
#    latest_game = games_2223[games_2223.GAME_DATE.str.contains(current_date)]
#except:
#    latest_game = 'fail'
#if (latest_game == 'fail'):
#    print("Kareem lives on for another day")
#else:
#    print("Lebron is bringing it")
