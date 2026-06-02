import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '' # Insert your bot token here

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def get_crypto_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['price']
                else:
                    print(f"Binance API Error: Status {response.status}")
                    return "Error"
    except Exception as e:
        print(f"Network error: {e}")
        return "Error"

async def send_price(message: types.Message, symbol: str):
    price = await get_crypto_price(symbol)
    
    if price == "Error":
        await message.answer("Failed to retrieve data from the Binance server.")
        return

    pretty_price = f"{float(price):,.2f}".replace(',', ' ')
    await message.answer(f"Current {symbol} price: ${pretty_price}")

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    welcome_text = (
        "Hello! I'm crypto bot.\n"
        "Available commands:\n"
        "/btc - Bitcoin\n"
        "/eth - Ethereum\n"
        "/bnb - Binance Coin\n"
        "/sol - Solana"
    )
    await message.reply(welcome_text)

@dp.message(Command("btc"))
async def btc_command(message: types.Message):
    await send_price(message, "BTC")

@dp.message(Command("eth"))
async def eth_command(message: types.Message):
    await send_price(message, "ETH")

@dp.message(Command("bnb"))
async def bnb_command(message: types.Message):
    await send_price(message, "BNB")

@dp.message(Command("sol"))
async def sol_command(message: types.Message):
    await send_price(message, "SOL")

async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())