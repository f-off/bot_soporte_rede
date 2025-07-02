import telebot
import os
from comandos_redes import hacer_ping
from comandos_windows import listar_procesos
from ai_chat import preguntar_ia
from keep_alive import mantener_vivo

mantener_vivo()
bot = telebot.TeleBot(os.getenv("KEY_BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def cmd_start(m):
    bot.reply_to(m, "🤖 Hola, soy tu bot de soporte técnico. Enviame comandos:\n/ping dominio.com\n/procesos\n/ia pregunta")

@bot.message_handler(commands=['ping'])
def cmd_ping(m):
    try:
        dominio = m.text.split(" ",1)[1]
        bot.reply_to(m,f"📡 Resultado:\n{hacer_ping(dominio)}")
    except:
        bot.reply_to(m,"⚠️ Uso: /ping dominio.com", parse_mode="Markdown")

@bot.message_handler(commands=['procesos'])
def cmd_procesos(m):
    bot.reply_to(m, f"🧠 Procesos:\n{listar_procesos()}")

@bot.message_handler(commands=['ia'])
def cmd_ia(m):
    if len(m.text.split(" ",1))>1:
        bot.reply_to(m,"💭 Pensando...")
        bot.reply_to(m,f"🤖 IA: {preguntar_ia(m.text.split(' ',1)[1])}")
    else:
        bot.reply_to(m,"❓ Escribí algo luego de /ia")

bot.infinity_polling()
