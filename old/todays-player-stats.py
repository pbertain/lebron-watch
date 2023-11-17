import argparse
from datetime import datetime, timedelta
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import pandas as pd

def get_player_stats(player_name, date, season='2022-23'):
    # Find players by name
    nba_players = players.get_players()
    player = [player for player in nba_players if player['full_name'].lower() == player_name.lower()][0]
    player_id = player['id']

    # Query the game log for this player
    gamelog = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    df = gamelog.get_data_frames()[0]

    # Handle date input
    if date.lower() == 'yesterday':
        date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    elif date.lower() == 'today':
        date = datetime.now().strftime('%Y-%m-%d')

    # Filter the dataframe for the specified date
    game_stats = df[df['GAME_DATE'] == date]

    # Select the required stats
    if not game_stats.empty:
        stats = game_stats[['PTS', 'REB', 'AST', 'STL', 'BLK']]
        return stats
    else:
        return f"No game found for {player_name} on {date}"

def main():
    parser = argparse.ArgumentParser(description='Get NBA player statistics for a specific date.')
    parser.add_argument('player_name', type=str, help='Full name of the NBA player')
    parser.add_argument('date', type=str, help='Date of the game (format: YYYY-MM-DD) or keywords "today" or "yesterday"')
    parser.add_argument('--season', type=str, default='2022-23', help='NBA season (format: YYYY-YY)')
    args = parser.parse_args()

    stats = get_player_stats(args.player_name, args.date, args.season)
    print(stats)

if __name__ == '__main__':
    main()

