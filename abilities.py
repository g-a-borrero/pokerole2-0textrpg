import os, json
import numpy
import pandas as pd

path_to_json = 'data/Abilities/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

abilities = pd.DataFrame(columns=['Name', 'Effect', 'Description'])

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        name = json_text['Name']
        effect = json_text['Effect']
        description = json_text['Description']
        abilities.loc[index] = [name, effect, description]