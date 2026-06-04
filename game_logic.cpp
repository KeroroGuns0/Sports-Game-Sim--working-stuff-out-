#include "game_logic.h"
#include "game_state.h"

#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
#include<numeric>

namespace game_logic
{

    void startup()
    {
        std::cout << "Welcome to SF6 simulator!\n";
        std::cout << "The year is 2024, and you are an upcoming prodigy\n";
        std::cout << "Enter your name here: \n";

        std::cin >> game_state::player_name;

        std::cout << "Enter your gamer tag: \n";

        std::cin >> game_state::player_tag;

        select_pronouns();
        select_region();

        std::cout << "You are a promising 13 year-old gamer in "  << game_state::Regions[game_state::player_region].name << "\n";
        std::cout << "In the grand scheme of things, you are nothing, but you have many years ahead of you.\n";
        std::cout << "Train your player, compete at tournaments, and become the world champion!\n";
        std::cout << "Just be sure to manage your motivation and money as well, or it will be game over.\n";
        std::cout << "Now go forth! Your journey awaits!\n";
    }

    void select_region()
    {
        std::cout << "Select your region: \n";
        
        for(int i = 1; i < game_state::Regions.size(); i++)
        {
            game_state::Region cur = game_state::Regions[i];
            std::cout << i << ": " << cur.name << " - " << cur.level_name << "\n";
        }

        std::vector<int> keys(game_state::Regions.size());
        std::iota(keys.begin(), keys.end(), 1);

        game_state::player_region = get_valid_integer(keys);
    }

    void select_pronouns()
    {
        std::cout << "Select your pronouns: \n";
        
        for(const auto& [key, value] : game_state::Pronouns)
        {
            std::cout << key << ": " << value[0] << "/" << value[1] << "\n";
        }

        std::vector<int> keys;
        for(const auto& [key, value] : game_state::Pronouns)
        {
            keys.push_back(key);
        }

        game_state::player_pronouns = get_valid_integer(keys);

    }

    int get_valid_integer(std::vector<int> options)
    {
        int num;
        std::cin.exceptions(std::ios_base::failbit);
        while(true)
        {
            try
            {
                std::cin >> num;
                if (std::ranges::find(options, num) == options.end())
                {
                    throw std::runtime_error("INVALID OPTION");
                }
                break;
            }
            catch(const std::ios_base::failure& e)
            {
                std::cout << "ENTER AN INTEGER\n";

                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            }
            catch(const std::runtime_error& e)
            {
                std::cout << "NOT A VALID CHOICE\n";

                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            }
        }

        return num;
    }
}