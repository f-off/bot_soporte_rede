import requests, os

def preguntar_ia(prompt):
    api_key = os.getenv("OPENROUTER_API_KEY")
    r = requests.post("https://openrouter.ai/api/v1/chat/completions", json={
        "model": "mistral/mistral-7b-instruct",
        "messages": [{"role":"user","content":prompt}]
    }, headers={"Authorization":f"Bearer {api_key}"})
    if r.ok:
        return r.json()["choices"][0]["message"]["content"]
    return "❌ Error IA"
