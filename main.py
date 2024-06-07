from fastapi import FastAPI


app = FastAPI(
    title="Trading App"
)

fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"}
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 123, "amount": 2.12}
]


@app.get("/users/{user_id}")
def get_user(user_id: int) -> list:
    return [user for user in fake_users if user.get("id") == user_id]


@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str) -> dict:
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
    current_user["name"] = new_name
    return {"status": 200, "user": current_user}


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 1) -> list:
    return fake_trades[offset:][:limit]
