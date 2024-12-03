import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from config_data import config
from handlers.client.handlers_client import router as router_client
from handlers.admin.handlers_admin import router as router_admin

async def main():
    # Инициализация бота с токеном и режимом парсинга
    bot = Bot(token=config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    
    # Подключение маршрутизаторов
    dp.include_router(router=router_client)
    dp.include_router(router=router_admin)
    
    # Удаление вебхука (если был установлен) и запус опроса
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    
if __name__ == '__main__':
    # Настройка логирования
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
            print('Программа завершена')
