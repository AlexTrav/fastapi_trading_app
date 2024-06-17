from datetime import datetime
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing_extensions import List, Optional


app = FastAPI(
    title="Trading App"
)

fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
    {"id": 4, "role": "investor", "name": "Homer", "degree": [
        {"id": 1, "created_at": "2024-01-01T00:00:00", "type_degree": "expert"}
    ]}
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 123, "amount": 2.12}
]


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=10)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int) -> list:
    return [user for user in fake_users if user.get("id") == user_id]


@app.post("/trades")
def add_trades(trades: List[Trade]):
    for trade in trades:
        fake_trades.append(trade.dict())
    return {"status": 200, "data": fake_trades}
