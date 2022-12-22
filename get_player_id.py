#!/usr/bin/env python3
# File name: get_player_id.py
# Description: return player id for a given name
# Author: Paul Bertain
# Date: 2022-12-18
# Code template: python-script-template.py
# Source: https://github.com/swar/nba_api/blob/master/docs/examples/Basics.ipynb
# Additional: https://betterprogramming.pub/using-pythons-nba-api-to-create-a-simple-regression-model-ac9a3b36bc8

# First we will import our packages
from nba_api.stats.static import players
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
