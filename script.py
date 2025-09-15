import requests
import json

def quiz_bot(text):
    BOT_TOKEN = "8052074681:AAGJqQfUkOH-51n-EhJgS6ndrH7LtlATsCQ"
    CHAT_ID = -4021310778

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPoll"


    # Split by commas, strip spaces, ignore empty items
    items = [i.strip() for i in text.strip().split(",") if i.strip()]

    # Group into chunks of 6
    groups = [items[i:i+6] for i in range(0, len(items), 6)]


    for group in groups:
        payload = {
            "chat_id": CHAT_ID,
            "question": group[0],
            "options": group[1:5],  # Must be a list
            "type": "quiz",
            "correct_option_id": int(group[5]),  # Must be int
            "is_anonymous": False,
            "explanation": "Quiz"
        }
        response = requests.post(url, json=payload)  # Use json= instead of data=
        result = response.json()

    if result.get("ok"):
        return "✅ Successful!"
    else:
        return f"❌ Failed: {result}"








def send_message(topic):

    # Replace with your bot token and chat ID
    BOT_TOKEN = "8052074681:AAGJqQfUkOH-51n-EhJgS6ndrH7LtlATsCQ"
    CHAT_ID = -4021310778
    MESSAGE = f"السلام عليكم و رحمة الله, هذه 10 اسالة عن محاضرة {topic}, ارجو منكم حلها"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": MESSAGE
    }

    response = requests.post(url, data=payload)
    result = response.json()

    if result.get("ok"):
        return "✅ Successful!"
    else:
        return f"❌ Failed: {result}"


