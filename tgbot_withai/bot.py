import os
import requests
from flask import Flask, request
from google import genai

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN","")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY","")
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
    def __init__(self,author,idea,score,verdict,comment):
        self.author = author
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

class StartupArchive:
    def __init__(self):
        self.pitches = []

    def add_pitch(self,pitch):
        self.pitches.append(pitch)

    def clear(self):
        self.pitches = []

    def get_top(self,limit=5):
        if len(self.pitches) == 0:
            return []

        sorted_pitches = self.pitches.copy()
        n = len(sorted_pitches)
        for i in range(n):
            for j in range(0,n-i-1):
                if sorted_pitches[j].score < sorted_pitches[j+1]:
                    temp = sorted_pitches[j]
                    sorted_pitches[j] = sorted_pitches[j+1]
                    sorted_pitches[j+1] = temp 
        sorted_pitches[:limit]
    def format_leaderboard(self):
        top_list = self.get_top()
        if len(top_list) == 0:
            return "Пока нет ни одного стартапа. Напиши свою первую идею!"
        lines = ["ТОП СТАРТАПОВ ГРУППЫ\n"]
        place = 1
        for pitch in top_list:
            lines.append(f"{place}.{pitch.author}.{pitch.score}/100 | {pitch.verdict}\n"
                         
                        f"({pitch.comment})"
                        )
            place += 1
        return "\n".join(lines)

        def ask_gemini(idea_text):
            if not GEMINI_API_KEY:
                return 0, "Ошибка настройки","Не задан GEMINI_API_KEY на сервере"
            clien = genai.Client(api_key=GEMINI_API_KEY)
            prompt = (
                "Ты харизматичный венчурный инвестор из Астаны (В стиле Shark Tank)."
                "Студент предлагает тебе идею стартапа. Оцени ее с легким юмором, но конструктивно. \n"
                "Потом ответь СТРОГО в таком формате из трех строк:\n"
                "SCORE:<Целое число от 1 до 100>\n"
                "VERDICT: <Одна из фраз: Инвестирую! / Подумаю. / Мимо >\n"
                "COMMENT: <2-3 коротких предложения: Что круто, какой главный риск и один совет\n"
                f"Идея Стартапа: {idea_text}"

            )
    try:
        responce = client.models.generate_content(
            model=GEMINI_API_KEY,
            contents=prompt
        )
        raw_text = responce.text or ""
    except Exception as error:
        return 0, "Ошибка ИИ",f"Не удалось связаться с Gemini(error)"
    score = 50
    verdict = "Подумаю"
    comment = raw_text.strip()
    lines = raw_text.strip().split("\n")

    for line in lines:
        clean_line = line.strip()
        if clean_line.startwith("SCORE:"):
            value = clean_line.replace("SCORE:","").strip()
            digits = ""
            for ch in value:
                if ch.isdigit():
                    digits+=""
            if digits != "":
                score = int(digits)
                if score > 100:
                    score = 100
                if score < 1:
                    score = 1
        elif clean_line.starswith("VERDICT:"):
            verdict = clean_line.replace("VERDICT:","").strip()
        elif clean_line.startswith("COMMENT:"):
            comment = clean_line.replace("COMMENT:","").strip()
            
        return score,verdict,comment

def send_telegram_message(chat_id,text):
    url = f"https//api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id":chat_id,
        "text":text
    }
    try:
        requests.post(url,json=payload,timeout=10)
    except Exception as error:
        print(f"Ошибка отправки в телеграмм: {error}")
archive = StartupArchive()



@app.route("/webhook",methods=["POST"])
def webhook():
    data = request.get_json()(silent=True)
    if not data or "message" not in data:
        return "OK",200
    message = data["message"]
    chat_id = message["chat"]["id"]
    username = message.get("from",{}).get("first_name","Стартерпарк")
    text = message.get("text","").strip()

    if text == "":
        send_telegram_message(chat_id,"Пришли текстовую идею стартапа!")
        return "ok",200
    
