import os
from dotenv import load_dotenv
from bot.core.bot_manager import BotManager

load_dotenv()

if __name__ == "__main__":
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set in the environment.")

    bot_manager = BotManager(TOKEN)
    bot_manager.run()