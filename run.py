import requests
from collections import defaultdict
import json
from datetime import datetime

START_YEAR = 2021
END_YEAR = 2024

COLUMNS = [
    'Time',
    'Time Class',
    'Time Control',
    'Rated?',
    'White User',
    'White Rating',
    'White Result',
    'White Accuracy',
    'Black User',
    'Black Rating',
    'Black Result',
    'Black Accuracy',
    'Result',
]

class Player(object):
    def __init__(self, username, rating, result):
        self.username = username
        self.rating = rating
        self.result = result

class Row(object):
    def __init__(self):
        self.time = None
        self.time_class = None
        self.time_control = None
        self.white = None
        self.black = None
        self.result = None
        self.rated = None
        self.white_accuracy = ''
        self.black_accuracy = ''

    @classmethod
    def game(cls, game):
        self = cls()

        self.white = Player(game['white']['username'], game['white']['rating'], game['white']['result'])
        self.black = Player(game['black']['username'], game['black']['rating'], game['black']['result'])

        self.time_class = game['time_class']
        self.time_control = game['time_control']
        self.time = datetime.fromtimestamp(game['end_time']).isoformat()
        self.rated = game['rated']

        if 'accuracies' in game:
            self.white_accuracy = f"{game['accuracies']['white']:.1f}"
            self.black_accuracy = f"{game['accuracies']['black']:.1f}"

        if game['white']['result'] == 'win':
            self.result = '1-0'
        elif game['black']['result'] == 'win':
            self.result = '0-1'
        else:
            self.result = '0.5-0.5'
        return self

    def csv(self):
        return ','.join([
            str(self.time),
            self.time_class,
            self.time_control,
            str(self.rated),
            self.white.username,
            str(self.white.rating),
            self.white.result,
            self.white_accuracy,
            self.black.username,
            str(self.black.rating),
            self.black.result,
            self.black_accuracy,
            self.result,
        ])

def parse_month(year, month):
    with open(f'./games/{year}-{month:02}.json', 'r') as f:
        raw = json.loads(f.readlines()[0])
        for game in raw['games']:
            g = Row.game(game)
            print(g.csv())

def main():
    print(','.join(COLUMNS))
    for year in range(START_YEAR, END_YEAR+1):
        for month in range(1, 13):
            if year == 2024 and month > 5:
                break
            parse_month(year, month)

if __name__ == '__main__':
    main()
