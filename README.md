# CryptoBot Telegram

A Telegram bot to check cryptocurrency prices via Binance API.

## Prerequisites

- Python 3.7 or newer.
- Telegram application.

## Step 1: Get a Telegram Bot Token

1. Open Telegram and search for "@BotFather".
2. Send the /newbot command.
3. Type a name and username for your bot.
4. Copy the API token provided by BotFather.

## Step 2: Installation

1. Clone the repository:
   git clone https://github.com/Mr-Ordinary-UA/CryptoBot_Telegram.git
2. Go to the project directory:
   cd CryptoBot_Telegram
3. Set up a virtual environment:
   Windows: python -m venv venv
   Linux/macOS/Termux: python3 -m venv venv
4. Activate the virtual environment:
   Windows: venv\Scripts\activate
   Linux/macOS/Termux: source venv/bin/activate
5. Install required packages:
   Windows: pip install -r requirements.txt
   Linux/macOS/Termux: pip3 install -r requirements.txt

## Step 3: Configuration

1. Open the bot.py file.
2. Find the API_TOKEN variable.
3. Paste your token inside the quotes.
WARNING: Do not commit the bot.py file to a public repository if it contains your active token.

## Step 4: Run the Bot

1. Ensure the virtual environment is active.
2. Run the program:
   Windows: python bot.py
   Linux/macOS/Termux: python3 bot.py
3. Open your bot in Telegram and send the /start command.

## Commands

- /start : Show available commands
- /btc : Get Bitcoin price
- /eth : Get Ethereum price
- /bnb : Get Binance Coin price
- /sol : Get Solana price