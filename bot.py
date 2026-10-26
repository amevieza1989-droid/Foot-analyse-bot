import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from datetime import datetime

# Le token vient de Render (variable BOT_TOKEN)
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

def analyse_match(text):
    # Sépare les 2 équipes
    if "vs" in text.lower():
        t1, t2 = text.lower().split("vs", 1)
    elif "-" in text:
        t1, t2 = text.split("-", 1)
    else:
        t1, t2 = text, "Adversaire"
    
    t1 = t1.strip().title()
    t2 = t2.strip().title()
    
    if not t2:
        t2 = "Adversaire"

    rapport = f"""⚽ *ANALYSE : {t1} vs {t2}*
🕒 {datetime.now().strftime('%d/%m %H:%M')}

📊 *FORME (5 derniers)*
• {t1} : ✅✅➖❌✅ - 10 pts / 15
• {t2} : ✅❌✅✅➖ - 10 pts / 15

🏠/✈️ *DOMICILE / EXTERIEUR*
• {t1} à domicile : 2.1 buts marqués / match
• {t2} à l'extérieur : 1.3 buts encaissés / match

🤝 *FACE A FACE*
• 4 derniers : {t1} 2 Victoires - 1 Nul - 1 Victoire {t2}
• Moyenne : 2.8 buts par match

📈 *TENDANCES*
• Over 1.5 buts : 82%
• Over 2.5 buts : 64%
• BTTS (les deux marquent) : 58%
• Corners >8.5 : 71%

⚠️ *CONCLUSION V1*
• Match ouvert, tendance buts
• Risque : Moyen
• V2 branchera les vraies stats API

Envoie un autre : ex `Real vs Barca`"""

    return rapport

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salut Boss ! 👋\nEnvoie un match comme ça :\n\n`PSG vs Marseille`\nou `Real - Barca`",
        parse_mode="Markdown"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    result = analyse_match(text)
    await update.message.reply_text(result, parse_mode="Markdown")

if __name__ == "__main__":
    if not BOT_TOKEN:
        print("ERREUR: BOT_TOKEN manquant")
    else:
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        print("Bot lancé...")
        app.run_polling()
