class WordHandler:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    async def add_word(self, update, context):
        if update.effective_user.id not in self.data_manager.admin_ids:
            await update.message.reply_text("Only admins can add banned words.")
            return

        if not context.args:
            await update.message.reply_text("Please provide at least one word to add.")
            return

        new_words = []
        for word in context.args:
            word = word.lower()
            if word not in self.data_manager.banned_words:
                self.data_manager.banned_words.add(word)
                new_words.append(word)

        self.data_manager.save_data()

        if new_words:
            await update.message.reply_text(f"Added words: {', '.join(new_words)}.")
        else:
            await update.message.reply_text("No new words were added (they might already exist in the banned words list).")

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
        await update.message.reply_text(f"Banned words: {words}")
