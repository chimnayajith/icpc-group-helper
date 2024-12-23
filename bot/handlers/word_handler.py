from telegram.ext import ConversationHandler, MessageHandler, filters
class WordHandler:
    WAITING_FOR_WORDS = 1 
    def __init__(self, data_manager):
        self.data_manager = data_manager

    async def start_add_word(self, update, context):
        if update.effective_user.id not in self.data_manager.admin_ids:
            await update.message.reply_text("Only admins can add banned words.")
            return ConversationHandler.END

        await update.message.reply_text(
            "Please provide the banned words, each on a new line.\n"
            "For example:\n"
            "word1\n"
            "word2\n"
            "word3\n\n"
            "You can type /cancel to stop this operation."
        )
        return self.WAITING_FOR_WORDS

    async def cancel(self, update, context):
        await update.message.reply_text("Operation canceled.")
        return ConversationHandler.END

    async def receive_words(self, update, context):
        if update.message.text.startswith("/"):
            await update.message.reply_text("Operation canceled.")
            return ConversationHandler.END

        text = update.message.text.strip()
        words = {word.strip().lower() for word in text.splitlines() if word.strip()}

        if not words:
            await update.message.reply_text("No valid words provided. Please try again.")
            return ConversationHandler.END

        new_words = words - self.data_manager.banned_words

        if new_words:
            self.data_manager.banned_words.update(new_words)
            try:
                self.data_manager.save_data()
                await update.message.reply_text(
                    f"Added the following words to the banned list:\n- " + "\n- ".join(sorted(new_words))
                )
            except Exception as e:
                await update.message.reply_text(f"Failed to save data: {e}")
        else:
            await update.message.reply_text(
                "No new words were added (they might already exist in the banned words list)."
            )

        return ConversationHandler.END


    async def remove_word(self, update, context):
        if update.effective_user.id not in self.data_manager.admin_ids:
            await update.message.reply_text("Only admins can remove banned words.")
            return

        if not context.args:
            await update.message.reply_text("Please provide at least one word to remove.")
            return

        removed_words = []
        not_found_words = []
        for word in context.args:
            word = word.lower()
            if word in self.data_manager.banned_words:
                self.data_manager.banned_words.remove(word)
                removed_words.append(word)
            else:
                not_found_words.append(word)

        self.data_manager.save_data()

        if removed_words:
            await update.message.reply_text(f"Removed words: {', '.join(removed_words)}.")
        if not_found_words:
            await update.message.reply_text(f"Words not found in the banned list: {', '.join(not_found_words)}.")
        if not removed_words and not not_found_words:
            await update.message.reply_text("No words were removed (they might not exist in the banned words list).")

    async def list_words(self, update, context):
        if update.effective_user.id not in self.data_manager.admin_ids:
            await update.message.reply_text("Only admins can view banned words.")
            return

        if not self.data_manager.banned_words:
            await update.message.reply_text("There are no banned words in the list.")
            return

        words = "\n- ".join(sorted(self.data_manager.banned_words))
        await update.message.reply_text(f"Banned words: \n- {words}")
