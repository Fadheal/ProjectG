from fastapi import FastAPI, HTTPException
app = FastAPI()
from scraper.coingecko import pixels_coin

@app.get("/")
def root():
    return {"Hello Mas Udang"}

@app.get("/api/v1/scrap/coingecko/pixels/prices")
def coin_gecko():
    return pixels_coin()