import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token pris depuis Render
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚽ Bot Boss en ligne !\nTape /analyse pour tester")

async def analyse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Analyse Over 1.5 prête ! Bot fonctionne parfaitement.")

if __name__ == "__main__":
    if not TOKEN:
        print("ERREUR: BOT_TOKEN manquant dans Render")
    else:
        print("Bot demarre...")
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("analyse", analyse))
        app.run_polling()
