#!/usr/bin/env python3
# File name: get_player_points.py
# Description: return player career points
# Author: Paul Bertain
# Date: 2022-12-21
# Code template: python-script-template.py
# Source: https://github.com/swar/nba_api/blob/master/docs/examples/Basics.ipynb
# Additional: https://betterprogramming.pub/using-pythons-nba-api-to-create-a-simple-regression-model-ac9a3b36bc8

# First we will import our packages
from nba_api.stats.endpoints import playercareerstats
import pandas as pd
import requests

def get_points(nba_id):
    '''
    This module takes an ID of a player and returns their career points
    '''
    player_career = playercareerstats.PlayerCareerStats(player_id=nba_id)
    career_stats = player_career.get_data_frames()[0]
    player_stats_dataframe = pd.DataFrame(career_stats)
    total_points = player_stats_dataframe["PTS"].sum()
    return(total_points)
