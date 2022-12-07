import requests
from bs4 import BeautifulSoup


def fastest_slowest(year, day):
    html = requests.get(f"https://adventofcode.com/{year}/leaderboard/day/{day}").text

    soup = BeautifulSoup(html, "html.parser")

    entries = soup.find_all("div", class_="leaderboard-entry")

    try:
        fastest = (
            entries[0].find("span", class_="leaderboard-time").text.split("  ")[-1]
        )
        slowest = (
            entries[99].find("span", class_="leaderboard-time").text.split("  ")[-1]
        )

        return fastest
    except:
        return ""


for day in range(25):
    dayz = []
    for year in range(2015, 2023):
        dayz.append(fastest_slowest(year, day + 1))

    # print(dayz)
    # join with comma
    print(",".join(dayz))
