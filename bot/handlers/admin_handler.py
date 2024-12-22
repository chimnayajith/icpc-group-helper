from telegram import Update
from telegram.ext import ContextTypes

class AdminHandler:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Available commands:\n"
            "- `/addadmin <user_id>1 <user_id2> ...` - Adds multiple new admins (only accessible to the original admin)\n",
            "- `/addword <word1> <word2> ...` - Adds multiple banned words to the list\n",
            "- `/removeword <word1> <word2> ...` - Removes multiple banned word from the list\n",
            "- `/listwords` - Lists all banned words"
        )

    async def add_admin(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.effective_user.id != int(os.getenv("OG_ADMIN_ID")):
            await update.message.reply_text("Only the original admin can add new admins.")
            return

        new_admins = []
        for user_id in context.args:
            try:
                user_id = int(user_id)
                if user_id not in self.data_manager.admin_ids:
                    self.data_manager.admin_ids.add(user_id)
                    new_admins.append(user_id)
            except ValueError:
                pass

        self.data_manager.save_data()
        await update.message.reply_text(f"Added admins: {', '.join(map(str, new_admins))}.")
