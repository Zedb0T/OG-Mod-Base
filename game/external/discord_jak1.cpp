#include "discord_jak1.h"

#include "fmt/format.h"

namespace jak1 {
const std::map<std::string, std::string> level_names = {{"intro", "Intro"},
                                                        {"title", "Title screen"},
                                                        {"training", "Geyser Rock"},
                                                        {"village1", "Sandover Village"},
                                                        {"beach", "Sentinel Beach"},
                                                        {"jungle", "Forbidden Jungle"},
                                                        {"misty", "Misty Island"},
                                                        {"firecanyon", "Fire Canyon"},
                                                        {"village2", "Rock Village"},
                                                        {"swamp", "Boggy Swamp"},
                                                        {"rolling", "Precursor Basin"},
                                                        {"sunken", "Lost Precursor City"},
                                                        {"ogre", "Mountain Pass"},
                                                        {"village3", "Volcanic Crater"},
                                                        {"snow", "Snowy Mountain"},
                                                        {"maincave", "Spider Cave"},
                                                        {"lavatube", "Lava Tube"},
                                                        {"citadel", "Gol and Maia's Citadel"},
                                                        {"finalboss", "Final Boss"}};

// for remapping sub-level names to the matching one in level_names
const std::map<std::string, std::string> level_name_remap = {{"jungleb", "jungle"},
                                                             {"sunkenb", "sunken"},
                                                             {"robocave", "maincave"},
                                                             {"darkcave", "maincave"}};

// levels that are not affected by time of day
const std::vector<std::string> indoor_levels = {
    "intro",    "title",    "jungleb",  "sunken",   "sunkenb",
    "maincave", "robocave", "darkcave", "lavatube", "citadel",
};

// time of day string to append to level name for icons
const char* time_of_day_str(float time) {
  int hour = static_cast<int>(time);

  if (hour >= 0 && hour <= 9) {
    return "green-sun";
  } else if (hour < 22) {
    return "day";
  } else if (hour < 25) {
    return "evening";
  } else {
    return "";
  }
}

// A Complicated Mod art, the same images the mod list uses
const char* const cover_art_url =
    "https://raw.githubusercontent.com/MikeGamePro/OG-Complicated/refs/heads/main/cover.png";
const char* const thumbnail_art_url =
    "https://raw.githubusercontent.com/MikeGamePro/OG-Complicated/refs/heads/main/thumbnail.png";

// countdown ticks (300 per second) as h:mm:ss or m:ss
std::string time_remaining_str(s32 ticks) {
  int total_seconds = std::max(ticks, 0) / 300;
  int hours = total_seconds / 3600;
  int minutes = (total_seconds / 60) % 60;
  int seconds = total_seconds % 60;
  if (hours > 0) {
    return fmt::format("{}:{:02}:{:02}", hours, minutes, seconds);
  }
  return fmt::format("{}:{:02}", minutes, seconds);
}
}  // namespace jak1