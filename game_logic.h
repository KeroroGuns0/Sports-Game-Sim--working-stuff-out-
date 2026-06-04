#pragma once

#include <vector>

#include "game_state.h"

namespace game_logic
{

    void startup();

    void select_region();

    void select_pronouns();

    int get_valid_integer(std::vector<int> options);
}



