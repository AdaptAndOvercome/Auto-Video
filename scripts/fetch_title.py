import requests

headers = {
    "User-Agent": "auto-story-video-bot"
}

try:
    r = requests.get(
        "https://www.reddit.com/r/AITA/hot.json?limit=20",
        headers=headers,
        timeout=15
    )
    data = r.json()
    titles = [
        c["data"]["title"]
        for c in data["data"]["children"]
        if "data" in c and "title" in c["data"]
    ]
    print(titles[0] if titles else "A situation that changed everything")
except Exception:
    print("A situation that changed everything")
