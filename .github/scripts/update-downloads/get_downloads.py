import requests

repos = [
    "Kuitar5/the-forgotten-lands",
    "OpenGOAL-Mods/OG-Speedrun-Practice",
    "OpenGOAL-Mods/OG-Randomizer",
    "OpenGOAL-Mods/OG-RCO",
    "OpenGOAL-Mods/OG-FlutFlut-Legacy",
    "OpenGOAL-Mods/OG-Zoomer-Legacy",
    "OpenGOAL-Mods/OG-SM64",
    "OpenGOAL-Mods/OG-Microtransactions",
    "dallmeyer/OG-OrbHunt",
    "OpenGOAL-Mods/OG-Bugged",
    "OpenGOAL-Mods/OG-Patched",
    "Hat-Kid/og-orange-demon",
    "OpenGOAL-Mods/OG-Fricked",
    "ruhphorte/spec-ops-jak",
    "ArchipelaGOAL/ArchipelaGOAL",
    "my-opengoal-mods/OG-Jak-The-Chicken-Reborn",
    "OpenGOAL-Mods/OG-Daxter2",
    "OpenGOAL-Mods/OG-Jak2-AugustBuild",
    "RealOfficialKraken/updated-HeroModePlus",
    "RealOfficialKraken/roguelikejakii",
    "OpenGOAL-Mods/OG-Dark-Jak",
    "Grateful-Forest/Platformia",
    "dallmeyer/jak-up",
    "Cuttlefishthesage/OG-Mod-Base",
    "Cuttlefishthesage/Og-ModBase-Rockpool",
    "Cuttlefishthesage/LL-OpenGOAL-ModBase",
    "OpenGOAL-Mods/OG-Shrek-Adventures",
    "dallmeyer/OG-rayman",
    "Clankape/OG-Mod-Base-Halloween",
]


def get_downloads(repo):
    url = f"https://api.github.com/repos/{repo}/releases"
    response = requests.get(url)
    releases = response.json()
    total_downloads = sum(
        release["assets"][0]["download_count"]
        for release in releases
        if "assets" in release
    )
    return total_downloads


total_downloads = sum(get_downloads(repo) for repo in repos)

badge_url = (
    f"https://img.shields.io/badge/Total%20Downloads-{total_downloads}-brightgreen"
)
readme_file = "README.md"

with open(readme_file, "r") as file:
    content = file.read()

content = content.replace(
    "![Total Downloads](https://img.shields.io/badge/Total%20Downloads-XXXXX-brightgreen)",
    f"![Total Downloads]({badge_url})",
)

with open(readme_file, "w") as file:
    file.write(content)

print(f"Total Downloads: {total_downloads}")
