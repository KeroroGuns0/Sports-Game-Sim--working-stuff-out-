class Player:
    def __init__(self, name: str, tag: str, age: int, pronouns: int, region: int, advantage: int, disadvantage: int, neutral: int, mental: int):
        self.name = name
        self.tag = tag
        self.age = age
        self.pronouns = pronouns
        self.region = region
        self.advatange = advantage
        self.disadvantage = disadvantage
        self.neutral = neutral
        self.mental = mental
        #self.main = main

# Only toggle this for quit options basically
game_running = True

# variables that need to be accessed by multiple files.
player_name = ""
player_tag = ""
player_pronouns = -1
player_region = -1

player = Player(player_name, player_tag, 13, player_pronouns, player_region, 0, 0, 0, 0)

# these are more game state instead of player state


# format: {region name, difficulty name, diffculty num}
Regions = {
    1: ["Japan", "Very Competitive", 5],
    2: ["NA East", "Competitive", 4],
    3: ["China", "Competitive", 4],
    4: ["UK/Ireland", "Hard", 4],
    5: ["South Korea", "Hard", 4],
    6: ["EU West", "Moderate", 3],
    7: ["NA West", "Moderate", 3],
    8: ["NA Midwest", "Moderate", 3],
    9: ["South America", "Moderate", 3],
    10: ["Europe North/East", "Light", 2],
    11: ["Mexico", "Light", 2],
    12: ["Middle East", "Light", 2],
    13: ["Asia Southeast", "Obscure", 1],
    14: ["Asia South", "Obscure", 1],
    15: ["Central America", "Obscure", 1],
    16: ["Africa", "Obscure", 1],
    17: ["Oceaina", "Obscure", 1]
}

Pronouns = {
    1: ["he", "him"],
    2: ["she", "her"],
    3: ["they", "them"] 
}

Game_Characters = {
    # TODO:
    # Add characters, selecting a main, and tier lists of characters that change with meta
    # Counters are less important because it is less prevalent in FGC games
}



# neutral, advantage, disadvantage is the basics. The hero select is mainly aesthetic but necessary I think. 
# 
        