import os
import requests
from flask import Flask, request
from google import genai

TELEGRAM_TOKEN = os.environ.get(class="tok-str">"TELEGRAM_TOKEN","")
GEMINI_API_KEY = os.environ.get(class="tok-str">"GEMINI_API_KEY","")
GEMINI_MODEL = "gemini-3.5-flash-lite"

app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return "Startap Shark Bot is running!", 200

    # tpc/ip
    # udp
    # 1xx - информационные
    # 100 Continue --> сервер получил начало запроса
    # и ждет остальную часть данных
    # 101 -> Switch protocols --> Сервер готов сменить протокол
    # 2xx
    # 200 --> OK --> успешный результат
    # 201 --> Created -> запрос выполнен, создан новый ресурс
    # 202 --> Accepted -> Запрос принят в обработку, но еще не завершен
    # 204 --> Not Content --> Запрос выполнен,
    # Но тело ответа отсутствует
    # 3xx -> Перенаправления(редиректоры)
    # 302 --> Found -> Временный перенос ресурса
    # 4xx -> Ошибки клиета
    # 400 --> Bad request --> неккоректный запрос
    # 401 --> Unauthorized -> Требуется аутентификация
    # 403 --> Forbidden -> Доступ к ресурсу запрещен даже при наличии аутентификации
    # 404 --> Not Found -> Запрошенный ресурс не найден
    # 408 --> Request Timeout --> сервер не дождался полного запроса от клиента за определенное время
    # 429 --> Too many requests -> Превышен лимит запросов за единицу время.
    # 5xx -> Ошибки сервера
    # 500 --> Internal Server Error - внутренняя ошибка сервера
    # 502 --> Bad Gateway -> шлюз получил неккоректный ответ от вышестоящего сервера 
    # 503 --> Service Unavailable -> Сервис времено недоступен
    # (Техработы,перезагрузка сервера)

class StartupPitch:
    def __init__(self,author,idea,score,verdict,comment)
    self.author  = author
    self.idea = idea
    self.score = score
    self.verdict = verdict
    self.comment = comment
def format_card(self):
    return (
        if "СТАРТАП-ПИТЧ ОТ : {self.author}\n",
        f"Идея : {self.idea}\n\n",
        f"Оценка инвестора: {self.score}/100\n",
        f"Вердикт : {self.verdict}\n",
        f"Разбор от инвестора : {self.comment}"
        

    )
