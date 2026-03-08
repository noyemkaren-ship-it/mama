from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

otkritki_data = [
    {
        "title": "С 8 Марта, мама!",
        "text": "Дорогая мама! Поздравляю тебя с 8 Марта. Спасибо за твою заботу, доброту и любовь. Ты самая лучшая мама!",
        "emoji": "🌷💖🌸"
    },
    {
        "title": "Любимой маме",
        "text": "Мамочка, с праздником! Пусть у тебя всегда будет хорошее настроение, крепкое здоровье и много счастливых дней.",
        "emoji": "💐🌹💖"
    },
    {
        "title": "С праздником весны",
        "text": "Мама, поздравляю тебя с 8 Марта! Желаю счастья, радости и чтобы каждый день был наполнен улыбками.",
        "emoji": "🌸🌷✨"
    },
    {
        "title": "Самой лучшей маме",
        "text": "Ты самая добрая, заботливая и любимая мама. Спасибо за всё! С 8 Марта!",
        "emoji": "💖🌷💐"
    }
]

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/otkritka", response_class=HTMLResponse)
async def otkritka(request: Request):
    cards = otkritki_data.copy()
    random.shuffle(cards)
    return templates.TemplateResponse(
        "otkritka.html",
        {
            "request": request,
            "otkritka": cards
        }
    )