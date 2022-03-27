import time

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from selenium import webdriver

import border_cross
import first_aid
import huhelp
import mental

#import googlemaps
#rom GoogleAPI import

TOKEN='5233323168:AAEL5OddXII7gFQdlP1RxAAx5Xsi5Y11FOM'
API_KEY='AIzaSyD6R4OmyAdkl-eoR8de9hyJBLILzRx54KA'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

ukrainian = KeyboardButton("Ukrainian🇺🇦")
english = KeyboardButton("English🇬🇧")

language_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(ukrainian).add(english)


back_region = KeyboardButton("Change region")
back_region_ua=KeyboardButton("Змінити регіон")
back_help=KeyboardButton("Back to services")

second_english_ukraine=KeyboardButton("I'm in Ukraine now🇺🇦")
second_english_eu=KeyboardButton("I'm refugee in EU🇪🇺")


first_english = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(second_english_ukraine).add(second_english_eu)

second_ua_ukraine=KeyboardButton("Зараз в Україні 🇺🇦")
second_ua_eu=KeyboardButton("Біженець в ЄС 🇪🇺")
first_ua=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(second_ua_ukraine).add(second_ua_eu)

#HELP IN UKRAINE IN ENGLISH
ukraine_english_map = KeyboardButton("Air raid map")
ukraine_english_medhelp = KeyboardButton("First Aid Help")
ukraine_english_border=KeyboardButton("Border crossings")
ukraine_english_mental=KeyboardButton("Mental Health support")

ukraine_english = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(ukraine_english_medhelp).add(ukraine_english_map).add(ukraine_english_border).add(back_region)


#HELP IN UKRAINE IN UKRAINIAN
ukraine_ua_map = KeyboardButton("Карта повітряних нальотів")
ukraine_ua_medhelp = KeyboardButton("Допомога першої допомоги")
ukraine_ua_border=KeyboardButton("Прикордонні переходи")
ukraine_ua_menthal=KeyboardButton("Підтримка психічного здоров'я")
ukraine_ua=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(ukraine_ua_map).add(ukraine_ua_medhelp).add(ukraine_ua_border).add(back_region_ua)


eu_english_hungary=KeyboardButton("Refugee in Hungary🇭🇺")
eu_english_czech=KeyboardButton("Refugee in Czech Republic🇨🇿")
eu_english_poland=KeyboardButton("Refugee in Poland🇵🇱")

eu_english_countries=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(eu_english_hungary).add(eu_english_czech).add(eu_english_poland)

#HELP IN EU IN UKRANIAN
eu_ua_hungary=KeyboardButton("Біженець в Угорщині🇭🇺")
eu_ua_czech=KeyboardButton("Біженець у Чехії🇨🇿")
eu_ua_poland=KeyboardButton("Біженець у Польщі🇵🇱")
eu_ua_countries=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(eu_ua_hungary).add(eu_ua_czech).add(eu_ua_poland)

hu_english_acc=KeyboardButton("Accommodation")
hu_english_sim=KeyboardButton("Phone and SIM")
hu_english_med=KeyboardButton("Medical help")
hu_english_food=KeyboardButton("Food and supply")
hu_english=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(hu_english_acc).add(hu_english_sim).add(hu_english_med).add(hu_english_food).add(back_region)


hu_ua_acc=KeyboardButton("Житло")
hu_ua_sim=KeyboardButton("Телефон, SIM-карта, WiFi")
hu_ua_med=KeyboardButton("Медична допомога")
hu_ua_food=KeyboardButton("Харчування")
hu_ua=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(hu_ua_acc).add(hu_ua_sim).add(hu_ua_med).add(hu_ua_food).add(back_region_ua)




q1n=InlineKeyboardButton(text='No',callback_data='q1n')
q1y=InlineKeyboardButton(text='Yes',callback_data='q1y')
q1=InlineKeyboardMarkup().add(q1n).add(q1y)

lq2n=InlineKeyboardButton(text='No',callback_data='lq2n')
lq2y=InlineKeyboardButton(text='Yes',callback_data='lq2y')
lq2=InlineKeyboardMarkup().add(lq2n).add(lq2y)

location=KeyboardButton(text="Send location",request_location=True)
locationmar=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(location).add(back_region)

rq2l=InlineKeyboardButton(text='First',callback_data='rq2l')
rq2r=InlineKeyboardButton(text='Second',callback_data='rq2r')
rq2=InlineKeyboardMarkup().add(rq2l).add(rq2r)

rrql=InlineKeyboardButton(text='First',callback_data='rrql')
rrqr=InlineKeyboardButton(text='Second',callback_data='rrqr')
rrq=InlineKeyboardMarkup().add(rrql).add(rrqr)



@dp.message_handler(commands=['start'])
async def choose_language(message: types.Message):
    await message.reply("Please choose your language\nБудь ласка, виберіть свою мову",reply_markup=language_buttons)



