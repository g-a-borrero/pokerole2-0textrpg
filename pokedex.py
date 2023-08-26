import os, json
import numpy
import pandas as pd

path_to_json = 'data/Pokedex/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

pokedex = pd.DataFrame(columns=['DexID', 'Number', 'Species', 'Type1', 'Type2', 'Base HP', 'Strength', 'Max Strength', 'Dexterity', 'Max Dexterity', 'Vitality', 'Max Vitality', 'Special', 'Max Special', 'Insight', 'Max Insight', 'Ability1', 'Ability2', 'Hidden Ability','Dex', 'Moves Learned'])

for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)
        dexid = json_text['DexID']
        number = json_text['Number']
        species = json_text['Name']
        type1 = json_text['Type1']
        type2 = json_text['Type2']
        base_hp = json_text['BaseHP']
        strength = json_text['Strength']
        max_strength = json_text['MaxStrength']
        dexterity = json_text['Dexterity']
        max_dexterity = json_text['MaxDexterity']
        vitality = json_text['Vitality']
        max_vitality = json_text['MaxVitality']
        special = json_text['Special']
        max_special = json_text['MaxSpecial']
        insight = json_text['Insight']
        max_insight = json_text['MaxInsight']
        ability1 = json_text['Ability1']
        ability2 = json_text['Ability2']
        hidden_ability = json_text["HiddenAbility"]
        dex = json_text['DexDescription']
        moves = json_text['Moves']
        pokedex.loc[index] = [dexid, number, species, type1, type2, base_hp, strength, max_strength, dexterity, max_dexterity, vitality, max_vitality, special, max_special, insight, max_insight, ability1, ability2, hidden_ability, dex, moves]

