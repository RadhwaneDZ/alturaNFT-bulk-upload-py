import json
import csv
import os

#set default value tat are not present in json file or for extra traits and properties 
default_values = { 
    'stackable': True,
    'supply': 1,
    'maxSupply': 1,
    'consumable': False,
    'nsfw': False,
    'revealed': False,
    'Health': 100,
    'Stamina': 100,
    'Capacity': 1000,
    'Mining': 2,
    'Time': 2,
    'Multiplier': 2,
    'description': 'Foxtil Collection of 10.000 NFTs use it to play2earn in meta board games like DominoFi, LudoFi, ChessFi and our web3 games, currently in development https://beta.dominofi.com'
}

csv_columns = ['image', 'name', 'description', 'unlockableText', 'stackable', 'supply', 'maxSupply', 'consumable', 'nsfw', 'revealed', 'Background', 'Body', 'Eyes', 'Shirts', 'Chain', 'Mouth', 'Glasses', 'Hat', 'Health', 'Stamina', 'Capacity', 'Mining', 'Time', 'Multiplier']

csv_file = open('altura.csv', 'w', newline='', encoding='utf-8')
writer = csv.DictWriter(csv_file, fieldnames=csv_columns)

writer.writeheader()

for file_name in os.listdir('json'):
    if file_name.endswith('.json'):
        with open(os.path.join('json', file_name), encoding='utf-8') as f:
            item = json.load(f)

        row = {column: default_values.get(column, '') for column in csv_columns}

        row.update({
            'image': os.path.splitext(item['image'].lstrip('/'))[0],
            'name': item['name'],
            'description': item.get('description', default_values['description']),
            'unlockableText': item.get('unlockableText', ''),
        })

        if 'attributes' in item:
            for attribute in item['attributes']:
                row[attribute['trait_type']] = attribute['value']

        writer.writerow(row)

csv_file.close()