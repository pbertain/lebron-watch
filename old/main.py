#!/usr/bin/env python3
# File name: nba-data.py
# Description: Get various data about the NBA
# Author: Paul Bertain
# Date: 2022-12-18
# Source: python-script-template.py
# IntelliJ Git notes: https://intellij-support.jetbrains.com/hc/en-us/articles/206544839

import argparse
from logging import critical, error, info, warning, debug

import get_player_id
import get_player_points


def parse_arguments():
    """Read arguments from a command line."""
    parser = argparse.ArgumentParser(description='Arguments get parsed via --commands')
    parser.add_argument('-v', metavar='verbosity', type=int, default=2,
                        help='Verbosity of logging: 0 -critical, 1 -error, 2 -warning, 3 -info, 4 -debug')

    args = parser.parse_args()
    #verbose = {0: logging.CRITICAL, 1: logging.ERROR, 2: logging.WARNING, 3: logging.INFO, 4: logging.DEBUG}
    #logging.basicConfig(format='%(message)s', level=verbose[args.v], stream=sys.stdout)
    # logging.basicConfig(filename='python-scripts.log',level=verbose[args.v])

    return args


def get_id(name_of_the_player):
    player_id = get_player_id.get_id(name_of_the_player)
    return (player_id)

def get_career_points(player_id):
    career_points = get_player_points.get_points(player_id)
    return (career_points)

def main():
    # list of players
    players_list = ["Damian Lillard"]
    points_dict = dict.fromkeys(players_list)
    for name_to_check in players_list:
        id_of_player = get_id(name_to_check)
        career_points = get_career_points(id_of_player)
        points_dict[name_to_check] = career_points
        # print("%-20s%6d" % (name_to_check, career_points))
    dame_points = points_dict['Damian Lillard']
    return(dame_points)

if __name__ == '__main__':
    args = parse_arguments()
    main()
