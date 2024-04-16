import logging

from telegram import ReplyKeyboardMarkup, Update, KeyboardButton
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
MENU = "🍴 Menyu"
BASKET = "📥 Savat"
LOCATION = "KAFE LOKATSIYASI"
ABOUT_ORDER = "🚀 Buyurtma haqida"
ABOUT_COMMENT = "✍️ Fikr bildirish"
CONTACTS = "☎️ Kontaktlar"
SETTINGS = "⚙️ Sozlamalar"
ADDRESS = "📍 Manzilini yuborish"

PASTA = "Pasta"
ADDITIONAL = "Qo`shimchalar"
SALAT = "SALAT"
TAOMLAR = "🆕 Taomlar"

KISLODSKAYA = "🆕 Kislosladkaya"
TOMATO = "🆕 Tomato"
KARRI = "🆕 Karri (achchiq emasi)"
KARRI_SPICY = "🆕 Karri (achchig`i)"

MENU_KEYBOARD = [
    [BASKET],
    [PASTA, ADDITIONAL],
    [SALAT, TAOMLAR],
]

PASTA_MENU = [
    [KISLODSKAYA, TOMATO],
    [KARRI, KARRI_SPICY],
]

NUMBEROFRODER = [
    ["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["10"]
]

MAIN_KEYBOARD = [
    [
        MENU,
        BASKET,
    ],
    [LOCATION, ABOUT_ORDER],
    [ABOUT_COMMENT, CONTACTS],
    [SETTINGS],
]
MARKS = [["Zo'r 5"], ["Yaxshi 4"], ["O'rtacha 3"], ["Qoniqarsiz 2"], ["Yomon 1"]]


def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""

    update.message.reply_text(
        "Kerakli bo'limni tanlang",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        ),
    )


def menu(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """Quyidagilardan birini tanlang 👇🏻""",
        reply_markup=ReplyKeyboardMarkup(
            MENU_KEYBOARD,
            one_time_keyboard=False,
        )
    )


def basket(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """Savatingiz bo`sh""",
        # reply_markup=ReplyKeyboardMarkup(
        #     MENU_KEYBOARD,
        #     one_time_keyboard=False,
    )


def pasta(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """Mahsulotni tanlang 👇🏻""",
        reply_markup=ReplyKeyboardMarkup(
            PASTA_MENU,
            one_time_keyboard=False,
        )
    )


def kislodskaya(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """🆕 Kislosladkaya

Tovuq filesi, piyoz, maxsus sous, penne, pishloq va ziravorlar.
Sarimsoqli bagetlarni "Qo'shimchalar" bo'limidan qo'shishni unutmang!❣️

Vazn: 400 g

Narxi: 43 000 so'm""", )
    update.message.reply_text(
        """Sonini tanlang ⬇️""",
        reply_markup=ReplyKeyboardMarkup(
            NUMBEROFRODER,
            one_time_keyboard=False,
        )
    )


def tomato(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """🆕 Tomato

Tovuq filesi, tomat va qaymoqli souslar, penne, pishloq va ziravorlar.
Sarimsoqli bagetlarni "Qo'shimchalar" bo'limidan qo'shishni unutmang!❣️

Vazn: 400 g

Narxi: 43 000 so'm""", )
    update.message.reply_text(
        """Sonini tanlang ⬇️""",
        reply_markup=ReplyKeyboardMarkup(
            NUMBEROFRODER,
            one_time_keyboard=False,
        )
    )


def karri(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """🆕 Karri (achchiq emasi)

Tovuq filesi, Karri sousi, piyoz, ko'kat, penne, pishloq va ziravorlar.
Sarimsoqli bagetlarni "Qo'shimchalar" bo'limidan qo'shishni unutmang!❣️

Vazn: 420 g

Narxi: 43 000 so'm""", )
    update.message.reply_text(
        """Sonini tanlang ⬇️""",
        reply_markup=ReplyKeyboardMarkup(
            NUMBEROFRODER,
            one_time_keyboard=False,
        )
    )


