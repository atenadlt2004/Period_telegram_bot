import telebot
from telebot import types
import datetime
bot = telebot.TeleBot('TOKEN')

# Variables
name = ""
gender = ""
partner_id = ""
partner_name = ""
start_date = ""
dur = 0
cycle = 0
is_period = False

# Client Class


class Client:
    def __init__(self, name, gender, partner_id, partner_name, start_date, dur, cycle):
        self.name = name
        self.gender = gender
        self.partner_id = partner_id
        self.partner_name = partner_name
        self.start_date = start_date
        self.dur = int(dur)
        self.cycle = int(cycle)


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_berim = types.KeyboardButton("حله بریم")
    markup.add(item_berim)
    bot.reply_to(
        message, "(:سلام!من بات تلگرام هستم,از صحبت با شما بسی خوشحالم ...اگه آماده ای بزن بریم", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "حله بریم")
def start1(message):
    bot.send_message(message.chat.id, "اسمت؟")
    bot.register_next_step_handler(message, start2)


def start2(message):
    global name
    name = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_zan = types.KeyboardButton("زن")
    item_mard = types.KeyboardButton("مرد")
    markup.add(item_zan, item_mard)
    bot.reply_to(
        message, "(:ممنون میشم جنسیت خودت رو انتخاب کنی ", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "زن")
def start3(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_yes = types.KeyboardButton("بله")
    item_no = types.KeyboardButton("خیر")
    markup.add(item_yes, item_no)
    bot.reply_to(
        message, "آیا پارتنر عاطفی داری؟", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "مرد")
def isman(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_are = types.KeyboardButton("آره")
    item_na = types.KeyboardButton("نه")
    markup.add(item_are, item_na)
    bot.reply_to(
        message, "آیا پارتنر عاطفی داری؟", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "آره")
def partnerofman(message):
    bot.send_message(
        message.chat.id, "(:یه پیام از پارتنرت واسم فوروارد کنم تا آیدیش رو داشته باشم. اینطوری میتونم بیشتر به تو و رابطت کمک کنم")
    bot.register_next_step_handler(message, start11)


def start11(message):
    global partner_id
    partner_id = message.forward_from.id
    bot.send_message(message.chat.id, "لطفا اسم پارتنرت رو بهم بگو")
    bot.register_next_step_handler(message, start12)


@bot.message_handler(func=lambda message: message.text == "نه")
def thesingleboy(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, "(:دوست عزیزم این بات برای آقایونی هست که پارتنر دارن...ببخش که نمیتونم در این زمینه راهنماییت کنم اما اگه دوست داری میتونی بازدن کلید پریود چیستت در منو اطلاعات زیادی راجع به پریود بدست بیاری")
    item_resendinformation = types.KeyboardButton("تغییر اطلاعات")
    item_whatisperid = types.KeyboardButton("پریود چیست")
    markup.add(item_resendinformation, whatisperiod)
    bot.reply_to(
        message, "چطور میتونم کمکت کنم؟", reply_markup=markup)


def start12(message):
    global partner_name
    partner_name = message.text
    bot.send_message(
        partner_id,  "(:سلام دوست عزیز من : من یک بات تلگرام هستم برای کمک به رابطه ی عاطفی شما و پارتنرت آیدیت رو ازش گرفتم ...ازآشنایی باهات خیلی خوشحالم")


@bot.message_handler(func=lambda message: message.text == "بله")
def start4(message):
    bot.send_message(
        message.chat.id, "(:یه پیام از پارتنرت واسم فوروارد کنم تا آیدیش رو داشته باشم. اینطوری میتونم بیشتر به تو و رابطت کمک کنم")
    bot.register_next_step_handler(message, start5)


@bot.message_handler(func=lambda message: message.text == "خیر")
def start10(message):
    bot.send_message(
        message.chat.id, " لطفا روز شروع آخرین دوره ی قاعدگیت رو بهم بگو چندم بود؟")
    bot.register_next_step_handler(message, start6)


def start5(message):
    global partner_id
    partner_id = message.forward_from.id
    bot.send_message(message.chat.id, "لطفا اسم پارتنرت رو بهم بگو")
    bot.register_next_step_handler(message, start9)


def start6(message):
    global start_date
    start_date = message.text
    bot.send_message(
        message.chat.id, "لطفا بهم بگو از شروع تا پایان دوره ی قاعدگیت معمولا چند روزه؟")
    bot.register_next_step_handler(message, start7)


def start7(message):
    global dur
    dur = int(message.text)
    bot.send_message(
        message.chat.id, "مدت زمان بین دو دوره ی قاعدگیت به طور معمول چند روزه؟")
    bot.register_next_step_handler(message, start8)


def start8(message):
    global cycle
    cycle = int(message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_changeinformation = types.KeyboardButton("تغییر اطلاعات")
    item_Iamperiod = types.KeyboardButton("(:من پریودهستم")
    item_electronicletter = types.KeyboardButton("ارسال نامه ی عاشقانه")
    item_aboutperiod = types.KeyboardButton("پریود چیست")
    markup.add(item_changeinformation, item_Iamperiod,
               item_electronicletter, item_aboutperiod)
    bot.reply_to(
        message, "چطور میتونم کمکت کنم؟", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "تغییر اطلاعات")
def changeinformation(message):
    bot.send_message(
        message, "شما در حال تغییر اطلاعات خود هستید لطفا به سوال پاسخ دهید")
    bot.register_next_step_handler(message, start1)


@bot.message_handler(func=lambda message: message.text == "ارسال نامه ی عاشقانه")
def electronicletter1(message):
    bot.send_message(
        message.chat.id, "متن نامه ی عاشقانه برای پارتنرتان را برای ما بفرستید")
    bot.register_next_step_handler(message, electronicletter2)


def electronicletter2(message):
    letter = "دلبر جانان گفت:" + "\n\n" + message.text
    bot.send_message(partner_id, letter)
    bot.send_message(message.chat.id, "پیام شما با موفقیت به پارتنرت ارسال شد")


@bot.message_handler(func=lambda message: message.text == "(:من پریودهستم")
def Iamperiod(message):
    global is_period
    is_period = True
    message = partner_name + " عزیز " + "\n" + \
        name + " جان " + " الآن تو دوره ی حساس پریودی قرار داره ممنونم ازت که حواست کلی بهش هست"

    bot.send_message(partner_id, message)


def start9(message):
    global partner_name
    partner_name = message.text
    bot.send_message(
        partner_id,  ":(:سلام دوست عزیز من : من یک بات تلگرام هستم برای کمک به رابطه ی عاطفی شما و پارتنرت آیدیت رو ازش گرفتم ...ازآشنایی باهات خیلی خوشحالم")
    bot.send_message(
        message.chat.id, " لطفا روز شروع آخرین دوره ی قاعدگیت رو بهم بگو چندم بود؟")
    bot.register_next_step_handler(message, start6)


@bot.message_handler(func=lambda message: message.text == "پریود چیست")
def whatisperiod(message):
    bot.send_message(
        message.chat.id, "اطلاعاتی در این باره فعلا در بات قرار داده نشده به زودی این بخش از بات به روز رسانی خواهد شد")


@bot.message_handler(commands=['help'])
def about(message):
    bot.send_message(
        message.chat.id, name + '\n' + str(dur) + str(partner_id))


bot.polling()
