import requests

repos = [
    'open-goal/jak-project',
    'jakmods-dev/opengoal-modbase'
]

def get_downloads(repo):
    url = f'https://api.github.com/repos/{repo}/releases'
    response = requests.get(url)
    releases = response.json()
    total_downloads = sum(release['assets'][0]['download_count'] for release in releases if 'assets' in release)
    return total_downloads

total_downloads = sum(get_downloads(repo) for repo in repos)

badge_url = f"https://img.shields.io/badge/Total%20Downloads-{total_downloads}-brightgreen"
readme_file = "README.md"

with open(readme_file, 'r') as file:
    content = file.read()

content = content.replace(
    "![Total Downloads](https://img.shields.io/badge/Total%20Downloads-XXXXX-brightgreen)",
    f"![Total Downloads]({badge_url})"
)

with open(readme_file, 'w') as file:
    file.write(content)

print(f"Total Downloads: {total_downloads}")
