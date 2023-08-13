import requests


def send(token, receiverId, msg):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    resp = requests.post(
        url,
        json={"chat_id": receiverId, "text": msg}
    )

    if resp.status_code != 200:
        raise Exception("Something went wrong: " + resp.text)
