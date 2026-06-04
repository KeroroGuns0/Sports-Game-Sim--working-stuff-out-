#include "game_state.h"

namespace game_state
{
    bool game_running = true;

    // Struct constructors
    game_state::Region::Region(std::string rname, std::string rlevel_name, int rlevel_num) : name(rname), level_name(rlevel_name), level_num(rlevel_num) {}
    game_state::Player::Player(std::string pname, std::string ptag, int page, int ppronouns, int pregion, int padvantage, int pdisadvantage, int pneutral, int pmental) 
        : name(pname), tag(ptag), age(page), pronouns(ppronouns), region(pregion), advantage(padvantage), disadvantage(pdisadvantage), neutral(pneutral), mental(pmental) {}

    std::string player_name = "";
    std::string player_tag = "";
    int player_pronouns = -1;
    int player_region = -1;

    std::unique_ptr<Player> player = std::make_unique<Player>(
        player_name, player_tag, 13, player_pronouns, player_region, 0, 0, 0, 0
    );

    std::vector<Region> Regions = 
    {
        Region{"PADDING", "FOR CONSISTENT INDEXING", -1},
        Region{"Japan", "Very Competitive", 5},
        Region{"NA East", "Competitive", 4},
        Region{"China", "Competitive", 4},
        Region{"UK/Ireland", "Hard", 4},
        Region{"South Korea", "Hard", 4},
        Region{"EU West", "Moderate", 3},
        Region{"NA West", "Moderate", 3},
        Region{"NA Midwest", "Moderate", 3},
        Region{"South America", "Moderate", 3},
        Region{"Europe North/East", "Light", 2},
        Region{"Mexico", "Light", 2},
        Region{"Middle East", "Light", 2},
        Region{"Asia Southeast", "Obscure", 1},
        Region{"Asia South", "Obscure", 1},
        Region{"Central America", "Obscure", 1},
        Region{"Africa", "Obscure", 1},
        Region{"Oceaina", "Obscure", 1}
    };

    std::unordered_map<int, std::array<std::string, 2>> Pronouns = 
    {
        {1, {"he", "him"}},
        {2, {"she", "her"}},
        {3, {"they", "them"}}
    };
}