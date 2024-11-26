from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



api = '7539261653:AAE1xDsK4vPWU1fxV9GzSf5xd6Mz6A91fU8'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

menu = ReplyKeyboardMarkup([
    [KeyboardButton(text='Информация'),KeyboardButton(text='Купить')]
],
resize_keyboard=True)

inline_products = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Ретро-телефон', callback_data='product_buying'),
         InlineKeyboardButton(text='Ретро-холодильник', callback_data='product_buying'),
         InlineKeyboardButton(text='Ретро-компьютер', callback_data='product_buying'),
         InlineKeyboardButton(text='Ретро-плеер', callback_data='product_buying')]
    ]
)



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for i in range(1, 5):
        await message.answer(f'Название: {i} | Описание: описание {i} | Цена: {i*100}' )
        print(f'Название: {i} | Описание: описание {i} | Цена: {i*100}' )
        with open(f'image/image{i}.jpg.jpg', 'rb') as photo:
            await  message.answer_photo(photo)
            print(f'Отправлено изображение {i}')
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_products)
    print("Выберите продукт для покупки:")

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    print("Вы успешно приобрели продукт!")


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_choices)
    print('Выберите опцию:')


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Меня зовут Алина, какая техника тебя интересует?', reply_markup=menu)
    print('Привет! Меня зовут Алина, какая техника тебя интересует?')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print('Введите команду /start, чтобы начать общение.')


@dp.message_handler()
async def send_confirm_message(message):
    print("Вы успешно приобрели продукт!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)