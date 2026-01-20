import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

print("Bot started and listening...")

BOT_TOKEN = os.getenv("BOT_TOKEN")
SOURCE_CHANNEL = "@matchpredictioncricket"
DEST_CHANNEL = "@SessionKingTejasvi"

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN missing")

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        username = update.channel_post.chat.username
        if username and username.lower() == SOURCE_CHANNEL.replace("@", "").lower():
            await context.bot.copy_message(
                chat_id=DEST_CHANNEL,
                from_chat_id=update.channel_post.chat.id,
                message_id=update.channel_post.message_id
            )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()
