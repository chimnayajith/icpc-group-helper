# ICPC Group Helper Bot

Telegram bot designed to assist with deleting messages and kicking the users who use certain banned words

## Features

- Add or remove admins
- Add, remove, and list banned words
- Delete and ban users who use banned words

## Prerequisites

Before running the bot, ensure you have the following:

- Python 3.8+ installed
- A virtual environment to manage dependencies
- A `.env` file with your bot's Telegram token and other configuration settings

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/chimnayajith/icpc_group_helper.git
cd icpc_group_helper
```

### 2. Create a virtual environment (if not already created)

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

- **On macOS/Linux:**

```bash
source venv/bin/activate
```

- **On Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

Create a `.env` file in the root directory with the following content:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
OG_ADMIN_ID=your_admin_id_here
```

Replace `your_bot_token_here` with the bot token you received from [BotFather](https://telegram.me/BotFather) and `your_admin_id_here` with your [Telegram user ID](https://telegram.me/userinfobot). 

### 6. Run the bot

Once everything is set up, you can start the bot by running:

```bash
python bot.py
```

The bot will begin running and will listen for commands.

## Usage

### Available Commands:

- `/start` - Displays all available commands
- `/addadmin <user_id>1 <user_id2> ...` - Adds multiple new admins (only accessible to the original admin)
- `/addword <word1> <word2> ...` - Adds multiple banned words to the list
- `/removeword <word1> <word2> ...` - Removes multiple banned word from the list
- `/listwords` - Lists all banned words

The bot will automatically delete and ban users who send messages containing any banned words.