def karri_spicy(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """🆕 Karri (achchig'i)

Tovuq filesi, Karri sousi, piyoz, ko'kat, penne, pishloq va ziravorlar.
Sarimsoqli bagetlarni "Qo'shimchalar" bo'limidan qo'shishni unutmang!❣️

Vazn: 420 g

Narxi: 43 000 so'm""", )
    update.message.reply_text(
        """Sonini tanlang ⬇️""",
        reply_markup=ReplyKeyboardMarkup(
            NUMBEROFRODER,
            one_time_keyboard=False,
        )
    )


def about_order(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """🇮🇹 Italiyani yetkazib berish!
🍝 Italiyancha pasta korobochkalarda!
⏰ С 11:00 до 01:00 
🛵 Hoziroq buyurtma bering!

*Ob havo va yo'l tirbandliklar sababli yetkazish narxi o'zgarishi mumkin""",
    )


def location(update: Update, context: CallbackContext) -> None:
    update.message.reply_location(latitude=41.312082, longitude=69.292853)
    update.message.reply_text(
        "🤩 Pastani kafeimizga kelib to'g'ridan-to'g'ri skovorodkadan ta'tib ko'ring - aynan shu uchun ham shaharning markazida joy ochdik, manzil Ц-1'da Ecopark va 64 maktab yonida\n"
        "📌 Ish tartibi: du - pa 11:00 - 23:00 / ju 14:00 - 23:00 / sha - yak 11:00 - 23:00\n\n"
        "Operator bilan aloqa 👉 @pastarobot",
        reply_markup=ReplyKeyboardMarkup(MAIN_KEYBOARD),
    )


def fikr_bildirish(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """✅ PASTA-PASTA ni tanlaganingiz uchun rahmat.
Agar Siz bizning xizmatlarimiz sifatini yaxhshilashga yordam bersangiz benihoyat hursand bo’lamiz.
Buning uchun 5 ballik tizim asosida bizni baholang""",
        reply_markup=ReplyKeyboardMarkup(
            MARKS,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        ),
    )
    return FIKR_BILDIRISH


def contact(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """Buyurtma va boshqa savollar bo'yicha javob olish uchun @pastarobot'ga murojaat qiling, barchasiga javob beramiz :)""",
    )


def marking(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """Bahoyingiz uchun rahmat""",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        ),
    )
    return ConversationHandler.END


(FIKR_BILDIRISH, REG, NAME) = range(3)


def settings(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """Iltimos, tilni tanlang
Пожалуйста, выберите язык ⬇️""",
        reply_markup=ReplyKeyboardMarkup(
            [[KeyboardButton(text="⚙️ Sozlamalar")]],
            resize_keyboard=True,
        ),
    ),


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("7184246379:AAEdpdKKdN1xMyDMTsrBcWf9qzXgYSnXnSU")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            MessageHandler(Filters.text(MENU), menu),
            MessageHandler(Filters.text(BASKET), basket),
            MessageHandler(Filters.text(PASTA), pasta),
            MessageHandler(Filters.text(KISLODSKAYA), kislodskaya),
            MessageHandler(Filters.text(TOMATO), tomato),
            MessageHandler(Filters.text(KARRI), karri),
            MessageHandler(Filters.text(KARRI_SPICY), karri_spicy),
            MessageHandler(Filters.text(ABOUT_ORDER), about_order),
            MessageHandler(Filters.regex(ABOUT_COMMENT), fikr_bildirish),
            MessageHandler(Filters.regex(LOCATION), location),
            MessageHandler(Filters.regex(CONTACTS), contact),
            MessageHandler(Filters.regex(SETTINGS), settings),
        ],
        states={
            FIKR_BILDIRISH: [
                MessageHandler(Filters.regex("^(Zo'r 5|Yaxshi 4|O'rtacha 3|Qoniqarsiz 2|Yomon 1)$"), marking)
            ],
        },
        fallbacks=[
            CommandHandler("start", start),
            # MessageHandler(Filters.text(MENU), menu),
            MessageHandler(Filters.text(BASKET), basket),
            # MessageHandler(Filters.text(ABOUT_ORDER), fikr_bildirish),
            # MessageHandler(Filters.regex("O'rtacha 3"), marking),
        ],
    )
    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
