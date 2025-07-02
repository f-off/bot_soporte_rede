import requests

def preguntar_ia(prompt):
    try:
        respuesta = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )
        if respuesta.ok:
            return respuesta.json()["response"]
        else:
            return f"❌ Error IA local: {respuesta.status_code}"
    except Exception as e:
        return f"❌ No se pudo conectar con la IA local:\n{e}"
