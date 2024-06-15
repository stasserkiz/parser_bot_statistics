import asyncio
import schedule
from aiogram import Bot
from parser.job_parser import get_count_advertisement, save_to_db
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import config
from bot.handlers import dp

bot = Bot(token=config.BOT_TOKEN)

async def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    service = Service(r"C:\Users\Стас\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        url = "https://robota.ua/ru/zapros/junior/ukraine"
        count = await get_count_advertisement(url, driver)
        print(f"In this page {count} vacancies")

        await save_to_db(count)
    finally:
        driver.quit()

async def start_bot():
    await dp.start_polling(bot)

async def scheduler():
    schedule.every(1).hour.do(lambda: asyncio.create_task(main()))

    await main()
    
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

async def main_async():
    await asyncio.gather(scheduler(), dp.start_polling(bot))

if __name__ == "__main__":
    asyncio.run(main_async())