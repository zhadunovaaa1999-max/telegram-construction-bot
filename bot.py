from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = "8753592979:AAGZzoir2ILs_vGgXjP4uDed85RJNDVSQjA"

SOURCE_CHAT_ID = -1003094340818
TARGET_CHAT_ID = -1003986281476

TOPICS = {
    "#СевернаяЖемчужина": 4,
    "#СевернаяЖемчужина2": 6,
    "#Электроаппарат": 8,
    "#Колоколец": 10,
    "#Низино": 12,
    "#Кулакова": 14,
}


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    if update.message.chat_id != SOURCE_CHAT_ID:
        return

    text = update.message.caption or update.message.text or ""
    text_lower = text.lower()

    topic_id = None

    for tag, thread_id in TOPICS.items():
        if tag in text_lower:
            topic_id = thread_id
            break

    if not topic_id:
        return

    try:
        await context.bot.copy_message(
            chat_id=TARGET_CHAT_ID,
            from_chat_id=SOURCE_CHAT_ID,
            message_id=update.message.message_id,
            message_thread_id=topic_id,
        )

        print(f"Copied to topic {topic_id}")

    except Exception as e:
        print(e)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.ALL,
        handle_message
    )
)

print("BOT STARTED")

app.run_polling()
