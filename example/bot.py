from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from os import getenv

# Define a few command handlers.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(text="hello world!")
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(text="help me!")

async def bot_tele(text):
    # Create application
    application = (
        Application.builder().token(getenv("7034825032:AAFBesPJ6cVFfsURYk4S61Ke0TYjMOPLXRo")).build()
    )

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))

    # Start application
    await application.bot.set_webhook(url=getenv("https://telegram-bot-ruddy.vercel.app"))
    await application.update_queue.put(
            Update.de_json(data=text, bot=application.bot)
        )
    async with application:
        await application.start()
        await application.stop()
