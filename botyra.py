import asyncio
import logging
import red

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command,CommandObject
f=open('C:/Users/user/Desktop/boting/token.txt')
# Bot token can be obtained via https://t.me/BotFather
logging.basicConfig(level=logging.INFO)
TOKEN = f.readline()
# All handlers should be attached to the Router (or Dispatcher)
bot = Bot(TOKEN)
dp = Dispatcher()
helptext='доступные команды : \n/start \n/s (ваш снилс), данная команда позволяет узнать поступили ли вы в пгниу в этом году и куда  \n(снилс вводится по следущему типу: 999-999-999 99 )'

@dp.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    name=message.from_user.full_name
    await message.answer("привет "+name+', я - psucontestbot, пока что я умею только говорить поступили ли в пгниу в этом году или нет')
    
@dp.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    return await message.answer(helptext)
    




@dp.message(Command('s'))
async def command_give_snils_handler(message: Message, command:CommandObject) -> None:
    sl=command.args
    if command.args is None:
        return await message.answer('я не принимаю эту команду пустой, \n снилс вводится после команды через пробел по следущему типу: 999-999-999 99 ')
    if not ((len(sl)==14 and sl[0].isdigit()) or len(sl)==11) : #ищем снилсы 
        return await message.answer("это не похоже на снилс, попробуйте еще раз")
    print(sl)
    print(red.readfile(sl))
    ans=red.readfile(sl)
    if ans == None:
        return await message.answer('увы, вы не поступили в пгниу или снилс введен некоректно')
    return await message.answer("поздравляю , вы поступили на направление:"+ans)
async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
