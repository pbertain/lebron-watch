import requests
import argparse
from datetime import datetime, timedelta

def get_player_id(name):
    response = requests.get(f"https://www.balldontlie.io/api/v1/players?search={name}")
    players = response.json()['data']
    for player in players:
        if (player['first_name'] + ' ' + player['last_name']).lower() == name.lower():
            return player['id']
    return None

def get_game_stats(player_id, date):
    response = requests.get(f"https://www.balldontlie.io/api/v1/stats?dates[]={date}&player_ids[]={player_id}")
    stats = response.json()['data']
    return stats

def parse_date(date_str):
    if date_str.lower() == 'today':
        return datetime.now().strftime('%Y-%m-%d')
    elif date_str.lower() == 'yesterday':
        return (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    else:
        return date_str

def format_stats(player_name, stats):
    if stats:
        game_stat = stats[0]  # Assuming we're interested in the first game listed for that date
        player_name_formatted = f"{player_name:<20}"  # Left justify within 20 characters
        formatted_stats = f"{player_name_formatted}: {game_stat['pts']} pts, {game_stat['reb']} reb, {game_stat['ast']} ast, {game_stat['blk']} blk, {game_stat['stl']} stl"
        return formatted_stats
    else:
        player_name_formatted = f"{player_name:<20}"  # Left justify w/20 chars
        formatted_status = f"{player_name_formatted}: did not play"
        status = 'false'
        return status

def main():
    parser = argparse.ArgumentParser(description='Get NBA player statistics for a specific game.')
    parser.add_argument('player_name', type=str, help='Full name of the NBA player')
    parser.add_argument('date', type=str, help='Date of the game (format: YYYY-MM-DD), or "today" or "yesterday"')
    args = parser.parse_args()

    date = parse_date(args.date)
    player_id = get_player_id(args.player_name)
    if player_id:
        game_stats = get_game_stats(player_id, date)
        print(format_stats(args.player_name, game_stats))
    else:
        print(f"Player {args.player_name} not found.")

if __name__ == '__main__':
    main()

