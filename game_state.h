#pragma once

#include<string>
#include<memory>
#include<unordered_map>
#include<vector>
#include<array>
#include<tuple>

namespace game_state
{

    struct Player
    {
        std::string name;
        std::string tag;
        int age;
        int pronouns;
        int region;
        int advantage;
        int disadvantage;
        int neutral;
        int mental;
        

        Player(std::string pname, std::string ptag, int page, int ppronouns, int pregion, int padvantage, int pdisadvantage, int pneutral, int pmental);
    };

    struct Region
    {
        std::string name;
        std::string level_name;
        int level_num;

        Region(std::string rname, std::string rlevel_name, int rlevel_num);
    };

    extern bool game_running;

    // variables that need to be accessed by multiple files.
    extern std::string player_name;
    extern std::string player_tag;
    extern int player_pronouns;
    extern int player_region;

    extern std::unique_ptr<Player> player;

    extern std::vector<Region> Regions;

    extern std::unordered_map<int, std::array<std::string, 2>> Pronouns;

    // TODO: 
    // Add game characters map so we can have mains, tier list/meta, possibly some counterpick but probably not
}


