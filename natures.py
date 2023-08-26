import os, json
import numpy
import pandas as pd

path_to_json = 'data/Natures/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

natures = pd.DataFrame(columns=['Name', 'Confidence', 'Keywords', 'Description'])

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        name = json_text['Name']
        confidence = json_text['Confidence']
        keywords = json_text['Keywords']
        description = json_text['Description']
        natures.loc[index] = [name, confidence, keywords, description]