from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season
from nba_api.stats.library.parameters import SeasonType

nba_teams = teams.get_teams()

team_abbr = 'POR'

# Select the dictionary for the team_abbr team, which contains their team ID
team_to_check = [team for team in nba_teams if team['abbreviation'] == team_abbr][0]
#Get the team_to_check team_id
team_to_check_id = team_to_check['id']


# Searching through the games and get the most recent team_to_check game_id
# Query for the last regular season game where the team_to_check were playing
gamefinder    = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_to_check_id,
                            season_nullable=Season.default,
                            season_type_nullable=SeasonType.regular)
games_dict    = gamefinder.get_normalized_dict()
games         = games_dict['LeagueGameFinderResults']
game          = games[0]
game_id       = game['GAME_ID']
game_matchup  = game['MATCHUP']

# Get **all** the games so we can filter to an individual GAME_ID
result = leaguegamefinder.LeagueGameFinder()
all_games = result.get_data_frames()[0]
# Find the game_id we want
full_game = all_games[all_games.GAME_ID == game_id]

import pandas as pd

def combine_team_games(df, keep_method='home'):
    '''Combine a TEAM_ID-GAME_ID unique table into rows by game. Slow.

        Parameters
        ----------
        df : Input DataFrame.
        keep_method : {'home', 'away', 'winner', 'loser', ``None``}, default 'home'
            - 'home' : Keep rows where TEAM_A is the home team.
            - 'away' : Keep rows where TEAM_A is the away team.
            - 'winner' : Keep rows where TEAM_A is the losing team.
            - 'loser' : Keep rows where TEAM_A is the winning team.
            - ``None`` : Keep all rows. Will result in an output DataFrame the same
                length as the input DataFrame.

        Returns
        -------
        result : DataFrame
    '''
    # Join every row to all others with the same game ID.
    joined = pd.merge(df, df, suffixes=['_A', '_B'],
                      on=['SEASON_ID', 'GAME_ID', 'GAME_DATE'])
    # Filter out any row that is joined to itself.
    result = joined[joined.TEAM_ID_A != joined.TEAM_ID_B]
    # Take action based on the keep_method flag.
    if keep_method is None:
        # Return all the rows.
        pass
    elif keep_method.lower() == 'home':
        # Keep rows where TEAM_A is the home team.
        result = result[result.MATCHUP_A.str.contains(' vs. ')]
    elif keep_method.lower() == 'away':
        # Keep rows where TEAM_A is the away team.
        result = result[result.MATCHUP_A.str.contains(' @ ')]
    elif keep_method.lower() == 'winner':
        result = result[result.WL_A == 'W']
    elif keep_method.lower() == 'loser':
        result = result[result.WL_A == 'L']
    else:
        raise ValueError(f'Invalid keep_method: {keep_method}')
    return result

# Combine the game rows into one. By default, the home team will be TEAM_A.
game_df = combine_team_games(full_game)

team_a_abbr = game_df['TEAM_ABBREVIATION_A'].values[0]
team_a_score = game_df['PTS_A'].values[0]

team_b_abbr = game_df['TEAM_ABBREVIATION_B'].values[0]
team_b_score = game_df['PTS_B'].values[0]
if (team_a_score > team_b_score):
    print ("%s beats %s [%d - %d]" % (team_a_abbr, team_b_abbr, team_a_score, team_b_score))
else:
    print ("%s beats %s [%d - %d]" % (team_b_abbr, team_a_abbr, team_b_score, team_a_score))
