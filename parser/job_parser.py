import asyncio
import aiosqlite
from selenium.webdriver.common.by import By
from data.database import JobData, Session, engine


async def get_count_advertisement(url, driver):
    try:
        driver.get(url)
        await asyncio.sleep(3)
        count_element = driver.find_element(By.XPATH, '/html/body/app-root/div/alliance-jobseeker-vacancies-root-page/div/alliance-jobseeker-desktop-vacancies-page/main/section/div/div/lib-desktop-top-info/div/div/div')
        count_text = count_element.text
        count = int(''.join(filter(str.isdigit, count_text)))
    except Exception as e:
        print(f"Помилка при отриманні кількості вакансій: {e}")
        count = 0
    return count

async def save_to_db(vacancy_count):
    Session.configure(bind=engine)
    session = Session()
    
    try:
        job_data = JobData(vacancy_count=vacancy_count)
        session.add(job_data)
        session.commit()
        print(f"Дані про вакансії збережено в базу даних. ID={job_data.id}")
    finally:
        session.close()
