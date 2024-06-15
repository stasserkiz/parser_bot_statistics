## Встановлення

1. Клонуйте репозиторій:

   git clone https://github.com/stasserkiz/parser_bot_statistics

2. Встановіть усі залежності 

pip install -r requirements.txt

3.  Запустіть проект 
python main.py


## Структура проекту 

main.py: Основний файл програми, який містить логіку запуску парсера та Telegram бота.
parser/job_parser.py: Модуль для парсингу веб-сторінок і збереження даних у базу даних.
data/database.py: Налаштування бази даних SQLAlchemy та ORM модель для зберігання даних про вакансії.
bot/handlers.py: Обробники для Telegram бота, включаючи обробку команд та відправку статистики.