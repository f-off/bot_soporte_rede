import requests
import os

def preguntar_ia(prompt):
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        return "⚠️ No se encontró la API KEY. Verificá tus variables de entorno en Replit."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openchat/openchat-3.5",
        "messages": [
            {"role": "system", "content": "Sos un asistente experto en redes, soporte técnico e informática. Responde en español de forma clara y profesional."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        r = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
        if r.ok:
            return r.json()["choices"][0]["message"]["content"]
        else:
            return f"❌ Error IA: {r.status_code}\n{r.text}"
    except Exception as e:
        return f"❌ Excepción al conectar con OpenRouter:\n{e}"
