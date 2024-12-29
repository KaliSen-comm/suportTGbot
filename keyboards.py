from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='заготовленный вопрос кнопкой', callback_data='vop1')],
    [InlineKeyboardButton(text='заготовленный вопрос кнопкой', callback_data='vop2')],
    [InlineKeyboardButton(text='заготовленный вопрос кнопкой', callback_data='vop3')],
    [InlineKeyboardButton(text='заготовленный вопрос кнопкой', callback_data='vop4')],
    [InlineKeyboardButton(text='заготовленный вопрос кнопкой', callback_data='vop5')],
    [InlineKeyboardButton(text='заготовленный вопрос кнопкой', callback_data='vop6')],
#копируете данный элемент сколько нужно незабыв добавлять хендлер в файле handler.py
#    [InlineKeyboardButton(text='заготовленный вопрос кнопкой', callback_data='vop?')],
    [InlineKeyboardButton(text='заготовленный вопрос кнопкой', callback_data='vop7')] # последний вопрос в этом списке без запятой в конце строки

])

beak = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='main')],

])
