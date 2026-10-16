#pragma once

#include "discord.h"

namespace jak1 {
extern const std::map<std::string, std::string> level_names;
extern const std::map<std::string, std::string> level_name_remap;
extern const std::vector<std::string> indoor_levels;
extern const char* const cover_art_url;
extern const char* const thumbnail_art_url;
const char* time_of_day_str(float time);
std::string time_remaining_str(s32 ticks);
}  // namespace jak1