#FIRST MED HELP MENU
@dp.callback_query_handler(text=['tourni','recovery','penetrating','gunshot','eye','burn','amputation'])
async def aid_menu(callback:types.CallbackQuery):
    if(callback.data == 'tourni'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/1.png','rb'))
        await callback.message.answer(text=first_aid.tournitext, reply_markup=ukraine_english)
    elif(callback.data == 'recovery'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/2.png', 'rb'))
        await callback.message.answer(text=first_aid.recovertext, reply_markup=ukraine_english)
    elif (callback.data == 'penetrating'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/3.png', 'rb'))
        await callback.message.answer(text=first_aid.penetratingtext, reply_markup=ukraine_english)
    elif (callback.data == 'gunshot'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/4.png', 'rb'))
        await callback.message.answer(text=first_aid.gunshottext, reply_markup=ukraine_english)
    elif (callback.data == 'eye'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/5.png', 'rb'))
        await callback.message.answer(text=first_aid.eyetext, reply_markup=ukraine_english)
    elif (callback.data == 'burn'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/6.png', 'rb'))
        await callback.message.answer(text=first_aid.burntext, reply_markup=ukraine_english)
    elif (callback.data == 'amputation'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/7.png', 'rb'))
        await callback.message.answer(text=first_aid.amputationtext, reply_markup=ukraine_english)

@dp.callback_query_handler(text=['tourniu','recoveryu','penetratingu','gunshotu','eyeu','burnu','amputationu'])
async def aid_menu_ua(callback:types.CallbackQuery):
    if(callback.data == 'tourniu'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/1.png', 'rb'))
        await callback.message.answer(text=first_aid.tournitextu, reply_markup=ukraine_ua)
    elif(callback.data == 'recoveryu'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/2.png', 'rb'))
        await callback.message.answer(text=first_aid.recovertextu, reply_markup=ukraine_ua)
    elif (callback.data == 'penetratingu'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/3.png', 'rb'))
        await callback.message.answer(text=first_aid.penetratingtextu, reply_markup=ukraine_ua)
    elif (callback.data == 'gunshotu'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/4.png', 'rb'))
        await callback.message.answer(text=first_aid.gunshottextu, reply_markup=ukraine_ua)
    elif (callback.data == 'eyeu'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/5.png', 'rb'))
        await callback.message.answer(text=first_aid.eyetextu, reply_markup=ukraine_ua)
    elif (callback.data == 'burnu'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/6.png', 'rb'))
        await callback.message.answer(text=first_aid.burntextu, reply_markup=ukraine_ua)
    elif (callback.data == 'amputationu'):
        await callback.message.answer_photo(photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/7.png', 'rb'))
        await callback.message.answer(text=first_aid.amputationtextu, reply_markup=ukraine_ua)

#BORDER CROSSING MENU
@dp.callback_query_handler(text=['zahony','barabas','tiszebecs','beregsurany','lonya'])
async def border_menu(callback:types.CallbackQuery):
    if(callback.data == 'zahony'):
        await callback.message.reply(text=border_cross.zahonytext,reply_markup=ukraine_english)
    elif(callback.data == 'barabas'):
        await callback.message.reply(text=border_cross.barabastext,reply_markup=ukraine_english)
    elif (callback.data == 'tiszebecs'):
        await callback.message.reply(text=border_cross.tiszebectext,reply_markup=ukraine_english)
    elif (callback.data == 'beregsurany'):
        await callback.message.reply(text=border_cross.beregsuranytext,reply_markup=ukraine_english)
    elif (callback.data == 'lonya'):
        await callback.message.reply(text=border_cross.lonyatext,reply_markup=ukraine_english)

@dp.callback_query_handler(text=['q1n','q1y','lq2n','lq2y','rq2l','rq2r','rrqr','rrql'])
async def mental_menu(callback:types.CallbackQuery):
    if callback.data=='q1n':
        await callback.message.answer(text=mental.q1l,reply_markup=lq2)
    if callback.data=='lq2y':
        await callback.message.answer(text=mental.q1ly,reply_markup=ukraine_ua)
    if callback.data=='lq2n':
        await callback.message.answer(text=mental.q1ln, reply_markup=locationmar)
    if callback.data=='q1y':
        await callback.message.answer(text=mental.qr,reply_markup=rq2)
    if callback.data=='rq2l':
        await callback.message.answer(text=mental.rql,reply_markup=ukraine_ua)
    if callback.data=='rq2r':
        await callback.message.answer(text=mental.rqr,reply_markup=rrq)
    if callback.data=='rrqr':
        await callback.message.answer(text=mental.rrqr,reply_markup=ukraine_ua)
    if callback.data=='rrql':
        await callback.message.answer(text=mental.rrql,reply_markup=ukraine_ua)


@dp.message_handler()
async def menu(msg: types.Message):
    if msg.text == "English🇬🇧" :
        await msg.reply("Please choose your location",reply_markup=first_english)

    if msg.text == "I'm in Ukraine now🇺🇦":
        await msg.reply("How can I help you?",reply_markup=ukraine_english)

    if msg.text == "Back to services":
        await msg.reply("How can I help you?",reply_markup=ukraine_english)

    if msg.text == 'Change region':
        await msg.reply('Please choose your location', reply_markup=first_english)
    if msg.text=="Змінити регіон":
        await msg.reply("Будь ласка, виберіть своє місце розташування",reply_markup=first_ua)
    if msg.text=="I'm refugee in EU🇪🇺":
        await msg.reply("In which country are you now?",reply_markup=eu_english_countries)
    if msg.text=="Біженець в ЄС 🇪🇺":
        await msg.reply("Будь ласка, виберіть своє місце розташування",reply_markup=eu_ua_countries)


    if msg.text == "Air raid map":
        browser = webdriver.Chrome(executable_path=r'C://chromedriver.exe')
        print("CHECKDRIVER")
        browser.get("https://vadimklimenko.com/map/")
        print("CHECKBROWSER")
        time.sleep(1)
        browser.save_screenshot("screenshot.png")
        await bot.send_photo(chat_id=msg.chat.id, photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/screenshot.png', 'rb'))
        await msg.reply(text="Air raid alert map\nRed areas are under bombing now",reply_markup=ukraine_english)
    if msg.text=="First Aid Help":
        await msg.reply('What is your problem', reply_markup=first_aid.medhelp2)
    if msg.text=="Border crossings":
        await msg.reply('Select from list',reply_markup=border_cross.bordercross)
    if msg.text=="Mental Health support":
        await msg.reply(reply_markup=mental.q0)

    if msg.text=="Refugee in Hungary🇭🇺":
        await msg.reply(""" ‼️HOTLINE\n   Toll-free number to call from Hungary: 06 80 310 310\n
    Toll-free number to call from Ukraine: 0 800 504 546\n
    Email: menekultinfo@me.gov.hu""",reply_markup=hu_english)


    if msg.text=="Accommodation":
        await msg.reply(text=huhelp.en_acc,reply_markup=hu_english)
    if msg.text=="Phone and SIM":
        await msg.reply(text=huhelp.en_sim,reply_markup=hu_english)
    if msg.text=="Medical help":
        await msg.reply(text=huhelp.en_med,reply_markup=hu_english)
    if msg.text=="Food and supply":
        await msg.reply(text=huhelp.en_food,reply_markup=hu_english)

    if msg.text=="Refugee in Czech Republic🇨🇿":
        await msg.reply("Section is under construction...", reply_markup=first_english)
    if msg.text=="Refugee in Poland🇵🇱":
        await msg.reply("Section under construction...", reply_markup=first_english)


    if msg.text == "Біженець в Угорщині🇭🇺":
        await msg.reply(""" ‼️Угорський уряд встановив безкоштовну зелену лінію 24/7, де кожен може отримати важливу інформацію щодо поточної ситуації англійською, українською чи угорською мовами.\n
Безкоштовний номер для дзвінків з Угорщини: 06 80 310 310\n
Безкоштовний номер для дзвінків з України: 0 800 504 546\n
Email: menekultinfo@me.gov.hu""", reply_markup=hu_ua)
    if msg.text=="Житло":
        await msg.reply(text=huhelp.ua_acc,reply_markup=hu_ua)
    if msg.text=="Телефон, SIM-карта, WiFi":
        await msg.reply(text=huhelp.ua_sim,reply_markup=hu_ua)
    if msg.text=="Медична допомога":
        await msg.reply(text=huhelp.ua_med,reply_markup=hu_ua)
    if msg.text=="Харчування":
        await msg.reply(text=huhelp.ua_food,reply_markup=hu_ua)


    if msg.text == "Біженець у Чехії🇨🇿":
        await msg.reply("Розділ знаходиться на стадії будівництва", reply_markup=first_ua)
    if msg.text == "Біженець у Польщі🇵🇱":
        await msg.reply("Розділ знаходиться на стадії будівництва", reply_markup=first_ua)

    if msg.text=="Ukrainian🇺🇦":
        await msg.reply("Будь ласка, виберіть своє місце розташування",reply_markup=first_ua)


    if msg.text=="Зараз в Україні 🇺🇦":
        await msg.reply(text="Як я можу тобі допомогти",reply_markup=ukraine_ua)
    if msg.text=="Карта повітряних нальотів":
        browser = webdriver.Chrome(executable_path=r'C://chromedriver.exe')
        browser.get("https://vadimklimenko.com/map/")
        time.sleep(1)
        browser.save_screenshot("screenshot.png")
        await bot.send_photo(chat_id=msg.chat.id,photo=open('C:/Users/Нуржан/PycharmProjects/pythonProject1/screenshot.png', 'rb'))
        await msg.reply(text="Карта оповіщення про повітряні нальоти ", reply_markup=ukraine_ua)
    if msg.text=="Допомога першої допомоги":
        await msg.reply('What is your problem', reply_markup=first_aid.medhelpua)
    if msg.text=="Прикордонні переходи":
        await msg.reply('Виберіть зі списку', reply_markup=border_cross.bordercrossu)

if __name__ == '__main__':
    executor.start_polling(dp)
