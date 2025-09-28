from fastapi import APIRouter
from api.utils.fetch_data import get_players

router = APIRouter(prefix="/players", tags=["Players"])

@router.get("/mlb")
async def mlb_players():
    return await get_players(league="mlb")

@router.get("/nba")
async def nba_players():
    return await get_players(league="nba")
