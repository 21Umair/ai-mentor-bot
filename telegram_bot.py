import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from app.chatbot import Chatbot


load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Chatbot()

async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    "This function runs when the user sends /start on Telegram."
    welcome_message = (
        "Hello! I am your AI Career Mentor Bot.\n\n"
        "I can guide you based on your current AI/ML level.\n\n"
        "Are you a beginner, intermediate, or advanced?\n\n"
        "You can also say things like:\n"
        "- I know python basics\n"
        "- I have built ML projects\n"
        "- I have worked with LLMs"
    )

    await update.message.reply_text(welcome_message)

async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    "This function runs when the usersends /help on Telegram."
    help_message = (
        "You can ask me about:\n\n"
        "- Python roadmap\n"
        "- Machine learning\n"
        "- Deep learning\n"
        "- NLP\n"
        "- Computer vision\n"
        "- RAG\n"
        "- LLM fine-tuning\n"
        "- AI agents\n"
        "- Deployment\n"
        "- Portfolio projects\n\n"
        "Example messages:\n"
        "I am a beginner\n"
        "I know Python and machine learning\n"
        "What projects should I build?\n"
        "How to deploy ML model?"
    )

    await update.message.reply_text(help_message)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    "This function runs whenever the user sends a normal text message."
    user_message = update.message.text
    reply = bot.get_reply(user_message)
    await update.message.reply_text(reply)

def main():
    "Start the Telegram bot"

    if not TELEGRAM_BOT_TOKEN:
        raise ValueError(
            "TELEGRAM_BOT_TOKEN is missing."
            "Please add to your .env or verify it."
        )
    
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__=="__main__":
    main()