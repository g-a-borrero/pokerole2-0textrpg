import os, json
import numpy
import pandas as pd

path_to_json = 'data/Rooms/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

rooms = pd.DataFrame(columns=['ID', 'Short Description', 'Region', 'Location', 'Long Description', 'Inventory', 'Inside', 'north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest', 'in', 'out', 'up', 'down'])

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        ids = json_text['ID']
        short_desc = json_text['Short Description']
        region = json_text['Region']
        location = json_text['Location']
        long_desc = json_text['Long Description']
        inv = json_text['Inventory']
        inside = json_text['Inside']
        n = json_text['Directions'][0]['North']
        ne = json_text['Directions'][1]['Northeast']
        e = json_text['Directions'][2]['East']
        se = json_text['Directions'][3]['Southeast']
        s = json_text['Directions'][4]['South']
        sw = json_text['Directions'][5]['Southwest']
        w = json_text['Directions'][6]['West']
        nw = json_text['Directions'][7]['Northwest']
        ins = json_text['Directions'][8]['In']
        outs = json_text['Directions'][9]['Out']
        up = json_text['Directions'][10]['Up']
        down = json_text['Directions'][11]['Down']
        rooms.loc[index] = [ids, short_desc, region, location, long_desc, inv, inside, n, ne, e, se, s, sw, w, nw, ins, outs, up, down]
