from fastapi import APIRouter
from api.utils.fetch_data import get_odds

router = APIRouter(prefix="/odds", tags=["Odds"])

@router.get("/mlb")
async def mlb_odds():
    return await get_odds(sport="baseball_mlb")

@router.get("/nba")
async def nba_odds():
    return await get_odds(sport="basketball_nba")
