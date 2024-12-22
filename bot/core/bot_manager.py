from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.handlers.admin_handler import AdminHandler
from bot.handlers.word_handler import WordHandler
from bot.handlers.moderation_handler import ModerationHandler
from bot.core.data_manager import DataManager

class BotManager:
    def __init__(self, token: str):
        self.token = token
        print("Fetching data from settings...")
        self.data_manager = DataManager()
        print("Data loaded successfully ✅")

        self.admin_handler = AdminHandler(self.data_manager)
        self.word_handler = WordHandler(self.data_manager)
        self.moderation_handler = ModerationHandler(self.data_manager)

    def run(self):
        application = Application.builder().token(self.token).build()

        print("\nRegistering handlers...")
        application.add_handler(CommandHandler("start", self.admin_handler.start))
        application.add_handler(CommandHandler("addadmin", self.admin_handler.add_admin))
        application.add_handler(CommandHandler("addword", self.word_handler.add_word))
        application.add_handler(CommandHandler("removeword", self.word_handler.remove_word))
        application.add_handler(CommandHandler("listwords", self.word_handler.list_words))
        application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.moderation_handler.handle_message)
        )
        print("Handlers registered successfully ✅")
        print("\nBot is running ✅")

        application.run_polling()
