import subprocess

def hacer_ping(dominio):
    try:
        return subprocess.check_output(["ping","-c","4",dominio], universal_newlines=True)
    except Exception as e:
        return f"❌ Error ping: {e}"
