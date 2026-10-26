import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚽ Bot foot en ligne Boss ! Tape /analyse")

async def analyse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Analyse Over 1.5 activée ✅")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analyse", analyse))
    app.run_polling()
