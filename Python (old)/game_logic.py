import game_state

# Game setup and character creation. Before core gameplay loop
def startup():
    print("Welcome to SF6 simulator!")
    print("The year is 2024, and you are an upcoming prodigy")
    print("Enter your name here: ")

    game_state.player_name = input()

    print("Enter your gamer tag: ")

    game_state.player_tag = input()

    select_pronouns()
    select_region()

    print(f"You are a promising 13 year-old gamer in {(game_state.Regions[game_state.player_region])[0]}")
    print("In the grand scheme of things, you are nothing, but you have many years ahead of you.")
    print("Train your player, compete at tournaments, and become the world champion!")
    print("Just be sure to manage your motivation and money as well, or it will be game over.")
    print("Now go forth! Your journey awaits!")




# check if region is valid and if it is not then do it again.
def select_region() -> None:
    print("Select your region: ")
    
    for key, value in game_state.Regions.items():
        print(f"{key}: {value[0]} - {value[1]}")
    
    game_state.player_region = get_valid_integer(game_state.Regions.keys())
    

def select_pronouns() -> None:
    # check if pronoun is valid and if it is not then do it again.
    print("Select your pronouns: ")
    
    for key, value in game_state.Pronouns.items():
        print(f"{key}: {value[0]}/{value[1]}")

    game_state.player_pronouns = get_valid_integer(game_state.Pronouns.keys())


# This is a 2 fold check. Check if it is an integer, and check if it is a valid option in array options that is passed into the function
# options will most likely be dictionary keys. 
def get_valid_integer(options) -> int:
    while True:
        try:
            num = int(input())
            break
        except ValueError:
            print("ENTER AN INTEGER")
    
    if num in options:
        return num
    else:
        print("INVALID OPTION, TRY AGAIN")
        get_valid_integer(options)