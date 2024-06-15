from aiogram import types
from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import FSInputFile
import aiosqlite
import pandas as pd
import os 

dp = Dispatcher()

@dp.message(Command("get_today_statistic"))
async def get_today_statistic(message: types.Message):
    db_path = "C:/Users/Стас/Desktop/Нова папка/data/job_data.db"
    
    async with aiosqlite.connect(db_path) as conn:
        async with conn.execute("SELECT * FROM job_data") as cursor:
            records = await cursor.fetchall()
            
    if records:
        df = pd.DataFrame(records, columns=['id', 'parsed_at', 'vacancy_count'])
        df = df.drop("id", axis=1)
        df['change'] = df['vacancy_count'].diff().fillna(0)
        
        excel_file_path = 'C:/Users/Стас/Desktop/Нова папка/data/all_records.xlsx'

        df.to_excel(excel_file_path, index=False)

        await message.answer_document(document=FSInputFile(excel_file_path), caption="Статистика")
        
        os.remove(excel_file_path)
    else:
        await message.reply("Записів в базі даних немає.")



