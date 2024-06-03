import requests
import json

START_YEAR = 2021
END_YEAR = 2021

def open_month(year, month):
    with open(f'./games/{year}-{month:02}.json', 'r') as f:
        games = json.loads(f.readlines()[0])
        num_games = len(games['games'])
        game = games['games'][0]
        print(json.dumps(game))
        white = game['white']
        black = game['black']
        print(f"{white['username']} - {white['rating']} v {black['username']} - {black['rating']}")
        return num_games

def main():
    count = 0
    for year in range(START_YEAR, END_YEAR+1):
        for month in range(1, 13):
            count += open_month(year, month)
    print(count)

if __name__ == '__main__':
    main()
