from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
import random


app = FastAPI()
templates = Jinja2Templates(directory="templates")

otkritka = [
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

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/otkritka")
async def otkritka(request: Request):
    random.shuffle(otkritka)
    return templates.TemplateResponse("otkritka.html", {
        "request": request,
        "otkr": otkritka
                                                        })


@app.get("/create/otkritka")
async def create(title: str, emoji: str, text: str):
    otkritka.append({"title": title, "text": text, "emoji": emoji})
    if (title==None) or (text==None) or (emoji==None):
        return {"message": "Ошибка"}
    return {"Открытка добавлена"}