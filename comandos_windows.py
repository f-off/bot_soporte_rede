import os

def listar_procesos():
    try:
        salida = os.popen('tasklist').read()
        return salida[:4000]
    except Exception as e:
        return f"❌ Error listando procesos: {e}"
