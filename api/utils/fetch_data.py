import os
import httpx
from typing import Any

ODDS_API_KEY = os.getenv("ODDS_API_KEY")
BALLEDONTLIE_API = "https://www.balldontlie.io/api/v1/"
MLB_STATS_API = "https://statsapi.mlb.com/api/v1/"

# Odds endpoints mapping
SPORT_MAP = {
    "baseball_mlb": "baseball_mlb",
    "basketball_nba": "basketball_nba",
}

async def get_odds(sport: str) -> Any:
    url = f"https://api.the-odds-api.com/v4/sports/{SPORT_MAP[sport]}/odds"
    params = {
        "apiKey": ODDS_API_KEY,
        "regions": "us",
        "markets": "h2h,spreads,totals",
        "oddsFormat": "american"
    }
    async with httpx.AsyncClient() as client:
        r = await client.get(url, params=params)
        return r.json()

async def get_players(league: str) -> Any:
    async with httpx.AsyncClient() as client:
        if league == "nba":
            # Get all NBA players (balldontlie)
            url = BALLEDONTLIE_API + "players"
            players = []
            page = 1
            while True:
                r = await client.get(url, params={"per_page": 100, "page": page})
                data = r.json()
                players.extend(data["data"])
                if not data["meta"]["next_page"]:
                    break
                page += 1
            return players
        elif league == "mlb":
            # Get all active MLB players (MLB Stats API)
            url = MLB_STATS_API + "people?hydrate=stats(group=[hitting,pitching,fielding],type=[season])&sportId=1&active=true"
            r = await client.get(url)
            return r.json().get("people", [])
        else:
            return {"error": "Invalid league"}
