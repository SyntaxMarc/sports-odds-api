from fastapi import FastAPI
from api.routes import odds, players

app = FastAPI(
    title="Sports Odds & Player Data API",
    description="Real-time odds and player data for MLB and NBA.",
    version="0.1.0"
)

app.include_router(odds.router)
app.include_router(players.router)
