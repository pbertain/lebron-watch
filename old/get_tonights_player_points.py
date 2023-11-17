#!/usr/bin/env python3
# File name: get_tonights_player_points.py
# Description: return player points for tonights game
# Author: Paul Bertain
# Date: 2023-01-31
# Code template: python-script-template.py
# Source: https://github.com/swar/nba_api/blob/master/docs/examples/Basics.ipynb
# Additional: https://betterprogramming.pub/using-pythons-nba-api-to-create-a-simple-regression-model-ac9a3b36bc8

# First we will import our packages
## Get BoxScore
from nba_api.live.nba.endpoints import boxscore
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.static import players
from nba_api.stats.static import teams
import pandas as pd
import requests

def get_id(player_name):
    '''
    This module takes a full name and searches the NBA API for their ID
    '''
    name_to_find = player_name
    nba_players = players.get_players()
    #print(nba_players)
    get_player_data = [player for player in nba_players
                       if player['full_name'] == name_to_find][0]
    player_id   = get_player_data['id']
    return(player_id)

def get_game_id():
    team_abbr = 'POR'
    nba_teams = teams.get_teams()

    # Select the dictionary for the gsw, which contains their team ID
    team_to_check = [team for team in nba_teams if team['abbreviation'] == team_abbr][0]
    team_to_check_id = team_to_check['id']
    #team_to_check_id: 1610612754

    # Searching through the games and get the most recent team_to_check game_id
    # Query for the last regular season game where the team_to_check were playing

    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_to_check_id)
#                                                season_nullable=Season.default,
#                                                season_type_nullable=SeasonType.regular)
    games_dict    = gamefinder.get_normalized_dict()
    games         = games_dict['LeagueGameFinderResults']
    game          = games[0]
    game_id       = game['GAME_ID']

    # Get **all** the games so we can filter to an individual GAME_ID
    result = leaguegamefinder.LeagueGameFinder()
    all_games = result.get_data_frames()[0]
    # Find the game_id we want
    full_game = all_games[all_games.GAME_ID == game_id]
    return game_id

def player_score(the_player_id):
    # Getting Box Scores.
    # Note: home_team & away_team have the identicial data structure.
    box.game.get_dict()                    #equal to box.get_dict()['game']
    players_away = box.away_team.get_dict()['players']
    players_home = box.home_team.get_dict()['players']
#    f = "The Blazers were {loc} and {name} scored {points} PTS tonight"
    f = "{name} scored {points} PTS tonight"
    for player in players_away:
        if player['personId'] == the_player_id:
            location = 'away'
            print(f.format(loc=location,player_id=player['personId'],name=player['name'],points=player['statistics']['points']))
    for player in players_home:
        if player['personId'] == the_player_id:
            location = 'away'
            print(f.format(loc=location,player_id=player['personId'],name=player['name'],points=player['statistics']['points']))

playa_id = get_id('Damian Lillard')
gamer_id = get_game_id()
box = boxscore.BoxScore(gamer_id)
player_score(playa_id)


# Data Sets
#box.game.get_dict()                    #equal to box.get_dict()['game']
#box.away_team_player_stats.get_dict() #equal to box.get_dict()['game']['awayTeam']['players']
#box.home_team_player_stats.get_dict() #equal to box.get_dict()['game']['homeTeam']['players']

#box.game.get_dict()                    #equal to box.get_dict()['game']
#box.arena.get_dict()                  #equal to box.get_dict()['game']['arena']
#box.away_team.get_dict()              #equal to box.get_dict()['game']['awayTeam']
#box.away_team_player_stats.get_dict() #equal to box.get_dict()['game']['awayTeam']['players']
#box.away_team_stats.get_dict()        #equal to box.get_dict()['game']['homeTeam'] w/o ['players']
#box.home_team.get_dict()              #equal to box.get_dict()['game']['homeTeam']
#box.home_team_player_stats.get_dict() #equal to box.get_dict()['game']['homeTeam']['players']
#box.home_team_stats.get_dict()        #equal to box.get_dict()['game']['homeTeam'] w/o ['players']
#box.game_details.get_dict()           #equal to box.get_dict()['game'] scrubbed of all other dictionaries
#box.officials.get_dict()              #equal to box.get_dict()['game']['officials']box = boxscore.BoxScore(game_id)
