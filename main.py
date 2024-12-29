from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging
import keyboards as kb
from handler import router

#WORK



async def main():
    # Вставьте токен вашего бота
    BOT_TOKEN = ""
    ADMIN_ID =   # Замените на ID администратора

    # Настройка логирования
    logging.basicConfig(level=logging.INFO)

    # Инициализация бота и диспетчера
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)


    # Хранение обратной связи пользователей
    user_messages = {}

    @dp.message(Command(commands=["start", "help"]))
    async def send_welcome(message: types.Message):
       await message.answer(' Привет, это бот техподдержки VPNProtectorBot🤖' 
                               
                              "\n" "\nВыберите свой вопрос из списка вопросов📋"
                            "\n"
                            '\nЕсли не нашли своего вопроса - напишите его прямо в ЧАТ этого бота 💬'

                            , reply_markup=kb.main)

    @dp.message(lambda message: message.chat.id != ADMIN_ID)
    async def handle_user_message(message: types.Message):
        """Обрабатывает сообщения пользователей и пересылает их администратору."""
        user_id = message.chat.id
        user_messages[message.message_id] = user_id

        # Пересылаем сообщение администратору с указанием reply_to_message_id
        forward_message = await bot.send_message(
            ADMIN_ID,
            f"Сообщение от {message.from_user.full_name} (@{message.from_user.username}) (ID: {user_id}):\n{message.text}"
        )

        # Сохраняем соответствие пересланного сообщения
        user_messages[forward_message.message_id] = user_id
        await message.reply("Ваше сообщение отправлено нашему оператору техподдержки.")

    @dp.message(lambda message: message.chat.id == ADMIN_ID)
    async def handle_admin_reply(message: types.Message):
        """Обрабатывает ответы администратора и пересылает их пользователю через реплай."""
        try:
            if message.reply_to_message and message.reply_to_message.message_id in user_messages:
                user_id = user_messages[message.reply_to_message.message_id]
                await bot.send_message(user_id, f"Ответ от администратора:\n{message.text}")
                await message.reply("Ответ отправлен пользователю.")
            else:
                await message.reply("Пожалуйста, ответьте на сообщение пользователя, чтобы отправить ответ.")
        except Exception as e:
            logging.error(f"Ошибка при отправке ответа пользователю: {e}")
            await message.reply("Произошла ошибка при отправке ответа пользователю.")

    async def main():
        # Запуск диспетчера
        try:
            await dp.start_polling(bot)
        except Exception as e:
            logging.critical(f"Критическая ошибка при запуске бота: {e}")

    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
