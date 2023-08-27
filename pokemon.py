import random
from pokedex import pokedex
from natures import natures
from abilities import abilities

"""
def rand_dist(total, d, keys, max_total=False):
	for _ in range(total):
		rand_key = random.choice(keys)
		if type(max_total) == type(13):
			while d[rand_key] == max_total:
				rand_key = random.choice(keys)
		elif type(max_total) == type({"a": 1}):
			while d[rand_key] == max_total[rand_key]:
				rand_key = random.choice(keys)
		d[rand_key] += 1
	return d
"""

def rand_dist(total, d, keys, max_total=False):
	for _ in range(total):
		rand_key = random.choice(keys)
		if type(max_total) == type(13):
			while d[rand_key] == max_total:
				if d.values() == [max_total]*len(keys):
					break
				else:
					rand_key = random.choice(keys)
		elif type(max_total) == type({"a": 1}):
			while d[rand_key] == max_total[rand_key]:
				if d == max_total:
					break
				else:
					rand_key = random.choice(keys)
		d[rand_key] += 1
	return d

class Pokemon:
	ranks = ["Starter", "Beginner", "Amateur", "Ace", "Pro", "Master", "Champion"]
	every = {
		"Human": [],
		"Pokemon": []
	}
	def __init__(self, species=False, name="", age=False, rank="Starter", nature=False, rand=False):
		self.basics(species, name, age, rank, nature, rand)
		self.maxhp = pokedex[pokedex['Species']==self.species]['Base HP'].values[0] if self.species not in ["Human", "Trainer"] else 4
		
		skill_keys = ["Brawl", "Channel", "Clash", "Evasion", "Alert", "Athletic", "Nature", "Stealth", "Allure", "Etiquette", "Intimidate", "Perform", "Empathy"]
		if self.species in ["Human", "Trainer"]:
			skill_keys += ["Crafts", "Lore", "Medicine", "Science"]
		skills = dict(zip(skill_keys, [0]*len(skill_keys)))
		ranks_skills = {"Starter": 5, "Beginner": 9, "Amateur": 12, "Ace": 14, "Pro": 15, "Master": 15, "Champion": 15}
		ranks_skills_max = {"Starter": 1, "Beginner": 2, "Amateur": 3, "Ace": 4, "Pro": 5, "Master": 5, "Champion": 5}
		
		self.base_attrs()
		attr_keys = ["Strength", "Vitality", "Dexterity", "Insight", "Special"]
		attrs = dict(zip(attr_keys, [self.strength, self.vitality, self.dexterity, self.insight, self.special]))
		attr_max = {"Strength": self.max_strength, "Vitality": self.max_vitality, "Dexterity": self.max_dexterity, "Insight": self.max_insight, "Special": self.max_special}
		
		self.base_socs()
		soc_keys = ["Tough", "Cool", "Beauty", "Clever", "Cute"]
		socs = dict(zip(soc_keys, [1]*len(soc_keys)))
		soc_max = 5

		if rand:
			rand_dist(ranks_skills[self.rank], skills, skill_keys, max_total=ranks_skills_max[self.rank])
			if self.species not in ["Human", "Trainer"]:
				skills["Crafts"] = 0
				skills["Lore"] = 0
				skills["Medicine"] = 0
				skills["Science"] = 0
			attr_total = 0
			soc_total = 0
			if self.species in ["Human", "Trainer"]:
				soc_max = 5
				if self.age in [range(0, 13)]:
					attr_total += 0
					soc_total += 0
				elif self.age in [range(13,18)]:
					attr_total += 2
					soc_total += 2
				elif self.age in [range(18,65)]:
					attr_total += 4
					soc_total += 4
				else:
					attr_total += 3
					soc_total += 6
			ranks_attrs = {"Starter": 0, "Beginner": 2, "Amateur": 4, "Ace": 6, "Pro": 8, "Master": 8, "Champion": 8}
			attr_total += ranks_attrs[self.rank]
			soc_total += ranks_attrs[self.rank]
			rand_dist(attr_total, attrs, attr_keys, attr_max)
			rand_dist(soc_total, socs, soc_keys, soc_max)
		else:
			pass

		self.set_attrs(attrs)
		self.set_socs(socs)		
		self.set_skills(skills)
		self.set_calcs()

		self.inventory = []

		if self.species in ["Human", "Trainer"]:
			humans_len = len(Pokemon.every["Human"])
			self.id = f"{humans_len:05d}_Human_{self.name}"
			Pokemon.every["Human"] += [(self.id, self)]
		else:
			self.set_ability()
			self.set_moves()
			pokemon_len = len(Pokemon.every["Pokemon"])
			self.id = f"{pokemon_len:05d}_{self.species}"
			Pokemon.every["Pokemon"] += [(self.id, self)]

	def basics(self, species, name, age, rank, nature, rand):
		self.species = species.title() if species.title() not in ["Human", "Trainer"] else "Human"
		self.name = name if name != "" else self.species
		self.rank = rank.title() if rank.title() != "Random" else Pokemon.ranks[random.randint(0,len(Pokemon.ranks)-1)]
		self.nature_ = nature.title() if nature else natures.loc[random.randint(0, len(natures)-1)]['Name']
		self.confidence = natures[natures['Name']==self.nature_]['Confidence'].values[0]
		self.nature_keywords = natures[natures['Name']==self.nature_]['Keywords'].values[0]
		self.nature_description = natures[natures['Name']==self.nature_]['Description'].values[0]
		self.set_age(age)

	def set_age(self, age):
		if type(age) == type("abc"):
			if age.title() in ["Kid", "Child"]:
				self.age = random.randint(8, 12)
			elif age.title() in ["Teen", "Teenager"]:
				self.age = random.randint(13, 17)
			elif age.title() in ["Adult", "Young Adult"]:
				self.age = random.randint(18, 64)
			else:
				self.age = random.randint(65, 100)
		elif age == False:
			self.age = random.randint(8, 100)
		else:
			self.age = age

	def base_attrs(self):
		self.strength = 1 if self.species in ["Human", "Trainer"] else pokedex[pokedex['Species']==self.species]['Strength'].values[0]
		self.vitality = 1 if self.species in ["Human", "Trainer"] else pokedex[pokedex['Species']==self.species]['Vitality'].values[0]
		self.dexterity = 1 if self.species in ["Human", "Trainer"] else pokedex[pokedex['Species']==self.species]['Dexterity'].values[0]
		self.insight = 1 if self.species in ["Human", "Trainer"] else pokedex[pokedex['Species']==self.species]['Insight'].values[0]
		self.special = 0 if self.species in ["Human", "Trainer"] else pokedex[pokedex['Species']==self.species]['Special'].values[0]
		self.max_strength = 5 if self.species in ["Human", "Trainer"] else pokedex[pokedex['Species']==self.species]['Max Strength'].values[0]
		self.max_vitality = 5 if self.species in ["Human", "Trainer"] else pokedex[pokedex['Species']==self.species]['Max Vitality'].values[0]
		self.max_dexterity = 5 if self.species in ["Human", "Trainer"] else pokedex[pokedex['Species']==self.species]['Max Dexterity'].values[0]
		self.max_insight = 5 if self.species in ["Human", "Trainer"] else pokedex[pokedex['Species']==self.species]['Max Insight'].values[0]
		self.max_special = 0 if self.species in ["Human", "Trainer"] else pokedex[pokedex['Species']==self.species]['Max Strength'].values[0]

	def base_socs(self):
		self.tough = 1
		self.cool = 1
		self.beauty = 1
		self.clever = 1
		self.cute = 1

	def set_attrs(self, attrs):
		self.strength = attrs["Strength"]
		self.vitality = attrs["Vitality"]
		self.dexterity = attrs["Dexterity"]
		self.insight = attrs["Insight"]
		self.special = attrs["Special"]

	def set_socs(self, socs):
		self.tough = socs["Tough"]
		self.cool = socs["Cool"]
		self.beauty = socs["Beauty"]
		self.clever = socs["Clever"]
		self.cute = socs["Cute"]

	def set_skills(self, skills):
		self.brawl = skills["Brawl"]
		self.channel = skills["Channel"]
		self.clash = skills["Clash"]
		self.evasion = skills["Evasion"]
		self.alert = skills["Alert"]
		self.athletic = skills["Athletic"]
		self.nature = skills["Nature"]
		self.stealth = skills["Stealth"]
		self.allure = skills["Allure"]
		self.etiquette = skills["Etiquette"]
		self.intimidate = skills["Intimidate"]
		self.perform = skills["Perform"]
		self.empathy = skills["Empathy"]
		self.crafts = skills["Crafts"]
		self.lore = skills["Lore"]
		self.medicine = skills["Medicine"]
		self.science = skills["Science"]

	def set_calcs(self):
		self.maxhp += self.vitality
		self.currenthp = self.maxhp
		self.maxmoves = 2 + self.insight
		self.battle_evasion = self.dexterity + self.evasion
		self.battle_clash = max([self.strength, self.special]) + self.clash
		self.initiative = self.dexterity + self.alert
		self.defense = self.vitality
		self.special_defense = self.insight

	def set_ability(self):
		ab_num = random.randint(0,255)
		ab_list = []
		for ab in [pokedex[pokedex['Species']==self.species]['Ability1'].values[0], pokedex[pokedex['Species']==self.species]['Ability2'].values[0], pokedex[pokedex['Species']==self.species]['Hidden Ability'].values[0]]:
			if ab != "":
				ab_list.append(ab)
		if len(ab_list) == 1:
			self.ability = ab_list[-1]
		elif ab_num == 255:
			self.ability = ab_list[-1]
		elif ab_num % 2 == 0:
			self.ability = ab_list[0]
		else:
			self.ability = ab_list[1]
		self.set_ability_info(self.ability)

	def set_ability_info(self, ab):
		self.ability_effect = abilities[abilities['Name']==ab]['Effect'].values[0]
		self.ability_description = abilities[abilities['Name']==ab]['Description'].values[0]

	def set_moves(self):
		pkmn_moveset = {}
		for each_rank in Pokemon.ranks:
			pkmn_moveset[each_rank] = []
		for each_rank in pokedex[pokedex['Species']==self.species]['Moves Learned'].values[0]:
			pkmn_moveset[each_rank['Learned']].append(each_rank['Name'])
		moveset = []
		for each_rank in Pokemon.ranks:
			moveset.append(pkmn_moveset[each_rank])
			if each_rank == self.rank:
				break
		moveset = sum(moveset, [])
		self.moves = moveset if self.maxmoves >= len(moveset) else random.sample(moveset, k=self.maxmoves)
		

	def display(self):
		print("-"*50)
		print(self.species + " (" + self.name + ")\tRank: " + self.rank)
		if self.species in ["Human", "Trainer"]:
			print("Age: %d" % (self.age))
		print("-"*50)
		print("HP: %d/%d\t\tMax Moves: %d" % (self.currenthp, self.maxhp, self.maxmoves))
		print("Defense: %d\tSpecial Defense:%d" % (self.defense, self.special_defense))
		print("Initiative: %d\tEvasion: %d\tClash:%d" % (self.initiative, self.battle_evasion, self.battle_clash))
		print("-"*50)
		print("Strength: %d\tVitality: %d\tDexterity: %d" % (self.strength, self.vitality, self.dexterity))
		print("Insight: %d\tSpecial: %d" % (self.insight, self.special))
		print("-"*50)
		print("Tough: %d\tCool: %d\t\tBeauty: %d" % (self.tough, self.cool, self.beauty))
		print("Clever: %d\tCute: %d" % (self.clever, self.cute))
		print("-"*50)
		if self.species not in ["Human", "Trainer"]:
			print(self.moves)

"""
abc = Pokemon("Pikachu", name="Sparky", rank="Random", rand=True)
abc.display()

xyz = Pokemon("Trainer", name="Gabby", rank="Champion", rand=True)
xyz.display()

print(Pokemon.every)
"""
