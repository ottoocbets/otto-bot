import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💎 VIP Trial", url="https://t.me/ottopredict?text=30-day%20VIP%20Trial%E2%9C%85")],
        [InlineKeyboardButton("💎 Purchase VIP", url="https://t.me/ottopredictions/501")],
        [InlineKeyboardButton("Join Discord", url="https://discord.gg/BT5tDDSp")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Welcome to Otto VIP Bot!\nChoose an option below:",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
