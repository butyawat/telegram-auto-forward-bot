print("Bot started and listening...")
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "7257182586:AAHNiunwa309ctqdkOz-Y0TpPlLvZ08EzvM"
SOURCE_CHANNEL = "@+TLVUOKDH81wxOTY1"
DEST_CHANNEL = "@SessionKingTejasvi"

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post and update.channel_post.chat.username == SOURCE_CHANNEL[1:]:
        await context.bot.copy_message(
            chat_id=DEST_CHANNEL,
            from_chat_id=update.channel_post.chat.id,
            message_id=update.channel_post.message_id
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()






