class ModerationHandler:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    async def handle_message(self, update, context):
        if not update.message or not update.message.text:
            return

        text = update.message.text.lower()
        if any(word in text for word in self.data_manager.banned_words):
            try:
                await update.message.delete()
                await context.bot.ban_chat_member(update.message.chat_id, update.message.from_user.id)
                await context.bot.send_message(
                    chat_id=update.message.chat_id,
                    text=f"User {update.message.from_user.name} was banned for using banned words."
                )
            except Exception as e:
                print(f"Error banning user: {e}")
