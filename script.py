import requests
import json

def quiz_bot(text):
    BOT_TOKEN = "8369470525:AAFpexj-b3QUt8eo8588TyLwjqMr9ARRSEc"
    CHAT_ID = -1002593491038
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPoll"

    # Split by commas, strip spaces, ignore empty items
    items = [i.strip() for i in text.strip().split(",") if i.strip()]

    # Validate input
    if len(items) % 6 != 0:
        return "Error: Invalid input format. Each question must have 4 options and a correct index."

    # Group into chunks of 6
    groups = [items[i:i+6] for i in range(0, len(items), 6)]

    for idx, group in enumerate(groups, 1):
        question = group[0].strip('"').strip()
        options = [o.strip('"').strip() for o in group[1:5]]


        try:
            correct_option_id = int(group[5])
            if correct_option_id < 0 or correct_option_id > 3:
                return f"Error: Correct option index out of range for question {idx}"
        except ValueError:
            return f"Error: Correct option index must be an integer for question {idx}"

        payload = {
            "chat_id": CHAT_ID,
            "question": question,
            "options": json.dumps(options),
            "type": "quiz",
            "correct_option_id": correct_option_id,
            "is_anonymous": True,
            "explanation": "Quiz"
        }

        response = requests.post(url, data=payload)
        if response.status_code != 200:
            return f"Error sending question {idx}: {response.text}"

    return "All questions sent successfully!"
