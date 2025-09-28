# Sports Odds & Player Data API

A modern FastAPI-based project to fetch real-time odds and player data for MLB and NBA.  
Supports REST API endpoints, code examples, and Docker deployment.

## Features

- Real-time odds for MLB and NBA games
- Player roster and stats endpoints
- Easy integration (REST API)
- Dockerized for deployment
- Python code examples

## API Endpoints

| Endpoint           | Description                     |
|--------------------|---------------------------------|
| `/odds/mlb`        | Get real-time MLB odds          |
| `/odds/nba`        | Get real-time NBA odds          |
| `/players/mlb`     | MLB player roster/stats         |
| `/players/nba`     | NBA player roster/stats         |

## Setup

1. Clone the repository.
2. Copy `.env.example` to `.env` and add your API keys.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run locally:

   ```bash
   uvicorn api.main:app --reload
   ```

5. Or use Docker:

   ```bash
   docker build -t sports-odds-api .
   docker run --env-file .env -p 8000:8000 sports-odds-api
   ```

## Example Usage

See [`examples/python_example.py`](examples/python_example.py) for how to call the endpoints.

## Data Sources

- Odds: [The Odds API](https://the-odds-api.com/), [OddsAPI](https://oddsapi.io/)
- NBA: [balldontlie](https://www.balldontlie.io/)
- MLB: [MLB-Stats API](https://appac.github.io/mlb-data-api-docs/)
