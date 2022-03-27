from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


zahonytext="Zahony border crossing open 0-24\nVery highly loaded\nInfo is actual for"+dt_string
barabastext="Barabas border crossing open 0-24\nVery highly loaded\nInfo is actual for"+dt_string
tiszebectext="Tiszebec border crossing open 0-24\nHighly loaded\nInfo is actual for"+dt_string
beregsuranytext="Beregsurany border crossing open 0-24\nHighly loaded\nInfo is actual for"+dt_string
lonyatext="Lonya border crossing open 7-23\nHighly loaded\nInfo is actual for"+dt_string

zahonytextu="Прикордонний пункт «Захонь» відкритий 0-24\n Дуже сильно завантажений\n Інформація актуальна для "+dt_string
barabastextu="Прикордонний пункт «Барабаш» відкритий 0-24\n Дуже сильно завантажений\n Інформація актуальна для "+dt_string
tiszebectextu="Прикордонний пункт «Тисебец» відкритий 0-24\n Cильно завантажений\n Інформація актуальна для "+dt_string
beregsuranytextu="Прикордонний пункт «Берегшурань» відкритий 0-24\n Дуже сильно завантажений\n Інформація актуальна для "+dt_string
lonyatextu="Прикордонний пункт «Лонья» відкритий 7-23\n Cильно завантажений\n Інформація актуальна для "+dt_string

Zahony=InlineKeyboardButton(text="Zahony",callback_data="zahony")
Barabas=InlineKeyboardButton(text="Barabas",callback_data="barabas")
Tiszebec=InlineKeyboardButton(text="Tiszebec",callback_data="tiszebec")
Beregsurany=InlineKeyboardButton(text="Beregsurany",callback_data="Beregsurany")
Lonya=InlineKeyboardButton(text="Lonya",callback_data="lonya")

Zahonyu=InlineKeyboardButton(text="Захонь",callback_data="zahonyu")
Barabasu=InlineKeyboardButton(text="Барабаш",callback_data="barabasu")
Tiszebecu=InlineKeyboardButton(text="Тисебец",callback_data="tiszebecu")
Beregsuranyu=InlineKeyboardButton(text="Берегшурань",callback_data="Beregsuranyu")
Lonyau=InlineKeyboardButton(text="Лонья",callback_data="lonyau")

bordercross=InlineKeyboardMarkup(one_time_keyboard=True).add(Zahony).add(Barabas).add(Tiszebec).add(Beregsurany).add(Lonya)
bordercrossu=InlineKeyboardMarkup(one_time_keyboard=True).add(Zahonyu).add(Barabasu).add(Tiszebecu).add(Beregsuranyu).add(Lonyau)
