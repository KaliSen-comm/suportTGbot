from aiogram import Router, F, types, Bot
from aiogram.types import Message, CallbackQuery, message

import keyboards as kb


router = Router()


@router.callback_query(F.data == 'vop1')
async def vop1(callback: CallbackQuery):
    await callback.message.edit_text('Ответ на вопрос 1'
                                     , reply_markup=kb.beak)

@router.callback_query(F.data == 'vop2')
async def vop1(callback: CallbackQuery):
    await callback.message.edit_text('Ответ на вопрос 2'
                                     , reply_markup=kb.beak)

@router.callback_query(F.data == 'vop3')
async def vop1(callback: CallbackQuery):
    await callback.message.edit_text('Ответ на вопрос 3'
                                     , reply_markup=kb.beak)


@router.callback_query(F.data == 'vop4')
async def vop1(callback: CallbackQuery):
    await callback.message.edit_text('Ответ на вопрос 4'
                                     , reply_markup=kb.beak)


@router.callback_query(F.data == 'vop5')
async def vop1(callback: CallbackQuery):
    await callback.message.edit_text('Ответ на вопрос 5'
                                     , reply_markup=kb.beak)


@router.callback_query(F.data == 'vop6')
async def vop1(callback: CallbackQuery):
    await callback.message.edit_text('Ответ на вопрос 6'
                                     , reply_markup=kb.beak)


@router.callback_query(F.data == 'vop7')
async def vop1(callback: CallbackQuery):
    await callback.message.edit_text('Ответ на вопрос 7'
                                     , reply_markup=kb.beak)
#для добавления новых вопросов копируете элемент сколько нужно
#@router.callback_query(F.data == 'vop?')
#async def vop1(callback: CallbackQuery):
#    await callback.message.edit_text('Ответ на вопрос ?'
                                     , reply_markup=kb.beak)

@router.callback_query(F.data == 'main')
async def main(callback: CallbackQuery):
    await callback.answer('Вы вернулись')
    await callback.message.edit_text('' 
                               
                              "\n" "\nВыберите свой вопрос из списка вопросов📋"
                            "\n"
                            '\nЕсли не нашли своего вопроса - напишите его прямо в ЧАТ этого бота 💬'
,
                                     reply_markup=kb.main)
