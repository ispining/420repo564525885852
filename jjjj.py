import logging
#from db import Botdb
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, Bot)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackQueryHandler)

bot_token = "1323517256:AAETTnRx71j4ryNh3_qM8jPjjV5PzHN8v2A"
lang_message = "\nPleace select your language:\n"
welcome_message = "Выберите страну проживания:"
rus_message = "\n😎Добро пожаловать в Картель😎\n"  +"\nТолько на территории России!\n" +"\nВсе группы и каналы данной платформы защищены на 100%\n" +"\nКартель- это не просто планомагаз, это нечно большее! В картеле есть все, в чем закон нас ограничивает!😉\n"
ua_message = "\n😎Добро пожаловать в Картель😎\n"  +"\nТолько на территории Украины!\n" +"\nВсе группы и каналы данной платформы защищены на 100%\n" +"\nКартель- это не просто планомагаз, это нечно большее! В картеле есть все, в чем закон нас ограничивает!😉\n"
weed_message = "\n😎Добро пожаловать в Картель😎\n"   +"\nВыберите область, в которой хотите осуществить заказ.\n" +"\n(нажимайте на кнопки, бот не видит текстовые сообщения)\n"
kaza_message = "\n😎Добро пожаловать в Картель😎\n"  +"\nТолько на территории Казахстана\n" +"\nВсе группы и каналы данной платформы защищены на 100%\n" +"\nКартель- это не просто планомагаз, это нечно большее! В картеле есть все, в чем закон нас ограничивает!😉\n"
belo_message = "\n😎Добро пожаловать в Картель😎\n"  +"\nТолько на территорир Белоруссии" +"\nВсе группы и каналы данной платформы защищены на 100%\n" +"\nКартель- это не просто планомагаз, это нечно большее! В картеле есть все, в чем закон нас ограничивает!😉\n"
ar_message = "\n😎Добро пожаловать в Картель😎\n"  +"\nТолько на территорир Армении! \n"+"\nВсе группы и каналы данной платформы защищены на 100%\n" +"\nКартель- это не просто планомагаз, это нечно большее! В картеле есть все, в чем закон нас ограничивает!😉\n"
uz_message = "\n😎Добро пожаловать в Картель😎\n"  +"\nТолько на территорир Узбекистана! \n"+"\nВсе группы и каналы данной платформы защищены на 100%\n" +"\nКартель- это не просто планомагаз, это нечно большее! В картеле есть все, в чем закон нас ограничивает!😉\n"
tur_message = "\n😎Добро пожаловать в Картель😎\n"  +"\nТолько на территорир Туркмении! \n"+"\nВсе группы и каналы данной платформы защищены на 100%\n" +"\nКартель- это не просто планомагаз, это нечно большее! В картеле есть все, в чем закон нас ограничивает!😉\n"
azer_message = "\n😎Добро пожаловать в Картель😎\n"  +"\nТолько на территорир Азербайджана! \n"+"\nВсе группы и каналы данной платформы защищены на 100%\n" +"\nККартель- это не просто планомагаз, это нечно большее! В картеле есть все, в чем закон нас ограничивает!😉\n"
tdj_message = "\n😎Добро пожаловать в Картель😎\n"  +"\nТолько на территорир Таджикистана! \n"+"\nВсе группы и каналы данной платформы защищены на 100%\n" +"\nКартель- это не просто планомагаз, это нечно большее! В картеле есть все, в чем закон нас ограничивает!😉\n"
mol_message = "\n😎Добро пожаловать в Картель😎\n"  +"\nТолько на территорир Молдавии! \n"+"\nВсе группы и каналы данной платформы защищены на 100%\n" +"\nКартель- это не просто планомагаз, это нечно большее! В картеле есть все, в чем закон нас ограничивает!😉\n"
kir_message = "\n😎Добро пожаловать в Картель😎\n"  +"\nТолько на территорир Кыргызстана! \n"+"\nВсе группы и каналы данной платформы защищены на 100%\n" +"\nКартель- это не просто планомагаз, это нечно большее! В картеле есть все, в чем закон нас ограничивает!😉\n"
us_message = "\n😎 Welcome to the Cartel system😎\n" +"Only on the territory of US! \n"+"\nAll groups and channels of this platform are 100% protected\n" +"\nA cartel is not just a store, it is more! The cartel has everything that the law limits us to! 😉\n"




welcome_picture = "logo_ua.JPG"
ua_picture = "ua.JPG"
rus_picture = "rus.JPG"
kaza_picture = "kaza.JPG"
belo_picture = "belo.JPG"
ar_picture = "ar.JPG"
uz_picture = "uz.JPG"
tur_picture = "tur.JPG"
azer_picture = "azer.JPG"
tdj_picture = "tdj.JPG"
mol_picture = "mol.JPG"
kir_picture = "kir.JPG"
us_picture = ""


taf = "Главная страница"
ah = "Назад"
back = "back"
sah = "🔰Травы, смеси, порошки🔰"
poroh = "💊Порошки и пилюли💊"
hev = "🧑Беседка🧑"
avt = "🔒Тех.Поддержка🔒"
reg = "👥Регистрация👥"
gun = "🔫Огнестрельное оружие🔫"


sa = "🍀Марихуана и другая кана-продукция🍀"
ukraineen = "🇺🇦 Ukraine 🇺🇦"
ukraine = "🇺🇦 Украина 🇺🇦"
russiaen = "🇷🇺 Russia 🇷🇺"
russia = "🇷🇺 Россия 🇷🇺"
kazaen = "🇰🇿 Kazahstan 🇰🇿"
kaza = "🇰🇿 Казахстан 🇰🇿"
uzbeken = "🇺🇿 Uzbekistan 🇺🇿"
uzbek = "🇺🇿 Узбекистан 🇺🇿"
tjen = "🇹🇯 Tajikistan 🇹🇯"
tj = "🇹🇯 Таджикистан 🇹🇯"
azen = "🇦🇿 Azerbaijan 🇦🇿"
az = "🇦🇿 Азербайджан 🇦🇿"
aren = "🇦🇲 Armenia 🇦🇲"
ar = "🇦🇲 Армения 🇦🇲"
byen = "🇧🇾 Belorus 🇧🇾"
by = "🇧🇾 Белоруссия 🇧🇾"
kgen = "🇰🇬 Kirgizstan 🇰🇬"
kg = "🇰🇬 Кыргызстан 🇰🇬"
mden = "🇲🇩 Moldavia 🇲🇩"
md = "🇲🇩 Молдавия 🇲🇩"
tmen = "🇹🇲 Turkmenistan 🇹🇲"
tm = "🇹🇲 Туркмения 🇹🇲"


card = "💳Кардинг💳"
usa = "🇺🇸 USA 🇺🇸"
card_en = "💳carding💳"
weed_en = "🍀Marijuana and other cana-products🍀"
guns_en = "🔫 Firearms🔫"
reg_en = "👥Registration👥"
support_en = "🔒Support🔒"
client_en = "🧑Client Group🧑"
poroh_en = "💊Ampetogens💊"
sah_en = "🔰Weed & extracts🔰"
taf_en = "Main menu"

English = "English"
Russian = "Russian"




lang_main =InlineKeyboardMarkup( [  #выбор языка
                  [InlineKeyboardButton(English, callback_data='main_en'),
                  InlineKeyboardButton(Russian, callback_data='main_main')]])


main_en =InlineKeyboardMarkup( [  #Выбор страны en

                  [InlineKeyboardButton(russia, callback_data='main_rusen'),
                   InlineKeyboardButton(ukraine, callback_data='main_uaen')],
                  [InlineKeyboardButton(kaza, callback_data='main_kazaen'),
                   InlineKeyboardButton(by, callback_data='main_beloen')],
                  [InlineKeyboardButton(ar, callback_data='main_aren'),
                   InlineKeyboardButton(tm, callback_data='main_turen')],
                  [InlineKeyboardButton(uzbek, callback_data='main_uzen'),
                   InlineKeyboardButton(tj, callback_data='main_tdjen')],
                  [InlineKeyboardButton(az, callback_data='main_azeren'),
                   InlineKeyboardButton(md, callback_data='main_molen')],
                  [InlineKeyboardButton(kg, callback_data='main_kiren')]

])

main_main =InlineKeyboardMarkup( [  #Выбор страны

                  [InlineKeyboardButton(russia, callback_data='main_rus'),
                   InlineKeyboardButton(ukraine, callback_data='main_ua')],
                  [InlineKeyboardButton(kaza, callback_data='main_kaza'),
                   InlineKeyboardButton(by, callback_data='main_belo')],
                  [InlineKeyboardButton(ar, callback_data='main_ar'),
                   InlineKeyboardButton(tm, callback_data='main_tur')],
                  [InlineKeyboardButton(uzbek, callback_data='main_uz'),
                   InlineKeyboardButton(tj, callback_data='main_tdj')],
                  [InlineKeyboardButton(az, callback_data='main_azer'),
                   InlineKeyboardButton(md, callback_data='main_mol')],
                  [InlineKeyboardButton(kg, callback_data='main_kir')]

])



main_keyboard =InlineKeyboardMarkup( [ #Главна
                  [InlineKeyboardButton(" Принцип работы Картеля", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah, callback_data='sub_main0')],
                  [InlineKeyboardButton(gun, url="https://t.me/joinchat/AAAAAFTd6SlTD7E7vITrtQ")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBWgAPouO_hqLfz6fA')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFPUp3JujB3XLxjT5Q')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBgGuH9DsOp1b_DNig")],
                  [InlineKeyboardButton(card, url="https://t.me/joinchat/AAAAAFkPF_wc_78oSaqluQ")],
                  #[InlineKeyboardButton(reg, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(avt, url='https://t.me/apteka_helpbot')]
] )

main_keyboarden =InlineKeyboardMarkup( [ #Главна en
                  [InlineKeyboardButton(" How it work? ", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah_en, callback_data='sub_main0en')],
                  [InlineKeyboardButton(guns_en, url="https://t.me/joinchat/AAAAAFTd6SlTD7E7vITrtQ")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBWgAPouO_hqLfz6fA')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFPUp3JujB3XLxjT5Q')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBgGuH9DsOp1b_DNig")],
                  [InlineKeyboardButton(card_en, url="https://t.me/joinchat/AAAAAFkPF_wc_78oSaqluQ")],
                  #[InlineKeyboardButton(reg_en, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(support_en, url='https://t.me/apteka_helpbot')]
] )


main_keyboard_kaza =InlineKeyboardMarkup( [ #Главна kazahstan
                  [InlineKeyboardButton(" Принцип работы Картеля", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah, callback_data='sub_main0_kaza')],
                  [InlineKeyboardButton(gun, url="https://t.me/joinchat/AAAAAE_PmFWftxznHXwS_A")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBcUhLGEOD7Tx2HLJg')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFY9adoW95XyGPhJ7Q')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBsAh9QWxqfOd1NMhQ")],
                  [InlineKeyboardButton(card, url="https://t.me/joinchat/AAAAAFioFbrJpBRwP1oucw")],
                  #[InlineKeyboardButton(reg, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(avt, url='https://t.me/apteka_helpbot')]
] )

main_keyboard_kazaen =InlineKeyboardMarkup( [ #Главна kazahstan en
                  [InlineKeyboardButton(" How it work? ", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah_en, callback_data='sub_main0_kazaen')],
                  [InlineKeyboardButton(guns_en, url="https://t.me/joinchat/AAAAAE_PmFWftxznHXwS_A")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBcUhLGEOD7Tx2HLJg')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFY9adoW95XyGPhJ7Q')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBsAh9QWxqfOd1NMhQ")],
                  [InlineKeyboardButton(card_en, url="https://t.me/joinchat/AAAAAFioFbrJpBRwP1oucw")],
                  #[InlineKeyboardButton(reg_en, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(support_en, url='https://t.me/apteka_helpbot')]
] )


main_keyboard_aren =InlineKeyboardMarkup( [ #Главна armenia en
                  [InlineKeyboardButton(" How it work? ", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah_en, callback_data='sub_main0_aren')],
                  [InlineKeyboardButton(guns_en, url="https://t.me/joinchat/AAAAAExuLaQ5C9wmuxxa-A")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBJYujz55IYQpHhMhQ')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFIu-2gOsuWl7mkPKA')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBpuWMkSLi9Ycnuctg")],
                  [InlineKeyboardButton(card_en, url="https://t.me/joinchat/AAAAAFOdFXAoSp83MNb3YA")],
                  #[InlineKeyboardButton(reg_en, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(support_en, url='https://t.me/apteka_helpbot')]
] )

main_keyboard_ar =InlineKeyboardMarkup( [ #Главна armenia
                  [InlineKeyboardButton(" Принцип работы Картеля", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah, callback_data='sub_main0_ar')],
                  [InlineKeyboardButton(gun, url="https://t.me/joinchat/AAAAAExuLaQ5C9wmuxxa-A")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBJYujz55IYQpHhMhQ')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFIu-2gOsuWl7mkPKA')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBpuWMkSLi9Ycnuctg")],
                  [InlineKeyboardButton(card, url="https://t.me/joinchat/AAAAAFOdFXAoSp83MNb3YA")],
                  #[InlineKeyboardButton(reg, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(avt, url='https://t.me/apteka_helpbot')]
] )


main_keyboard_belo =InlineKeyboardMarkup( [ #Главна belorus
                  [InlineKeyboardButton(" Принцип работы Картеля", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah, callback_data='sub_main0_belo')],
                  [InlineKeyboardButton(gun, url="https://t.me/joinchat/AAAAAEiQSqUh9_SQuh-fhA")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyB0dkKFS9Xv609AISA')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFSFTqyu-8zJ4EnUPQ')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBn57uSjT5w4WSinqQ")],
                  [InlineKeyboardButton(card, url="https://t.me/joinchat/AAAAAFMSaL42Zu60Ys9ElQ")],
                  #[InlineKeyboardButton(reg, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(avt, url='https://t.me/apteka_helpbot')]])

main_keyboard_beloen =InlineKeyboardMarkup( [ #Главна belorus en
                  [InlineKeyboardButton(" How it work? ", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah_en, callback_data='sub_main0_beloen')],
                  [InlineKeyboardButton(guns_en, url="https://t.me/joinchat/AAAAAEiQSqUh9_SQuh-fhA")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyB0dkKFS9Xv609AISA')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFSFTqyu-8zJ4EnUPQ')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBn57uSjT5w4WSinqQ")],
                  [InlineKeyboardButton(card_en, url="https://t.me/joinchat/AAAAAFMSaL42Zu60Ys9ElQ")],
                  #[InlineKeyboardButton(reg_en, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(support_en, url='https://t.me/apteka_helpbot')]])

main_keyboard_uz =InlineKeyboardMarkup( [ #Главна uzbekistan
                  [InlineKeyboardButton(" Принцип работы Картеля", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah, callback_data='sub_main0_uz')],
                  [InlineKeyboardButton(gun, url="https://t.me/joinchat/AAAAAFZuEHnAFOHpXOMLYA")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBlThPXLZSxjauaQuA')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFVV8wAeV-c_U5W3hA')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBpyQ_c_Z_GWuIvVyQ")],
                  [InlineKeyboardButton(card, url="https://t.me/joinchat/AAAAAFT_0jPiWL1PRvA_SA")],
                 # [InlineKeyboardButton(reg, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(avt, url='https://t.me/apteka_helpbot')]])

main_keyboard_uzen =InlineKeyboardMarkup( [ #Главна uzbekistan en
                  [InlineKeyboardButton(" How it work? ", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah_en, callback_data='sub_main0_uzen')],
                  [InlineKeyboardButton(guns_en, url="https://t.me/joinchat/AAAAAFZuEHnAFOHpXOMLYA")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBlThPXLZSxjauaQuA')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFVV8wAeV-c_U5W3hA')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBpyQ_c_Z_GWuIvVyQ")],
                  [InlineKeyboardButton(card_en, url="https://t.me/joinchat/AAAAAFT_0jPiWL1PRvA_SA")],
                 # [InlineKeyboardButton(reg_en, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(support_en, url='https://t.me/apteka_helpbot')]])



main_keyboard_tur =InlineKeyboardMarkup( [ #Главна turkmenistan
                  [InlineKeyboardButton(" Принцип работы Картеля", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah, callback_data='sub_main0_tur')],
                  [InlineKeyboardButton(gun, url="https://t.me/joinchat/AAAAAEWEqFMBtY5apcSW0w")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBmQ_0g_Pp7StJxrWw')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFSxyAvmkkh4hpqSNQ')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBbVcgw7rgPRHg0Y-w")],
                  [InlineKeyboardButton(card, url="https://t.me/joinchat/AAAAAEzvZsN5D-PGwvG5rg")],
                  #[InlineKeyboardButton(reg, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(avt, url='https://t.me/apteka_helpbot')]])


main_keyboard_turen =InlineKeyboardMarkup( [ #Главна turkmenistan en
                  [InlineKeyboardButton(" How it work? ", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah_en, callback_data='sub_main0_turen')],
                  [InlineKeyboardButton(guns_en, url="https://t.me/joinchat/AAAAAEWEqFMBtY5apcSW0w")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBmQ_0g_Pp7StJxrWw')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFSxyAvmkkh4hpqSNQ')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBbVcgw7rgPRHg0Y-w")],
                  [InlineKeyboardButton(card_en, url="https://t.me/joinchat/AAAAAEzvZsN5D-PGwvG5rg")],
                  #[InlineKeyboardButton(reg_en, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(support_en, url='https://t.me/apteka_helpbot')]])


main_keyboard_azer =InlineKeyboardMarkup( [ #Главна azerbaijan
                  [InlineKeyboardButton(" Принцип работы Картеля", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah, callback_data='sub_main0_azer')],
                  [InlineKeyboardButton(gun, url="https://t.me/joinchat/AAAAAEtWS7AarJiLsxEQVQ")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBkVPfGR-Vecj9wl6w')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFDsgy_i4yKGRKE2jg')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBtLzB9JTIs9uT9BBw")],
                  [InlineKeyboardButton(card, url="https://t.me/joinchat/AAAAAFlZh8qFvs2UBgcPBw")],
                  #[InlineKeyboardButton(reg, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(avt, url='https://t.me/apteka_helpbot')]])

main_keyboard_azeren =InlineKeyboardMarkup( [ #Главна azerbaijan en
                  [InlineKeyboardButton(" How it  work? ", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah_en, callback_data='sub_main0_azeren')],
                  [InlineKeyboardButton(guns_en, url="https://t.me/joinchat/AAAAAEtWS7AarJiLsxEQVQ")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBkVPfGR-Vecj9wl6w')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFDsgy_i4yKGRKE2jg')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBtLzB9JTIs9uT9BBw")],
                  [InlineKeyboardButton(card_en, url="https://t.me/joinchat/AAAAAFlZh8qFvs2UBgcPBw")],
                  #[InlineKeyboardButton(reg_en, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(support_en, url='https://t.me/apteka_helpbot')]])



main_keyboard_tdj =InlineKeyboardMarkup( [ #Главна tadjikistan
                  [InlineKeyboardButton(" Принцип работы Картеля", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah, callback_data='sub_main0_tdj')],
                  [InlineKeyboardButton(gun, url="https://t.me/joinchat/AAAAAFQFj1kuLAVrBrr1KQ")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBq0FDOgNzTx7q7Fjw')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAEUvIcw3yR-Q9uy8qA')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBmoN8wt45Ar9SnlNA")],
                  [InlineKeyboardButton(card, url="https://t.me/joinchat/AAAAAEhBtwCogpcFCpaOlQ")],
                  #[InlineKeyboardButton(reg, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(avt, url='https://t.me/apteka_helpbot')]])


main_keyboard_tdjen =InlineKeyboardMarkup( [ #Главна tadjikistan en
                  [InlineKeyboardButton(" How it work? ", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah_en, callback_data='sub_main0_tdjen')],
                  [InlineKeyboardButton(guns_en, url="https://t.me/joinchat/AAAAAFQFj1kuLAVrBrr1KQ")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBq0FDOgNzTx7q7Fjw')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAEUvIcw3yR-Q9uy8qA')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBmoN8wt45Ar9SnlNA")],
                  [InlineKeyboardButton(card_en, url="https://t.me/joinchat/AAAAAEhBtwCogpcFCpaOlQ")],
                  #[InlineKeyboardButton(reg_en, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(support_en, url='https://t.me/apteka_helpbot')]])


main_keyboard_mol =InlineKeyboardMarkup( [ #Главна moldavia
                  [InlineKeyboardButton(" Принцип работы Картеля", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah, callback_data='sub_main0_mol')],
                  [InlineKeyboardButton(gun, url="https://t.me/joinchat/AAAAAEjwVnToCnAWepDKiw")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBy3t0tncpMirYboyQ')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAEj-EnL_J8G_vn1pwQ')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBz5tufO2hNn_ulUtw")],
                  [InlineKeyboardButton(card, url="https://t.me/joinchat/AAAAAEPtnnOX-IATRB5uCA")],
                  #[InlineKeyboardButton(reg, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(avt, url='https://t.me/apteka_helpbot')]])

main_keyboard_molen =InlineKeyboardMarkup( [ #Главна moldavia en
                  [InlineKeyboardButton(" How it work? ", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah_en, callback_data='sub_main0_molen')],
                  [InlineKeyboardButton(guns_en, url="https://t.me/joinchat/AAAAAEjwVnToCnAWepDKiw")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBy3t0tncpMirYboyQ')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAEj-EnL_J8G_vn1pwQ')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBz5tufO2hNn_ulUtw")],
                  [InlineKeyboardButton(card_en, url="https://t.me/joinchat/AAAAAEPtnnOX-IATRB5uCA")],
                  #[InlineKeyboardButton(reg_en, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(support_en, url='https://t.me/apteka_helpbot')]])


main_keyboard_kir =InlineKeyboardMarkup( [ #Главна kirgizstan
                  [InlineKeyboardButton(" Принцип работы Картеля", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah, callback_data='sub_main0_kir')],
                  [InlineKeyboardButton(gun, url="https://t.me/joinchat/AAAAAEvdY0jTr2M2eT0-Jg")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyB2eI_E_Agw6XSDoZA')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFRrwhfS9goiFOuXZw')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBod7baFoS_L5VYOQg")],
                  [InlineKeyboardButton(card, url="https://t.me/joinchat/AAAAAEiXvLmqPLokWnpwWg")],
                  #[InlineKeyboardButton(reg, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(avt, url='https://t.me/apteka_helpbot')]])


main_keyboard_kiren =InlineKeyboardMarkup( [ #Главна kirgizstan en
                  [InlineKeyboardButton(" How it work? ", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah_en, callback_data='sub_main0_kiren')],
                  [InlineKeyboardButton(guns_en, url="https://t.me/joinchat/AAAAAEvdY0jTr2M2eT0-Jg")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyB2eI_E_Agw6XSDoZA')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAFRrwhfS9goiFOuXZw')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBod7baFoS_L5VYOQg")],
                  [InlineKeyboardButton(card_en, url="https://t.me/joinchat/AAAAAEiXvLmqPLokWnpwWg")],
                  #[InlineKeyboardButton(reg_en, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(support_en, url='https://t.me/apteka_helpbot')]])




main_keyboard1 =InlineKeyboardMarkup( [ #Главна rus
                  [InlineKeyboardButton(" Принцип работы Картеля", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah, callback_data='sub_main0_rus')],
                  [InlineKeyboardButton(gun, url="https://t.me/joinchat/AAAAAFKAvU4qj7P1ldG7kQ")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBZ3QWqhWWqmMJjpnA')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAEuzQE5Bjd0iVaLtgw')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBzxPih6HP4AN8y6Zw")],
                  [InlineKeyboardButton(card, url="https://t.me/joinchat/AAAAAFS2iuTL0r9k4qgGlQ")],
                  #[InlineKeyboardButton(reg, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(avt, url='https://t.me/apteka_helpbot')]
] )

main_keyboard1en =InlineKeyboardMarkup( [ #Главна rusen
                  [InlineKeyboardButton(" How it work?", url='https://t.me/joinchat/AAAAAFPQO8JOtidCwBcKlg')],
                  [InlineKeyboardButton(sah_en, callback_data='sub_main0_rusen')],
                  [InlineKeyboardButton(guns_en, url="https://t.me/joinchat/AAAAAFKAvU4qj7P1ldG7kQ")],
                  [InlineKeyboardButton("👩‍🌾Гровер - группа👩‍🌾", url='https://t.me/joinchat/TY0lyBZ3QWqhWWqmMJjpnA')],
                  [InlineKeyboardButton("💎Халява💎", url='https://t.me/joinchat/AAAAAEuzQE5Bjd0iVaLtgw')],
                  [InlineKeyboardButton("🗣Беседка🗣", url="https://t.me/joinchat/TY0lyBzxPih6HP4AN8y6Zw")],
                  [InlineKeyboardButton(card_en, url="https://t.me/joinchat/AAAAAFS2iuTL0r9k4qgGlQ")],
                  #[InlineKeyboardButton(reg_en, url="https://t.me/ga_dmin")],
                  [InlineKeyboardButton(support_en, url='https://t.me/apteka_helpbot')]
] )


sub_main0 =InlineKeyboardMarkup( [ #shops ua
                  [InlineKeyboardButton(sa, callback_data='sub_main1')],
                  [InlineKeyboardButton(poroh, url="https://t.me/joinchat/AAAAAE7Fm-8llfTuX06UOw")],
                  [InlineKeyboardButton(taf, callback_data='main_ua')]] )

sub_main0en =InlineKeyboardMarkup( [ #shops ua en
                  [InlineKeyboardButton(weed_en, callback_data='sub_main1en')],
                  [InlineKeyboardButton(poroh_en, url="https://t.me/joinchat/AAAAAE7Fm-8llfTuX06UOw")],
                  [InlineKeyboardButton(back, callback_data='main_uaen')]] )


sub_main0_kaza =InlineKeyboardMarkup( [ #shops
                  [InlineKeyboardButton(sa, callback_data='sub_main4')],
                  [InlineKeyboardButton(poroh, url="https://t.me/joinchat/AAAAAFVELZnVK6-aoKBb2A")],
                  [InlineKeyboardButton(taf, callback_data='main_kaza')]] )

sub_main0_kazaen =InlineKeyboardMarkup( [ #shops kaza en
                  [InlineKeyboardButton(weed_en, callback_data='sub_main4en')],
                  [InlineKeyboardButton(poroh_en, url="https://t.me/joinchat/AAAAAFVELZnVK6-aoKBb2A")],
                  [InlineKeyboardButton(back, callback_data='main_kazaen')]] )

sub_main0_belo =InlineKeyboardMarkup( [ #shops
                  [InlineKeyboardButton(sa, callback_data='sub_main5')],
                  [InlineKeyboardButton(poroh, url="https://t.me/joinchat/AAAAAFA5Kbgd84-tUyW1_A")],
                  [InlineKeyboardButton(taf, callback_data='main_belo')]] )

sub_main0_beloen =InlineKeyboardMarkup( [ #shops belo en
                  [InlineKeyboardButton(weed_en, callback_data='sub_main5en')],
                  [InlineKeyboardButton(poroh_en, url="https://t.me/joinchat/AAAAAFA5Kbgd84-tUyW1_A")],
                  [InlineKeyboardButton(back, callback_data='main_beloen')]] )


sub_main0_ar =InlineKeyboardMarkup( [ #shops
                  [InlineKeyboardButton(sa, callback_data='sub_main6')],
                  [InlineKeyboardButton(poroh, url="https://t.me/joinchat/AAAAAFYpRQsYcQSTatUqGQ")],
                  [InlineKeyboardButton(taf, callback_data='main_belo')]] )

sub_main0_aren =InlineKeyboardMarkup( [ #shops ar en
                  [InlineKeyboardButton(weed_en, callback_data='sub_main6en')],
                  [InlineKeyboardButton(poroh_en, url="https://t.me/joinchat/AAAAAFYpRQsYcQSTatUqGQ")],
                  [InlineKeyboardButton(back, callback_data='main_beloen')]] )



sub_main0_rus =InlineKeyboardMarkup( [ #shops
                  [InlineKeyboardButton(sa, callback_data='sub_main3')],
                  [InlineKeyboardButton(poroh, url="https://t.me/joinchat/AAAAAFGE9nEpTUWtdP96AA")],
                  [InlineKeyboardButton(taf, callback_data='main_rus')]] )

sub_main0_rusen =InlineKeyboardMarkup( [ #shops rus en
                  [InlineKeyboardButton(weed_en, callback_data='sub_main3en')],
                  [InlineKeyboardButton(poroh_en, url="https://t.me/joinchat/AAAAAFGE9nEpTUWtdP96AA")],
                  [InlineKeyboardButton(back, callback_data='main_rusen')]] )



sub_main0_uz =InlineKeyboardMarkup( [ #shops uz
                  [InlineKeyboardButton(sa, callback_data='sub_main7')],
                  [InlineKeyboardButton(poroh, url="https://t.me/joinchat/AAAAAEdo5qEnSGU4SZdb8A")],
                  [InlineKeyboardButton(taf, callback_data='main_uz')]] )


sub_main0_uzen =InlineKeyboardMarkup( [ #shops uz en
                  [InlineKeyboardButton(weed_en, callback_data='sub_main7en')],
                  [InlineKeyboardButton(poroh_en, url="https://t.me/joinchat/AAAAAEdo5qEnSGU4SZdb8A")],
                  [InlineKeyboardButton(back, callback_data='main_uzen')]] )




sub_main0_tur =InlineKeyboardMarkup( [ #shops turkmenia
                  [InlineKeyboardButton(sa, callback_data='sub_main8')],
                  [InlineKeyboardButton(poroh, url="https://t.me/joinchat/AAAAAEmkMgUGm0MfC0sfeQ")],
                  [InlineKeyboardButton(taf, callback_data='main_tur')]] )

sub_main0_turen =InlineKeyboardMarkup( [ #shops turkmenia en
                  [InlineKeyboardButton(weed_en, callback_data='sub_main8en')],
                  [InlineKeyboardButton(poroh_en, url="https://t.me/joinchat/AAAAAEmkMgUGm0MfC0sfeQ")],
                  [InlineKeyboardButton(back, callback_data='main_turen')]] )


sub_main0_azer =InlineKeyboardMarkup( [ #shops azerbaijan
                  [InlineKeyboardButton(sa, callback_data='sub_main9')],
                  [InlineKeyboardButton(poroh, url="https://t.me/joinchat/AAAAAEaPNUCy7Or1orzkgA")],
                  [InlineKeyboardButton(taf, callback_data='main_azer')]] )

sub_main0_azeren =InlineKeyboardMarkup( [ #shops azerbaijan en
                  [InlineKeyboardButton(weed_en, callback_data='sub_main9en')],
                  [InlineKeyboardButton(poroh_en, url="https://t.me/joinchat/AAAAAEaPNUCy7Or1orzkgA")],
                  [InlineKeyboardButton(back, callback_data='main_azeren')]] )



sub_main0_tdj =InlineKeyboardMarkup( [ #shops tdj
                  [InlineKeyboardButton(sa, callback_data='sub_main_10')],
                  [InlineKeyboardButton(poroh, url="https://t.me/joinchat/AAAAAEz0M85rUo5xUZfDHA")],
                  [InlineKeyboardButton(taf, callback_data='main_tdj')]] )


sub_main0_tdjen =InlineKeyboardMarkup( [ #shops tdj_en
                  [InlineKeyboardButton(weed_en, callback_data='sub_main_10en')],
                  [InlineKeyboardButton(poroh_en, url="https://t.me/joinchat/AAAAAEz0M85rUo5xUZfDHA")],
                  [InlineKeyboardButton(back, callback_data='main_tdjen')]] )



sub_main0_mol =InlineKeyboardMarkup( [ #shops mol
                  [InlineKeyboardButton(sa, callback_data='sub_main_11')],
                  [InlineKeyboardButton(poroh, url="https://t.me/joinchat/AAAAAE73nv-lhTwaKDmg-Q")],
                  [InlineKeyboardButton(taf, callback_data='main_mol')]] )

sub_main0_molen =InlineKeyboardMarkup( [ #shops mol en
                  [InlineKeyboardButton(weed_en, callback_data='sub_main_11en')],
                  [InlineKeyboardButton(poroh_en, url="https://t.me/joinchat/AAAAAE73nv-lhTwaKDmg-Q")],
                  [InlineKeyboardButton(back, callback_data='main_molen')]] )



sub_main0_kir =InlineKeyboardMarkup( [ #shops
                  [InlineKeyboardButton(sa, callback_data='sub_main_12')],
                  [InlineKeyboardButton(poroh, url="https://t.me/joinchat/AAAAAEibDV87ZotG6bzjGg")],
                  [InlineKeyboardButton(taf, callback_data='main_kir')]] )

sub_main0_kiren =InlineKeyboardMarkup( [ #shops
                  [InlineKeyboardButton(weed_en, callback_data='sub_main_12en')],
                  [InlineKeyboardButton(poroh_en, url="https://t.me/joinchat/AAAAAEibDV87ZotG6bzjGg")],
                  [InlineKeyboardButton(back, callback_data='main_kiren')]] )



sub_main1 =InlineKeyboardMarkup( [ #kivun_ua
                  [InlineKeyboardButton("Диллеры всей страны", url='https://t.me/joinchat/AAAAAEWCkm6E5rwT-eMlZg')],
                  [InlineKeyboardButton("Донецкая Область", url='https://t.me/joinchat/AAAAAEZ84S7sASQiPXEhFw')],
                  [InlineKeyboardButton("Днепропетровская Область", url='https://t.me/joinchat/AAAAAEYSexvYJH_fRYAxhA')],
                  [InlineKeyboardButton("Киевская Область", url='https://t.me/joinchat/AAAAAEmncjMibe-xmbYe9g')],
                  [InlineKeyboardButton("Харьковская область", url='https://t.me/joinchat/AAAAAFBiR81N-G5PrdfaGQ')],
                  [InlineKeyboardButton("Одесская Область", url='https://t.me/joinchat/AAAAAEr_wruH7beqsPUaSQ')],
                  [InlineKeyboardButton("Луганская Область", url='https://t.me/joinchat/AAAAAEZYZfqyr-XX6VlgFA')],
                  [InlineKeyboardButton("Запорожская Область", url='https://t.me/joinchat/AAAAAFk6eas2w3w5GGQs7g')],
                  [InlineKeyboardButton("Винницкая Область", url='https://t.me/joinchat/AAAAAFiZX2OqDw6d1xSWdg')],
                  [InlineKeyboardButton("Полтавская Область", url='https://t.me/joinchat/AAAAAFMitTOOVnMN4mvbzg')],
                  [InlineKeyboardButton("Хмельницкая Область", url='https://t.me/joinchat/AAAAAEoEXQzLBw5g-EJHwQ')],
                  [InlineKeyboardButton("Закарпатская Область", url='https://t.me/joinchat/AAAAAEPTx2T6KfFHodAbMg')],
                  [InlineKeyboardButton("Житомирская Область", url='https://t.me/joinchat/AAAAAELxDhmG8v16yX21VA')],
                  [InlineKeyboardButton("Черкасская Область", url='https://t.me/joinchat/AAAAAFPMozHITJRIdt_QlQ')],
                  [InlineKeyboardButton("Ивано-Франковск", url='https://t.me/joinchat/AAAAAEx1VIR1vHhd-7lbMA')],
                  [InlineKeyboardButton("Ровненская Область", url='https://t.me/joinchat/AAAAAEx3VTq1fMFXee5cqA')],
                  [InlineKeyboardButton("Николаевская Облать", url='https://t.me/joinchat/AAAAAFOkfl78AUXauKJWIA')],
                  [InlineKeyboardButton("Сумская Область", url='https://t.me/joinchat/AAAAAEqj6zMZVYhapnATkw')],
                  [InlineKeyboardButton("Тернопольская Область", url='https://t.me/joinchat/AAAAAEwfgMTYQjj7nlZdlg')],
                  [InlineKeyboardButton("Херсонская Область", url='https://t.me/joinchat/AAAAAFdT-eK3dKzey7sP-w')],
                  [InlineKeyboardButton("Волынская Область", url='https://t.me/joinchat/AAAAAFa1RAVJxsszMO62VQ')],
                  [InlineKeyboardButton("Черниговская Область", url='https://t.me/joinchat/AAAAAEpFViPguk35su9d4g')],
                  [InlineKeyboardButton("Кировоградская Область", url='https://t.me/joinchat/AAAAAEqj6zMZVYhapnATkw')],
                  [InlineKeyboardButton("Черновицкая Область", url='https://t.me/joinchat/AAAAAExqOG_vOgDddTZpWg')],
                  [InlineKeyboardButton(taf, callback_data='main_ua')]] )

sub_main1en =InlineKeyboardMarkup( [ #kivun_ua en
                  [InlineKeyboardButton("Dealers all over the country", url='https://t.me/joinchat/AAAAAEWCkm6E5rwT-eMlZg')],
                  [InlineKeyboardButton("Donetsk region", url='https://t.me/joinchat/AAAAAEZ84S7sASQiPXEhFw')],
                  [InlineKeyboardButton("Dnipropetrovsk region", url='https://t.me/joinchat/AAAAAEYSexvYJH_fRYAxhA')],
                  [InlineKeyboardButton("Kiev region", url='https://t.me/joinchat/AAAAAEmncjMibe-xmbYe9g')],
                  [InlineKeyboardButton("Kharkov region", url='https://t.me/joinchat/AAAAAFBiR81N-G5PrdfaGQ')],
                  [InlineKeyboardButton("Odessa region", url='https://t.me/joinchat/AAAAAEr_wruH7beqsPUaSQ')],
                  [InlineKeyboardButton("Lugansk region", url='https://t.me/joinchat/AAAAAEZYZfqyr-XX6VlgFA')],
                  [InlineKeyboardButton("Zaporozhye region", url='https://t.me/joinchat/AAAAAFk6eas2w3w5GGQs7g')],
                  [InlineKeyboardButton("Vinnytsia region", url='https://t.me/joinchat/AAAAAFiZX2OqDw6d1xSWdg')],
                  [InlineKeyboardButton("Poltava region", url='https://t.me/joinchat/AAAAAFMitTOOVnMN4mvbzg')],
                  [InlineKeyboardButton("Khmelnitsky region", url='https://t.me/joinchat/AAAAAEoEXQzLBw5g-EJHwQ')],
                  [InlineKeyboardButton("Transcarpathian region", url='https://t.me/joinchat/AAAAAEPTx2T6KfFHodAbMg')],
                  [InlineKeyboardButton("Zhytomyr Oblast", url='https://t.me/joinchat/AAAAAELxDhmG8v16yX21VA')],
                  [InlineKeyboardButton("Cherkasy region", url='https://t.me/joinchat/AAAAAFPMozHITJRIdt_QlQ')],
                  [InlineKeyboardButton("Ivano-Frankivsk", url='https://t.me/joinchat/AAAAAEx1VIR1vHhd-7lbMA')],
                  [InlineKeyboardButton("Rivne region", url='https://t.me/joinchat/AAAAAEx3VTq1fMFXee5cqA')],
                  [InlineKeyboardButton("Nikolaevkskaya area", url='https://t.me/joinchat/AAAAAFOkfl78AUXauKJWIA')],
                  [InlineKeyboardButton("Sumy region", url='https://t.me/joinchat/AAAAAEqj6zMZVYhapnATkw')],
                  [InlineKeyboardButton("Ternopil region", url='https://t.me/joinchat/AAAAAEwfgMTYQjj7nlZdlg')],
                  [InlineKeyboardButton("Kherson region", url='https://t.me/joinchat/AAAAAFdT-eK3dKzey7sP-w')],
                  [InlineKeyboardButton("Volyn Region", url='https://t.me/joinchat/AAAAAFa1RAVJxsszMO62VQ')],
                  [InlineKeyboardButton("Chernihiv region", url='https://t.me/joinchat/AAAAAEpFViPguk35su9d4g')],
                  [InlineKeyboardButton("Kirovograd Region", url='https://t.me/joinchat/AAAAAEqj6zMZVYhapnATkw')],
                  [InlineKeyboardButton("Chernivtsi region", url='https://t.me/joinchat/AAAAAExqOG_vOgDddTZpWg')],
                  [InlineKeyboardButton(back, callback_data='main_uaen')]] )



sub_main4 =InlineKeyboardMarkup( [ #kivun_kazahstan
                  [InlineKeyboardButton("Диллеры всей страны", url='https://t.me/joinchat/AAAAAEmt2GrccfdEValpwA')],
                  [InlineKeyboardButton("Акмолинская Область", url='https://t.me/joinchat/AAAAAEi8NvA4yo_kWvXbsg')],
                  [InlineKeyboardButton("Актюбинская Область", url='https://t.me/joinchat/AAAAAEhmJj7pZQXoJ2nFjg')],
                  [InlineKeyboardButton("Алматинская Область", url='https://t.me/joinchat/AAAAAE1CIFUGLZyIliWtGA')],
                  [InlineKeyboardButton("Атырауская Область", url='https://t.me/joinchat/AAAAAFFKvyKpe0NRj98cUg')],
                  [InlineKeyboardButton("Восточно-казахская Область", url='https://t.me/joinchat/AAAAAEZnQL1leXnim6EUMQ')],
                  [InlineKeyboardButton("Жамбылская Область", url='https://t.me/joinchat/AAAAAFV1G7vi4z6fP9DHsA')],
                  [InlineKeyboardButton("Западно-казахская Область", url='https://t.me/joinchat/AAAAAFQsj14aUS2D_H2Mug')],
                  [InlineKeyboardButton("Карагандийская Область", url='https://t.me/joinchat/AAAAAFb-ndZVXjv3MQ4iwA')],
                  [InlineKeyboardButton("Костанайская Область", url='https://t.me/joinchat/AAAAAFJvv7brz8O8Gd4S8g')],
                  [InlineKeyboardButton("Кызылординская Область", url='https://t.me/joinchat/AAAAAEZsOwy48XnkBDv0oQ')],
                  [InlineKeyboardButton("Мангистауская Область", url='https://t.me/joinchat/AAAAAE6AnkCCddDomf8M3w')],
                  [InlineKeyboardButton("Павлодарская Область", url='https://t.me/joinchat/AAAAAENMFtlnzJZ-7NoWRw')],
                  [InlineKeyboardButton("Северо-казахская Область", url='')],
                  [InlineKeyboardButton("Туркестанская Область", url='https://t.me/joinchat/AAAAAFLYxwhLNAq-9MMZLg')],
                  [InlineKeyboardButton(taf, callback_data='main_kaza')]] )

sub_main4en =InlineKeyboardMarkup( [ #kivun_kazahstan en
                  [InlineKeyboardButton("Dealers all over the country", url='https://t.me/joinchat/AAAAAEmt2GrccfdEValpwA')],
                  [InlineKeyboardButton("Akmola region", url='https://t.me/joinchat/AAAAAEi8NvA4yo_kWvXbsg')],
                  [InlineKeyboardButton("Aktobe region", url='https://t.me/joinchat/AAAAAEhmJj7pZQXoJ2nFjg')],
                  [InlineKeyboardButton("Alma-Ata's region", url='https://t.me/joinchat/AAAAAE1CIFUGLZyIliWtGA')],
                  [InlineKeyboardButton("Atyrau region", url='https://t.me/joinchat/AAAAAFFKvyKpe0NRj98cUg')],
                  [InlineKeyboardButton("East Kazakhstan Region", url='https://t.me/joinchat/AAAAAEZnQL1leXnim6EUMQ')],
                  [InlineKeyboardButton("Jambyl Region", url='https://t.me/joinchat/AAAAAFV1G7vi4z6fP9DHsA')],
                  [InlineKeyboardButton("West Kazakh Region", url='https://t.me/joinchat/AAAAAFQsj14aUS2D_H2Mug')],
                  [InlineKeyboardButton("Karaganda region", url='https://t.me/joinchat/AAAAAFb-ndZVXjv3MQ4iwA')],
                  [InlineKeyboardButton("Kostanay region", url='https://t.me/joinchat/AAAAAFJvv7brz8O8Gd4S8g')],
                  [InlineKeyboardButton("Kyzylorda Region", url='https://t.me/joinchat/AAAAAEZsOwy48XnkBDv0oQ')],
                  [InlineKeyboardButton("Mangistau region", url='https://t.me/joinchat/AAAAAE6AnkCCddDomf8M3w')],
                  [InlineKeyboardButton("Pavlodar region", url='https://t.me/joinchat/AAAAAENMFtlnzJZ-7NoWRw')],
                  [InlineKeyboardButton("North-Kazakh Region", url='')],
                  [InlineKeyboardButton("Turkestan Region", url='https://t.me/joinchat/AAAAAFLYxwhLNAq-9MMZLg')],
                  [InlineKeyboardButton(back, callback_data='main_kazaen')]] )


sub_main5 =InlineKeyboardMarkup( [ #kivun_belorus
                  [InlineKeyboardButton("Диллеры всей страны", url='https://t.me/joinchat/AAAAAFZrp4F8oZS3xVksYQ')],
                  [InlineKeyboardButton("Брестская Область", url='https://t.me/joinchat/AAAAAEnyyC8jDKUNwixJbQ')],
                  [InlineKeyboardButton("Витебская Область", url='https://t.me/joinchat/AAAAAFVxsw8M3A3CRihSDw')],
                  [InlineKeyboardButton("Гомельская Область", url='https://t.me/joinchat/AAAAAExGTkMvoAW9Vsnglw')],
                  [InlineKeyboardButton("Гродненская Область", url='https://t.me/joinchat/AAAAAExGZidVjNRZFI0ppA')],
                  [InlineKeyboardButton("Минская Область", url='https://t.me/joinchat/AAAAAE_xvuVeC2soJRE6-g')],
                  [InlineKeyboardButton("Могилевская Область", url='https://t.me/joinchat/AAAAAETw9Tmso0jI-20oLw')],
                  [InlineKeyboardButton(taf, callback_data='main_belo')]] )

sub_main5en =InlineKeyboardMarkup( [ #kivun_belorus en
                  [InlineKeyboardButton("Dealers all over the country", url='https://t.me/joinchat/AAAAAFZrp4F8oZS3xVksYQ')],
                  [InlineKeyboardButton("Brest region", url='https://t.me/joinchat/AAAAAEnyyC8jDKUNwixJbQ')],
                  [InlineKeyboardButton("Vitebsk Region", url='https://t.me/joinchat/AAAAAFVxsw8M3A3CRihSDw')],
                  [InlineKeyboardButton("Gomel region", url='https://t.me/joinchat/AAAAAExGTkMvoAW9Vsnglw')],
                  [InlineKeyboardButton("The Grodno region", url='https://t.me/joinchat/AAAAAExGZidVjNRZFI0ppA')],
                  [InlineKeyboardButton("Minsk Region", url='https://t.me/joinchat/AAAAAE_xvuVeC2soJRE6-g')],
                  [InlineKeyboardButton("Mogilev Region", url='https://t.me/joinchat/AAAAAETw9Tmso0jI-20oLw')],
                  [InlineKeyboardButton(back, callback_data='main_beloen')]] )


sub_main6 =InlineKeyboardMarkup( [ #kivun_armenia
                  [InlineKeyboardButton("Диллеры Армении", url='https://t.me/joinchat/AAAAAExilAEVe2ajCkhfYg')],
                  [InlineKeyboardButton("Арагацотнская область", url='https://t.me/joinchat/AAAAAE6RnAeHV_I6WF7FEg')],
                  [InlineKeyboardButton("Араратская область", url='https://t.me/joinchat/AAAAAEzQAk58W-QE0-lJww')],
                  [InlineKeyboardButton("Армавирская Область", url='https://t.me/joinchat/AAAAAFZeEBg8Wd8U3mVrig')],
                  [InlineKeyboardButton("Вайоцдзорская Область", url='https://t.me/joinchat/AAAAAFF25VKHl3oW2VB4Vg')],
                  [InlineKeyboardButton("Гехаркуникская Область", url='https://t.me/joinchat/AAAAAFQ4Bq10zPsbtCkd2A')],
                  [InlineKeyboardButton("Котайская Область", url='https://t.me/joinchat/AAAAAFYFTy63NqFdfjue5Q')],
                  [InlineKeyboardButton("Лорийская Область", url='https://t.me/joinchat/AAAAAEiiqKR-Off8thLrZg')],
                  [InlineKeyboardButton("Сюникская Область", url='https://t.me/joinchat/AAAAAE0Z6P75LIHQc9G-JQ')],
                  [InlineKeyboardButton("Тавушская область", url='https://t.me/joinchat/AAAAAFeeeSNpJPk56Qfo8Q')],
                  [InlineKeyboardButton("Ширакская Область", url='https://t.me/joinchat/AAAAAFgvANlKOgsE3NQdUQ')],
                  [InlineKeyboardButton("Ереван", url='https://t.me/joinchat/AAAAAFfWJALCL3jkM-Y7xg')],
                  [InlineKeyboardButton(taf, callback_data='main_ar')]] )

sub_main6en =InlineKeyboardMarkup( [ #kivun_armenia en
                  [InlineKeyboardButton("Dealers all over the country", url='https://t.me/joinchat/AAAAAExilAEVe2ajCkhfYg')],
                  [InlineKeyboardButton("Aragatsotn region", url='https://t.me/joinchat/AAAAAE6RnAeHV_I6WF7FEg')],
                  [InlineKeyboardButton("Ararat region", url='https://t.me/joinchat/AAAAAEzQAk58W-QE0-lJww')],
                  [InlineKeyboardButton("Armavir Region", url='https://t.me/joinchat/AAAAAFZeEBg8Wd8U3mVrig')],
                  [InlineKeyboardButton("Vayots Dzor Province", url='https://t.me/joinchat/AAAAAFF25VKHl3oW2VB4Vg')],
                  [InlineKeyboardButton("Gegharkunik region", url='https://t.me/joinchat/AAAAAFQ4Bq10zPsbtCkd2A')],
                  [InlineKeyboardButton("Kotay Province", url='https://t.me/joinchat/AAAAAFYFTy63NqFdfjue5Q')],
                  [InlineKeyboardButton("Lori Province", url='https://t.me/joinchat/AAAAAEiiqKR-Off8thLrZg')],
                  [InlineKeyboardButton("Syunik region", url='https://t.me/joinchat/AAAAAE0Z6P75LIHQc9G-JQ')],
                  [InlineKeyboardButton("Tavush region", url='https://t.me/joinchat/AAAAAFeeeSNpJPk56Qfo8Q')],
                  [InlineKeyboardButton("Shirak Province", url='https://t.me/joinchat/AAAAAFgvANlKOgsE3NQdUQ')],
                  [InlineKeyboardButton("Yerevan", url='https://t.me/joinchat/AAAAAFfWJALCL3jkM-Y7xg')],
                  [InlineKeyboardButton(back, callback_data='main_aren')]] )

sub_main3 =InlineKeyboardMarkup( [ #kivun_rus
                  [InlineKeyboardButton("Диллеры всей страны", url='https://t.me/joinchat/AAAAAFUokCOMgdD7KjwkTQ')],
                  [InlineKeyboardButton("Амурская Область", url='https://t.me/joinchat/AAAAAFUokCOMgdD7KjwkTQ')],
                  [InlineKeyboardButton("Архангельская Область", url='https://t.me/joinchat/AAAAAFJbnoZ8BNRGLnhkIQ')],
                  [InlineKeyboardButton("Астраханская Область", url='https://t.me/joinchat/AAAAAFahSbwEkUfSEBKLmQ')],
                  [InlineKeyboardButton("Белгородская область", url='https://t.me/joinchat/AAAAAEvnPucfBc747kGR7A')],
                  [InlineKeyboardButton("Брянская Область", url='https://t.me/joinchat/AAAAAEmCogFQgveSWi7ZhQ')],
                  [InlineKeyboardButton("Челябинская Область", url='https://t.me/joinchat/AAAAAE0bO9V6B23uD36EhA')],
                  [InlineKeyboardButton("Иркутская Область", url='https://t.me/joinchat/AAAAAFbTKI2CqNjrsapw2Q')],
                  [InlineKeyboardButton("Ивановская Область", url='https://t.me/joinchat/AAAAAFT_2c67ZHy9RCrdCA')],
                  [InlineKeyboardButton("Калининградская Область", url='https://t.me/joinchat/AAAAAFOJW1NtzFKTKf7cZQ')],
                  [InlineKeyboardButton("Калужская Область", url='https://t.me/joinchat/AAAAAFIQyPrPkUEysDt7jw')],
                  [InlineKeyboardButton("Кемеровская Область", url='https://t.me/joinchat/AAAAAFXRjXUConT4XqeN6w')],
                  [InlineKeyboardButton("Кировская Область", url='https://t.me/joinchat/AAAAAEbgcAR2nJPoclObiw')],
                  [InlineKeyboardButton("Костромская Область", url='https://t.me/joinchat/AAAAAEbfl9e3i9YvxXG7lw')],
                  [InlineKeyboardButton("Курганская Область", url='https://t.me/joinchat/AAAAAFihI893pwOHmcNAQA')],
                  [InlineKeyboardButton("Курская Облать", url='https://t.me/joinchat/AAAAAErCcBP5vnL-PApFVg')],
                  [InlineKeyboardButton("Ленинградская Область", url='https://t.me/joinchat/AAAAAE3dCaSKT8AvCGT4JA')],
                  [InlineKeyboardButton("Липецкая Область", url='https://t.me/joinchat/AAAAAFQQmYXCaqSBEvNvGQ')],
                  [InlineKeyboardButton("Магаданская Область", url='https://t.me/joinchat/AAAAAFFsbIiXnXxUqvEPWw')],
                  [InlineKeyboardButton("Московская Область", url='https://t.me/joinchat/AAAAAEhh6Y7JWC4mfyIxjQ')],
                  [InlineKeyboardButton("Мурманская Область", url='https://t.me/joinchat/AAAAAEb8OHM0M7RvlaEK9w')],
                  [InlineKeyboardButton("Нижегородская Область", url='https://t.me/joinchat/AAAAAFXsJPngmnAkuFuP2g')],
                  [InlineKeyboardButton("Новгородская Область", url='https://t.me/joinchat/AAAAAES3p5Ta5qRIHDmn-A')],
                  [InlineKeyboardButton("Новосибирская Область", url='https://t.me/joinchat/AAAAAEorNK0k-VD4HJq9sA')],
                  [InlineKeyboardButton("Омская Область", url='https://t.me/joinchat/AAAAAFWQVMFL7DAflsjfig')],
                  [InlineKeyboardButton("Оренбургская Область", url='https://t.me/joinchat/AAAAAFVuzUEQlYVSezjU9A')],
                  [InlineKeyboardButton("Орловская Область", url='https://t.me/joinchat/AAAAAE3XX41fkMHtHvzGEQ')],
                  [InlineKeyboardButton("Пензенская Область", url='https://t.me/joinchat/AAAAAFMtk8b9D2p3Xx22oA')],
                  [InlineKeyboardButton("Псковская Область", url='https://t.me/joinchat/AAAAAFbWfnD3QeNGgauE8g')],
                  [InlineKeyboardButton("Ростовская Область", url='https://t.me/joinchat/AAAAAE-wnbLKyQi82q2kgw')],
                  [InlineKeyboardButton("Рязанская Область", url='https://t.me/joinchat/AAAAAFCsQYTOyjn7S5zerg')],
                  [InlineKeyboardButton("Сахалинская Область", url='https://t.me/joinchat/AAAAAFKTX4NhWjYLPhsVHA')],
                  [InlineKeyboardButton("Самарская Область", url='https://t.me/joinchat/AAAAAEhwJcYGT8oMAfLuEg')],
                  [InlineKeyboardButton("Саратовская Область", url='https://t.me/joinchat/AAAAAFTSA7lxY1ET46669g')],
                  [InlineKeyboardButton("Смоленская Область", url='https://t.me/joinchat/AAAAAEZk86h56GLfFsu4Mw')],
                  [InlineKeyboardButton("Свердловская Область", url='https://t.me/joinchat/AAAAAEbkvDz8uFJb6YhZWA')],
                  [InlineKeyboardButton("Тамбовская Область", url='https://t.me/joinchat/AAAAAE2XsKkphGDUHw9l1A')],
                  [InlineKeyboardButton("Томская Область", url='https://t.me/joinchat/AAAAAEo4PydpR1LCBjXGYg')],
                  [InlineKeyboardButton("Тверская Область", url='https://t.me/joinchat/AAAAAFRunqls-xPGdQxCww')],
                  [InlineKeyboardButton("Тульская Область", url='https://t.me/joinchat/AAAAAFJjUX6THeNplgBs9g')],
                  [InlineKeyboardButton("Тюменская Область", url='https://t.me/joinchat/AAAAAE2mcngXGTKdwAS1-A')],
                  [InlineKeyboardButton("Ульяновская Область", url='https://t.me/joinchat/AAAAAFPxwtbo2Eed8N6C9A')],
                  [InlineKeyboardButton("Владимировская Область", url='https://t.me/joinchat/AAAAAFL9VojNMdP9Uktnyw')],
                  [InlineKeyboardButton("Волгоградская Область", url='https://t.me/joinchat/AAAAAEk14aAhFjoJR-AFQg')],
                  [InlineKeyboardButton("Вологодская Область", url='https://t.me/joinchat/AAAAAE0bt89FqhhCh882CQ')],
                  [InlineKeyboardButton("Воронежская Область", url='https://t.me/joinchat/AAAAAFTy0XuY5BwfuC9FNA')],
                  [InlineKeyboardButton("Ярославская Область", url='https://t.me/joinchat/AAAAAEQAGmEuKBoqCMGqCg')],
                  [InlineKeyboardButton(taf, callback_data='main_rus')]] )


sub_main3en =InlineKeyboardMarkup( [ #kivun_rus en
                  [InlineKeyboardButton("Dealers all over the country", url='https://t.me/joinchat/AAAAAFUokCOMgdD7KjwkTQ')],
                  [InlineKeyboardButton("Amur region", url='https://t.me/joinchat/AAAAAFUokCOMgdD7KjwkTQ')],
                  [InlineKeyboardButton("Arhangelsk region", url='https://t.me/joinchat/AAAAAFJbnoZ8BNRGLnhkIQ')],
                  [InlineKeyboardButton("Astrakhan Region", url='https://t.me/joinchat/AAAAAFahSbwEkUfSEBKLmQ')],
                  [InlineKeyboardButton("Belgorod region", url='https://t.me/joinchat/AAAAAEvnPucfBc747kGR7A')],
                  [InlineKeyboardButton("Bryansk Region", url='https://t.me/joinchat/AAAAAEmCogFQgveSWi7ZhQ')],
                  [InlineKeyboardButton("Chelyabinsk region", url='https://t.me/joinchat/AAAAAE0bO9V6B23uD36EhA')],
                  [InlineKeyboardButton("Irkutsk region", url='https://t.me/joinchat/AAAAAFbTKI2CqNjrsapw2Q')],
                  [InlineKeyboardButton("Ivanovo region", url='https://t.me/joinchat/AAAAAFT_2c67ZHy9RCrdCA')],
                  [InlineKeyboardButton("Kaliningrad region", url='https://t.me/joinchat/AAAAAFOJW1NtzFKTKf7cZQ')],
                  [InlineKeyboardButton("Kaluga region", url='https://t.me/joinchat/AAAAAFIQyPrPkUEysDt7jw')],
                  [InlineKeyboardButton("Kemerovo region", url='https://t.me/joinchat/AAAAAFXRjXUConT4XqeN6w')],
                  [InlineKeyboardButton("Kirov region", url='https://t.me/joinchat/AAAAAEbgcAR2nJPoclObiw')],
                  [InlineKeyboardButton("Kostroma region", url='https://t.me/joinchat/AAAAAEbfl9e3i9YvxXG7lw')],
                  [InlineKeyboardButton("Kurgan region", url='https://t.me/joinchat/AAAAAFihI893pwOHmcNAQA')],
                  [InlineKeyboardButton("Курская Облать", url='https://t.me/joinchat/AAAAAErCcBP5vnL-PApFVg')],
                  [InlineKeyboardButton("Leningrad region", url='https://t.me/joinchat/AAAAAE3dCaSKT8AvCGT4JA')],
                  [InlineKeyboardButton("Lipetsk Region", url='https://t.me/joinchat/AAAAAFQQmYXCaqSBEvNvGQ')],
                  [InlineKeyboardButton("Magadan Region", url='https://t.me/joinchat/AAAAAFFsbIiXnXxUqvEPWw')],
                  [InlineKeyboardButton("Moscow region", url='https://t.me/joinchat/AAAAAEhh6Y7JWC4mfyIxjQ')],
                  [InlineKeyboardButton("Murmansk region", url='https://t.me/joinchat/AAAAAEb8OHM0M7RvlaEK9w')],
                  [InlineKeyboardButton("Nizhny Novgorod Region", url='https://t.me/joinchat/AAAAAFXsJPngmnAkuFuP2g')],
                  [InlineKeyboardButton("Novgorod region", url='https://t.me/joinchat/AAAAAES3p5Ta5qRIHDmn-A')],
                  [InlineKeyboardButton("Novosibirsk region", url='https://t.me/joinchat/AAAAAEorNK0k-VD4HJq9sA')],
                  [InlineKeyboardButton("Omsk Region", url='https://t.me/joinchat/AAAAAFWQVMFL7DAflsjfig')],
                  [InlineKeyboardButton("Orenburg region", url='https://t.me/joinchat/AAAAAFVuzUEQlYVSezjU9A')],
                  [InlineKeyboardButton("Oryol Region", url='https://t.me/joinchat/AAAAAE3XX41fkMHtHvzGEQ')],
                  [InlineKeyboardButton("Penza region", url='https://t.me/joinchat/AAAAAFMtk8b9D2p3Xx22oA')],
                  [InlineKeyboardButton("Pskov region", url='https://t.me/joinchat/AAAAAFbWfnD3QeNGgauE8g')],
                  [InlineKeyboardButton("Rostov region", url='https://t.me/joinchat/AAAAAE-wnbLKyQi82q2kgw')],
                  [InlineKeyboardButton("Ryazan Oblast", url='https://t.me/joinchat/AAAAAFCsQYTOyjn7S5zerg')],
                  [InlineKeyboardButton("Sakhalin Region", url='https://t.me/joinchat/AAAAAFKTX4NhWjYLPhsVHA')],
                  [InlineKeyboardButton("Samara Region", url='https://t.me/joinchat/AAAAAEhwJcYGT8oMAfLuEg')],
                  [InlineKeyboardButton("Saratov region", url='https://t.me/joinchat/AAAAAFTSA7lxY1ET46669g')],
                  [InlineKeyboardButton("Smolensk region", url='https://t.me/joinchat/AAAAAEZk86h56GLfFsu4Mw')],
                  [InlineKeyboardButton("Sverdlovsk region", url='https://t.me/joinchat/AAAAAEbkvDz8uFJb6YhZWA')],
                  [InlineKeyboardButton("Tambov Region", url='https://t.me/joinchat/AAAAAE2XsKkphGDUHw9l1A')],
                  [InlineKeyboardButton("Tomsk region", url='https://t.me/joinchat/AAAAAEo4PydpR1LCBjXGYg')],
                  [InlineKeyboardButton("Tver region", url='https://t.me/joinchat/AAAAAFRunqls-xPGdQxCww')],
                  [InlineKeyboardButton("Tula region", url='https://t.me/joinchat/AAAAAFJjUX6THeNplgBs9g')],
                  [InlineKeyboardButton("Tyumen region", url='https://t.me/joinchat/AAAAAE2mcngXGTKdwAS1-A')],
                  [InlineKeyboardButton("Ulyanovsk region", url='https://t.me/joinchat/AAAAAFPxwtbo2Eed8N6C9A')],
                  [InlineKeyboardButton("Vladimir region", url='https://t.me/joinchat/AAAAAFL9VojNMdP9Uktnyw')],
                  [InlineKeyboardButton("Volgograd Regionь", url='https://t.me/joinchat/AAAAAEk14aAhFjoJR-AFQg')],
                  [InlineKeyboardButton("Vologodskaya Oblast", url='https://t.me/joinchat/AAAAAE0bt89FqhhCh882CQ')],
                  [InlineKeyboardButton("Voronezh region", url='https://t.me/joinchat/AAAAAFTy0XuY5BwfuC9FNA')],
                  [InlineKeyboardButton("Yaroslavl region", url='https://t.me/joinchat/AAAAAEQAGmEuKBoqCMGqCg')],
                  [InlineKeyboardButton(back, callback_data='main_rusen')]] )


sub_main7 =InlineKeyboardMarkup( [ #kivun_uzbekistan
                  [InlineKeyboardButton("Диллеры всей страны", url='https://t.me/joinchat/AAAAAFcxQh_oi72pHMcHiw')],
                  [InlineKeyboardButton("Анджианская Область", url='https://t.me/joinchat/AAAAAEUzpybmNKNAJtkXGA')],
                  [InlineKeyboardButton("Бухарская Область", url='https://t.me/joinchat/AAAAAFba4t_BuikYLiEkLw')],
                  [InlineKeyboardButton("Джизакская Область", url='https://t.me/joinchat/AAAAAE27eF0vZhFpUlSQ7w')],
                  [InlineKeyboardButton("Кашкадарьинская Область", url='https://t.me/joinchat/AAAAAEYa8cdPZpHEW6ivWg')],
                  [InlineKeyboardButton("Навойская Область", url='https://t.me/joinchat/AAAAAFAILwj0EhZAhNa44g')],
                  [InlineKeyboardButton("Намаганская Область", url='https://t.me/joinchat/AAAAAFSwPTt7lIV87pCaow')],
                  [InlineKeyboardButton("Самаркандская Область", url='https://t.me/joinchat/AAAAAExoz67ge_RQmTZm8w')],
                  [InlineKeyboardButton("Сырдарьинская Область", url='https://t.me/joinchat/AAAAAE88dN_4-bRT8WbxjA')],
                  [InlineKeyboardButton("Сурхандарьинская Область", url='https://t.me/joinchat/AAAAAE1bEtDlE5l4GLw2bQ')],
                  [InlineKeyboardButton("Ташкентская Область", url='https://t.me/joinchat/AAAAAFVZiUvfHG5VxHVT8w')],
                  [InlineKeyboardButton("Ферганская Область", url='https://t.me/joinchat/AAAAAFjCsIULzwhlWTWz2A')],
                  [InlineKeyboardButton("Хорезмская Область", url='https://t.me/joinchat/AAAAAE0T6H9i6CGCiT0hdw')],
                  [InlineKeyboardButton(taf, callback_data='main_uz')]] )


sub_main7en =InlineKeyboardMarkup( [ #kivun_uzbekistan en
                  [InlineKeyboardButton("Dealers all over the country", url='https://t.me/joinchat/AAAAAFcxQh_oi72pHMcHiw')],
                  [InlineKeyboardButton("Anjian Province", url='https://t.me/joinchat/AAAAAEUzpybmNKNAJtkXGA')],
                  [InlineKeyboardButton("Bukhara region", url='https://t.me/joinchat/AAAAAFba4t_BuikYLiEkLw')],
                  [InlineKeyboardButton("Jizzakh region", url='https://t.me/joinchat/AAAAAE27eF0vZhFpUlSQ7w')],
                  [InlineKeyboardButton("Kashkadarya region", url='https://t.me/joinchat/AAAAAEYa8cdPZpHEW6ivWg')],
                  [InlineKeyboardButton("Navoi Region", url='https://t.me/joinchat/AAAAAFAILwj0EhZAhNa44g')],
                  [InlineKeyboardButton("Namagan Region", url='https://t.me/joinchat/AAAAAFSwPTt7lIV87pCaow')],
                  [InlineKeyboardButton("Samarkand region", url='https://t.me/joinchat/AAAAAExoz67ge_RQmTZm8w')],
                  [InlineKeyboardButton("Syrdarya region", url='https://t.me/joinchat/AAAAAE88dN_4-bRT8WbxjA')],
                  [InlineKeyboardButton("Syrdarya region", url='https://t.me/joinchat/AAAAAE1bEtDlE5l4GLw2bQ')],
                  [InlineKeyboardButton("Tashkent region", url='https://t.me/joinchat/AAAAAFVZiUvfHG5VxHVT8w')],
                  [InlineKeyboardButton("Fergana region", url='https://t.me/joinchat/AAAAAFjCsIULzwhlWTWz2A')],
                  [InlineKeyboardButton("Khorezm Region", url='https://t.me/joinchat/AAAAAE0T6H9i6CGCiT0hdw')],
                  [InlineKeyboardButton(back, callback_data='main_uzen')]] )


sub_main8 =InlineKeyboardMarkup( [ #kivun_turkmenistan
                  [InlineKeyboardButton("Диллеры всей страны", url='https://t.me/joinchat/AAAAAFLu7fLBudZejEVTRQ')],
                  [InlineKeyboardButton("Ашхабад", url='https://t.me/joinchat/AAAAAEm3Em_i-Jc8j1sGog')],
                  [InlineKeyboardButton("Ахалский Велаят", url='https://t.me/joinchat/AAAAAEhGkQfp6X7b626hqw')],
                  [InlineKeyboardButton("Балканский Велаят", url='https://t.me/joinchat/AAAAAE2CVOYVW5HM_CPp9g')],
                  [InlineKeyboardButton("Дашогузский Велаят", url='https://t.me/joinchat/AAAAAEgruf0OpIchScqwtA')],
                  [InlineKeyboardButton("Лебапский Велаят", url='https://t.me/joinchat/AAAAAFNTFBr2LBB8Wr-QmQ')],
                  [InlineKeyboardButton(taf, callback_data='main_tur')]] )

sub_main8en =InlineKeyboardMarkup( [ #kivun_turkmenistan en
                  [InlineKeyboardButton("Dealers all over the country", url='https://t.me/joinchat/AAAAAFLu7fLBudZejEVTRQ')],
                  [InlineKeyboardButton("Ashgabat", url='https://t.me/joinchat/AAAAAEm3Em_i-Jc8j1sGog')],
                  [InlineKeyboardButton("Akhal Velayat", url='https://t.me/joinchat/AAAAAEhGkQfp6X7b626hqw')],
                  [InlineKeyboardButton("Balkan Velayat", url='https://t.me/joinchat/AAAAAE2CVOYVW5HM_CPp9g')],
                  [InlineKeyboardButton("Dashoguz Velayat", url='https://t.me/joinchat/AAAAAEgruf0OpIchScqwtA')],
                  [InlineKeyboardButton("Lebap Velayat", url='https://t.me/joinchat/AAAAAFNTFBr2LBB8Wr-QmQ')],
                  [InlineKeyboardButton(back, callback_data='main_turen')]] )



sub_main9 =InlineKeyboardMarkup( [ #kivun_azerbaijan
                  [InlineKeyboardButton("Диллеры всей страны", url='https://t.me/joinchat/AAAAAFJUDCUNYzHg_XHRxg')],
                  [InlineKeyboardButton("Баку", url='https://t.me/joinchat/AAAAAFgYslucZjcXNYrLJw')],
                  [InlineKeyboardButton("Гянджа", url='https://t.me/joinchat/AAAAAFAPbXcYw38_tb1jQw')],
                  [InlineKeyboardButton("Евлах", url='https://t.me/joinchat/AAAAAFkdyuz4aAi0jkzmrQ')],
                  [InlineKeyboardButton("Ленкорань", url='https://t.me/joinchat/AAAAAFc9xpFZECKzJdfrzA')],
                  [InlineKeyboardButton("Мингечевир", url='https://t.me/joinchat/AAAAAEaw4B5hlgV1yDB-Kw')],
                  [InlineKeyboardButton("Нафталан", url='https://t.me/joinchat/AAAAAFL_8DkdSTUuYW9lDw')],
                  [InlineKeyboardButton("Нахичевань", url='https://t.me/joinchat/AAAAAEjROYAcTrwbGqUEGQ')],
                  [InlineKeyboardButton("Степанакерт", url='https://t.me/joinchat/AAAAAEcu9lymqZEU1lJUKQ')],
                  [InlineKeyboardButton("Сумгаит", url='https://t.me/joinchat/AAAAAFi4hDw33QzeLmuXXA')],
                  [InlineKeyboardButton("Шеки", url='https://t.me/joinchat/AAAAAEgYCQrSsYXyfw84Ug')],
                  [InlineKeyboardButton("Ширван", url='https://t.me/joinchat/AAAAAFULMpujQGrIG6LN4A')],
                  [InlineKeyboardButton("Шуша", url='https://t.me/joinchat/AAAAAFH5DBapokvPWNpaew')],
                  [InlineKeyboardButton(taf, callback_data='main_azer')]] )

sub_main9en =InlineKeyboardMarkup( [ #kivun_azerbaijan en
                  [InlineKeyboardButton("Dealers all over the country", url='https://t.me/joinchat/AAAAAFJUDCUNYzHg_XHRxg')],
                  [InlineKeyboardButton("Baku", url='https://t.me/joinchat/AAAAAFgYslucZjcXNYrLJw')],
                  [InlineKeyboardButton("Ganja", url='https://t.me/joinchat/AAAAAFAPbXcYw38_tb1jQw')],
                  [InlineKeyboardButton("Yevlakh", url='https://t.me/joinchat/AAAAAFkdyuz4aAi0jkzmrQ')],
                  [InlineKeyboardButton("Lankaran", url='https://t.me/joinchat/AAAAAFc9xpFZECKzJdfrzA')],
                  [InlineKeyboardButton("Mingachevir", url='https://t.me/joinchat/AAAAAEaw4B5hlgV1yDB-Kw')],
                  [InlineKeyboardButton("Naftalan", url='https://t.me/joinchat/AAAAAFL_8DkdSTUuYW9lDw')],
                  [InlineKeyboardButton("Nakhichevan", url='https://t.me/joinchat/AAAAAEjROYAcTrwbGqUEGQ')],
                  [InlineKeyboardButton("Stepanakert", url='https://t.me/joinchat/AAAAAEcu9lymqZEU1lJUKQ')],
                  [InlineKeyboardButton("Sumgait", url='https://t.me/joinchat/AAAAAFi4hDw33QzeLmuXXA')],
                  [InlineKeyboardButton("Sheki", url='https://t.me/joinchat/AAAAAEgYCQrSsYXyfw84Ug')],
                  [InlineKeyboardButton("Shirvan", url='https://t.me/joinchat/AAAAAFULMpujQGrIG6LN4A')],
                  [InlineKeyboardButton("Shusha", url='https://t.me/joinchat/AAAAAFH5DBapokvPWNpaew')],
                  [InlineKeyboardButton(back, callback_data='main_azeren')]] )


sub_main_10 =InlineKeyboardMarkup( [ #kivun_tdj
                  [InlineKeyboardButton("Диллеры всей страны", url='https://t.me/joinchat/AAAAAFYDU-9WG_hgmwi_EA')],
                  [InlineKeyboardButton("Душанбе", url='https://t.me/joinchat/AAAAAFVdUTz78k1E78zikw')],
                  [InlineKeyboardButton("Горно-бадашханская Область", url='https://t.me/joinchat/AAAAAEzpvjQ5oo5HkHFZhA')],
                  [InlineKeyboardButton("Согдийская Область", url='https://t.me/joinchat/AAAAAFH6jjnpSyD143fPfQ')],
                  [InlineKeyboardButton("Хатлонская Область", url='https://t.me/joinchat/AAAAAE2K9NZxc3iXlSIXag')],
                  [InlineKeyboardButton(taf, callback_data='main_tdj')]] )



sub_main_10en =InlineKeyboardMarkup( [ #kivun_tdj en
                  [InlineKeyboardButton("Dealers all over the country", url='https://t.me/joinchat/AAAAAFYDU-9WG_hgmwi_EA')],
                  [InlineKeyboardButton("Dushanbe", url='https://t.me/joinchat/AAAAAFVdUTz78k1E78zikw')],
                  [InlineKeyboardButton("Gorno-Badashkhan Region", url='https://t.me/joinchat/AAAAAEzpvjQ5oo5HkHFZhA')],
                  [InlineKeyboardButton("Sughd Region", url='https://t.me/joinchat/AAAAAFH6jjnpSyD143fPfQ')],
                  [InlineKeyboardButton("Khatlon Region", url='https://t.me/joinchat/AAAAAE2K9NZxc3iXlSIXag')],
                  [InlineKeyboardButton(back, callback_data='main_tdjen')]] )



sub_main_11 =InlineKeyboardMarkup( [ #kivun_moldavia
                  [InlineKeyboardButton("Диллеры всей страны", url='https://t.me/joinchat/AAAAAEiI2tlGwzfFLgQEgw')],
                  [InlineKeyboardButton("Бассарабский район", url='https://t.me/joinchat/AAAAAFHS16okXuqGtLsrmw')],
                  [InlineKeyboardButton("Бричанский район", url='https://t.me/joinchat/AAAAAE6JCDAPQZkC3H2LHQ')],
                  [InlineKeyboardButton("Дондюшанский район", url='https://t.me/joinchat/AAAAAFLNcC8XUQKqhWvsMg')],
                  [InlineKeyboardButton("Дрокиевский район", url='https://t.me/joinchat/AAAAAEejiVndCppPlh7-Wg')],
                  [InlineKeyboardButton("Дубоссарский район", url='https://t.me/joinchat/AAAAAEidWmgGT93l4QTohQ')],
                  [InlineKeyboardButton("Единецкий район", url='https://t.me/joinchat/AAAAAEVzhz6ARcCV-gda4Q')],
                  [InlineKeyboardButton("Кагульский район", url='https://t.me/joinchat/AAAAAFNqgiMfZmQuwA1CWw')],
                  [InlineKeyboardButton("Каларашский район", url='https://t.me/joinchat/AAAAAELCzkPOjaDL5Xx6Bw')],
                  [InlineKeyboardButton("Кантемирский район", url='https://t.me/joinchat/AAAAAETAsxzALb0Smk4BOA')],
                  [InlineKeyboardButton("Каушанский район", url='https://t.me/joinchat/AAAAAFWMcVD69ioVP_d1Pg')],
                  [InlineKeyboardButton("Криулянский район", url='https://t.me/joinchat/AAAAAEsI3g5dQWU2dJ3MRw')],
                  [InlineKeyboardButton("Леовский район", url='https://t.me/joinchat/AAAAAEVXYnrpjJBNL_0l7g')],
                  [InlineKeyboardButton("Ниспоренский район", url='https://t.me/joinchat/AAAAAFQRa0lNc7HT5FR_Ww')],
                  [InlineKeyboardButton("Новоаненский район", url='https://t.me/joinchat/AAAAAE0bBnu_xJwbKpwYmQ')],
                  [InlineKeyboardButton("Окницкий район", url='https://t.me/joinchat/AAAAAFG4TVugbELuINvy7Q')],
                  [InlineKeyboardButton("Резинский район", url='https://t.me/joinchat/AAAAAE5MQrNsuxqeOiotfA')],
                  [InlineKeyboardButton("Рышканский район", url='https://t.me/joinchat/AAAAAEgxuelZ72O9rzDoxA')],
                  [InlineKeyboardButton("Сорокский район", url='https://t.me/joinchat/AAAAAFETqDpf-uKM7IIx-w')],
                  [InlineKeyboardButton("Страшенский район", url='https://t.me/joinchat/AAAAAE3LRM4MELhFSIllXg')],
                  [InlineKeyboardButton("Сынжерейский район", url='https://t.me/joinchat/AAAAAE4rpd9CYUiNtojAqg')],
                  [InlineKeyboardButton("Тараклийский район", url='https://t.me/joinchat/AAAAAEaq2IRE9FWvJg3Yeg')],
                  [InlineKeyboardButton("Теленешский район", url='https://t.me/joinchat/AAAAAFYg5HPmJTCml4eRyg')],
                  [InlineKeyboardButton("Унгенский район", url='https://t.me/joinchat/AAAAAEzcRIiFelbgbb-YMA')],
                  [InlineKeyboardButton("Фалештский район", url='https://t.me/joinchat/AAAAAE1x9j-4LswWa7uFuA')],
                  [InlineKeyboardButton("Флорешский район", url='https://t.me/joinchat/AAAAAFb3mQAFtqoOTUxXkw')],
                  [InlineKeyboardButton("Хынчештский район", url='https://t.me/joinchat/AAAAAFDjYVoEfxci_KtTww')],
                  [InlineKeyboardButton("Чимишлийский район", url='https://t.me/joinchat/AAAAAEzYiy0lCi_gJ-jgng')],
                  [InlineKeyboardButton("Шолдагештский район", url='https://t.me/joinchat/AAAAAFX4K8vZA5m-FfE7iA')],
                  [InlineKeyboardButton("Штефан-Водский район", url='https://t.me/joinchat/AAAAAEpYeY5iFIdiEIwHuQ')],
                  [InlineKeyboardButton("Яловенский район", url='https://t.me/joinchat/AAAAAFJwDgw9KG8rXZaRJQ')],
                  [InlineKeyboardButton(taf, callback_data='main_mol')]] )


sub_main_11en =InlineKeyboardMarkup( [ #kivun_moldavia en
                  [InlineKeyboardButton("Dealers all over the country", url='https://t.me/joinchat/AAAAAEiI2tlGwzfFLgQEgw')],
                  [InlineKeyboardButton("Bassarabian region", url='https://t.me/joinchat/AAAAAFHS16okXuqGtLsrmw')],
                  [InlineKeyboardButton("Brichansky district", url='https://t.me/joinchat/AAAAAE6JCDAPQZkC3H2LHQ')],
                  [InlineKeyboardButton("Dondyushan district", url='https://t.me/joinchat/AAAAAFLNcC8XUQKqhWvsMg')],
                  [InlineKeyboardButton("Дрокиевский район", url='https://t.me/joinchat/AAAAAEejiVndCppPlh7-Wg')],
                  [InlineKeyboardButton("Dubossary district", url='https://t.me/joinchat/AAAAAEidWmgGT93l4QTohQ')],
                  [InlineKeyboardButton("Edinets district", url='https://t.me/joinchat/AAAAAEVzhz6ARcCV-gda4Q')],
                  [InlineKeyboardButton("Cahul district", url='https://t.me/joinchat/AAAAAFNqgiMfZmQuwA1CWw')],
                  [InlineKeyboardButton("Kalarash district", url='https://t.me/joinchat/AAAAAELCzkPOjaDL5Xx6Bw')],
                  [InlineKeyboardButton("Kantemir district", url='https://t.me/joinchat/AAAAAETAsxzALb0Smk4BOA')],
                  [InlineKeyboardButton("Kaushany district", url='https://t.me/joinchat/AAAAAFWMcVD69ioVP_d1Pg')],
                  [InlineKeyboardButton("Criuleni region", url='https://t.me/joinchat/AAAAAEsI3g5dQWU2dJ3MRw')],
                  [InlineKeyboardButton("Leovskiy district", url='https://t.me/joinchat/AAAAAEVXYnrpjJBNL_0l7g')],
                  [InlineKeyboardButton("Nisporensky district", url='https://t.me/joinchat/AAAAAFQRa0lNc7HT5FR_Ww')],
                  [InlineKeyboardButton("Novoanensky district", url='https://t.me/joinchat/AAAAAE0bBnu_xJwbKpwYmQ')],
                  [InlineKeyboardButton("Ocnitsa region", url='https://t.me/joinchat/AAAAAFG4TVugbELuINvy7Q')],
                  [InlineKeyboardButton("Rezinsky district", url='https://t.me/joinchat/AAAAAE5MQrNsuxqeOiotfA')],
                  [InlineKeyboardButton("Riscani region", url='https://t.me/joinchat/AAAAAEgxuelZ72O9rzDoxA')],
                  [InlineKeyboardButton("Soroksky district", url='https://t.me/joinchat/AAAAAFETqDpf-uKM7IIx-w')],
                  [InlineKeyboardButton("Strashensky district", url='https://t.me/joinchat/AAAAAE3LRM4MELhFSIllXg')],
                  [InlineKeyboardButton("Singerei district", url='https://t.me/joinchat/AAAAAE4rpd9CYUiNtojAqg')],
                  [InlineKeyboardButton("Taraclia region", url='https://t.me/joinchat/AAAAAEaq2IRE9FWvJg3Yeg')],
                  [InlineKeyboardButton("Telenesh district", url='https://t.me/joinchat/AAAAAFYg5HPmJTCml4eRyg')],
                  [InlineKeyboardButton("Ungheni district", url='https://t.me/joinchat/AAAAAEzcRIiFelbgbb-YMA')],
                  [InlineKeyboardButton("Falesti district", url='https://t.me/joinchat/AAAAAE1x9j-4LswWa7uFuA')],
                  [InlineKeyboardButton("Floreshsky district", url='https://t.me/joinchat/AAAAAFb3mQAFtqoOTUxXkw')],
                  [InlineKeyboardButton("Hincesti region", url='https://t.me/joinchat/AAAAAFDjYVoEfxci_KtTww')],
                  [InlineKeyboardButton("Cimislia region", url='https://t.me/joinchat/AAAAAEzYiy0lCi_gJ-jgng')],
                  [InlineKeyboardButton("Soldageshti district", url='https://t.me/joinchat/AAAAAFX4K8vZA5m-FfE7iA')],
                  [InlineKeyboardButton("Stefan Vodsky district", url='https://t.me/joinchat/AAAAAEpYeY5iFIdiEIwHuQ')],
                  [InlineKeyboardButton("Yalovensky district", url='https://t.me/joinchat/AAAAAFJwDgw9KG8rXZaRJQ')],
                  [InlineKeyboardButton(back, callback_data='main_molen')]] )


sub_main_12 =InlineKeyboardMarkup( [ #kivun_kirgizstan
                  [InlineKeyboardButton("Диллеры всей страны", url='https://t.me/joinchat/AAAAAEPF06bMxdWHp6v9sQ')],
                  [InlineKeyboardButton("Баткенская область", url='https://t.me/joinchat/AAAAAEmJMLt1yx1pWuSmcA')],
                  [InlineKeyboardButton("Таласская область", url='https://t.me/joinchat/AAAAAFRCTvc3G1VjFvAFhg')],
                  [InlineKeyboardButton("Нарынская область", url='https://t.me/joinchat/AAAAAFUOcIcN5kdq-9NndA')],
                  [InlineKeyboardButton("Ошская область", url='https://t.me/joinchat/AAAAAE1lvseI6QzT--QP_w')],
                  [InlineKeyboardButton("Джалал-Абадская область", url='https://t.me/joinchat/AAAAAEuinMEFtcLWpanKWg')],
                  [InlineKeyboardButton("Иссык-Кульская область", url='https://t.me/joinchat/AAAAAFH4qj73APiBOrin5g')],
                  [InlineKeyboardButton("Чуйская область", url='https://t.me/joinchat/AAAAAFljC9PruMzyi79w1A')],
                  [InlineKeyboardButton(taf, callback_data='main_kir')]] )

sub_main_12en =InlineKeyboardMarkup( [ #kivun_kirgizstan en
                  [InlineKeyboardButton("Dealers all over the country", url='https://t.me/joinchat/AAAAAEPF06bMxdWHp6v9sQ')],
                  [InlineKeyboardButton("Batken regionь", url='https://t.me/joinchat/AAAAAEmJMLt1yx1pWuSmcA')],
                  [InlineKeyboardButton("Talas region", url='https://t.me/joinchat/AAAAAFRCTvc3G1VjFvAFhg')],
                  [InlineKeyboardButton("Naryn region", url='https://t.me/joinchat/AAAAAFUOcIcN5kdq-9NndA')],
                  [InlineKeyboardButton("Osh region", url='https://t.me/joinchat/AAAAAE1lvseI6QzT--QP_w')],
                  [InlineKeyboardButton("Jalal-Abad region", url='https://t.me/joinchat/AAAAAEuinMEFtcLWpanKWg')],
                  [InlineKeyboardButton("Issyk-Kul region", url='https://t.me/joinchat/AAAAAFH4qj73APiBOrin5g')],
                  [InlineKeyboardButton("Chui area", url='https://t.me/joinchat/AAAAAFljC9PruMzyi79w1A')],
                  [InlineKeyboardButton(back, callback_data='main_kiren')]] )








logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(welcome_picture, 'rb'), caption=lang_message,
                          reply_markup=lang_main, supports_streaming=True)

def main_en_func(update,context):
    query = update.callback_query
    query.edit_message_caption(en_message, reply_markup=main_en)

def main_main_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(welcome_picture, 'rb'), caption=welcome_picture,
                          reply_markup=main_main, supports_streaming=True)

#def main_en_func(update,context):
 #   context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(welcome_picture, 'rb'), caption=welcome_picture,
 #                         reply_markup=main_main, supports_streaming=True)

def main_ua_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(ua_picture, 'rb'), caption=ua_message,
                          reply_markup=main_keyboard, supports_streaming=True)

#def main_ua_func(update,context):
#    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(ua_picture, 'rb'), caption=ua_message,
#                          reply_markup=main_keyboard, supports_streaming=True)

def main_rus_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(rus_picture, 'rb'), caption=rus_message,
                          reply_markup=main_keyboard1, supports_streaming=True)

def main_kaza_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("kaza.JPG", 'rb'), caption=kaza_message,
                          reply_markup=main_keyboard_kaza, supports_streaming=True)


def main_belo_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("belo.JPG", 'rb'), caption=belo_message,
                          reply_markup=main_keyboard_kaza, supports_streaming=True)

def main_ar_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("ar.JPG", 'rb'), caption=ar_message,
                          reply_markup=main_keyboard_ar, supports_streaming=True)

def main_uz_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("uz.JPG", 'rb'), caption=uz_message,
                          reply_markup=main_keyboard_uz, supports_streaming=True)

def main_tur_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("tur.JPG", 'rb'), caption=tur_message,
                          reply_markup=main_keyboard_tur, supports_streaming=True)


def main_azer_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("azer.JPG", 'rb'), caption=azer_message,
                          reply_markup=main_keyboard_azer, supports_streaming=True)

def main_tdj_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("tdj.JPG", 'rb'), caption=tdj_message,
                          reply_markup=main_keyboard_tdj, supports_streaming=True)

def main_mol_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("mol.JPG", 'rb'), caption=mol_message,
                          reply_markup=main_keyboard_mol, supports_streaming=True)

def main_kir_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("kir.JPG", 'rb'), caption=kir_message,
                          reply_markup=main_keyboard_kir, supports_streaming=True)


def sub_main0_func(update,context):
    query = update.callback_query
    query.edit_message_caption(ua_message, reply_markup=sub_main0)



def sub_main0_rus_func(update,context):
    query = update.callback_query
    query.edit_message_caption(rus_message, reply_markup=sub_main0_rus)

def sub_main0_kaza_func(update,context):
    query = update.callback_query
    query.edit_message_caption(kaza_message, reply_markup=sub_main0_kaza)


def sub_main0_belo_func(update,context):
    query = update.callback_query
    query.edit_message_caption(belo_message, reply_markup=sub_main0_belo)


def sub_main0_ar_func(update,context):
    query = update.callback_query
    query.edit_message_caption(ar_message, reply_markup=sub_main0_ar)

def sub_main0_uz_func(update,context):
    query = update.callback_query
    query.edit_message_caption(uz_message, reply_markup=sub_main0_uz)

def sub_main0_tur_func(update,context):
    query = update.callback_query
    query.edit_message_caption(tur_message, reply_markup=sub_main0_tur)

def sub_main0_azer_func(update,context):
    query = update.callback_query
    query.edit_message_caption(azer_message, reply_markup=sub_main0_azer)

def sub_main0_tdj_func(update,context):
    query = update.callback_query
    query.edit_message_caption(tdj_message, reply_markup=sub_main0_tdj)

def sub_main0_mol_func(update,context):
    query = update.callback_query
    query.edit_message_caption(mol_message, reply_markup=sub_main0_mol)

def sub_main0_kir_func(update,context):
    query = update.callback_query
    query.edit_message_caption(kir_message, reply_markup=sub_main0_kir)



def sub_main1_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main1)

def sub_main3_func(update,context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main3)

def sub_main4_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main4)


def sub_main5_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main5)

def sub_main7_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main7)

def sub_main8_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main8)

def sub_main6_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main6)


def sub_main9_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main9)

def sub_main_10_func(update,context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main_10)

def sub_main_11_func(update,context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main_11)

def sub_main_12_func(update,context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main_12)


def back_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(ua_picture, 'rb'), caption=ua_message,
                          reply_markup=main_keyboard, supports_streaming=True)
    #query.edit_message_caption(welcome_message, reply_markup=main_keyboard)

def back_rus_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(rus_picture, 'rb'), caption=rus_message,
                          reply_markup=main_keyboard1, supports_streaming=True)

def back_kaza_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(kaza_picture, 'rb'), caption=kaza_message,
                          reply_markup=main_keyboard_kaza, supports_streaming=True)


def back_belo_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(belo_picture, 'rb'), caption=belo_message,
                          reply_markup=main_keyboard_belo, supports_streaming=True)


def back_ar_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(ar_picture, 'rb'), caption=ar_message,
                          reply_markup=main_keyboard_ar, supports_streaming=True)

def back_uz_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(uz_picture, 'rb'), caption=uz_message,
                          reply_markup=main_keyboard_uz, supports_streaming=True)

def back_tur_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(tur_picture, 'rb'), caption=tur_message,
                          reply_markup=main_keyboard_tur, supports_streaming=True)

def back_azer_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(azer_picture, 'rb'), caption=azer_message,
                          reply_markup=main_keyboard_azer, supports_streaming=True)

def back_tdj_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(tdj_picture, 'rb'), caption=tdj_message,
                          reply_markup=main_keyboard_tdj, supports_streaming=True)

def back_mol_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(mol_picture, 'rb'), caption=mol_message,
                          reply_markup=main_keyboard_mol, supports_streaming=True)

def back_kir_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(kir_picture, 'rb'), caption=kir_message,
                          reply_markup=main_keyboard_kir, supports_streaming=True)

def main_uaen_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(ua_picture, 'rb'), caption=ua_message,
                          reply_markup=main_keyboard, supports_streaming=True)

def main_rusen_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(rus_picture, 'rb'), caption=rus_message,
                          reply_markup=main_keyboard1, supports_streaming=True)

def main_kazaen_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("kaza.JPG", 'rb'), caption=kaza_message,
                          reply_markup=main_keyboard_kaza, supports_streaming=True)


def main_beloen_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("belo.JPG", 'rb'), caption=belo_message,
                          reply_markup=main_keyboard_kaza, supports_streaming=True)

def main_aren_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("ar.JPG", 'rb'), caption=ar_message,
                          reply_markup=main_keyboard_ar, supports_streaming=True)

def main_uzen_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("uz.JPG", 'rb'), caption=uz_message,
                          reply_markup=main_keyboard_uz, supports_streaming=True)

def main_turen_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("tur.JPG", 'rb'), caption=tur_message,
                          reply_markup=main_keyboard_tur, supports_streaming=True)


def main_azeren_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("azer.JPG", 'rb'), caption=azer_message,
                          reply_markup=main_keyboard_azer, supports_streaming=True)

def main_tdjen_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("tdj.JPG", 'rb'), caption=tdj_message,
                          reply_markup=main_keyboard_tdj, supports_streaming=True)

def main_molen_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("mol.JPG", 'rb'), caption=mol_message,
                          reply_markup=main_keyboard_mol, supports_streaming=True)

def main_kiren_func(update,context):
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open("kir.JPG", 'rb'), caption=kir_message,
                          reply_markup=main_keyboard_kir, supports_streaming=True)


def sub_main0en_func(update,context):
    query = update.callback_query
    query.edit_message_caption(ua_message, reply_markup=sub_main0en)



def sub_main0_rusen_func(update,context):
    query = update.callback_query
    query.edit_message_caption(rus_message, reply_markup=sub_main0_rusen)

def sub_main0_kazaen_func(update,context):
    query = update.callback_query
    query.edit_message_caption(kaza_message, reply_markup=sub_main0_kazaen)


def sub_main0_beloen_func(update,context):
    query = update.callback_query
    query.edit_message_caption(belo_message, reply_markup=sub_main0_beloen)


def sub_main0_aren_func(update,context):
    query = update.callback_query
    query.edit_message_caption(ar_message, reply_markup=sub_main0_aren)

def sub_main0_uzen_func(update,context):
    query = update.callback_query
    query.edit_message_caption(uz_message, reply_markup=sub_main0_uzen)

def sub_main0_turen_func(update,context):
    query = update.callback_query
    query.edit_message_caption(tur_message, reply_markup=sub_main0_turen)

def sub_main0_azeren_func(update,context):
    query = update.callback_query
    query.edit_message_caption(azer_message, reply_markup=sub_main0_azeren)

def sub_main0_tdjen_func(update,context):
    query = update.callback_query
    query.edit_message_caption(tdj_message, reply_markup=sub_main0_tdjen)

def sub_main0_molen_func(update,context):
    query = update.callback_query
    query.edit_message_caption(mol_message, reply_markup=sub_main0_molen)

def sub_main0_kiren_func(update,context):
    query = update.callback_query
    query.edit_message_caption(kir_message, reply_markup=sub_main0_kiren)



def sub_main1en_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main1en)

def sub_main3en_func(update,context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main3en)

def sub_main4en_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main4en)


def sub_main5en_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main5en)

def sub_main7en_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main7en)

def sub_main8en_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main8en)

def sub_main6en_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main6en)


def sub_main9en_func(update, context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main9en)

def sub_main_10en_func(update,context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main_10en)

def sub_main_11en_func(update,context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main_11en)

def sub_main_12en_func(update,context):
    query = update.callback_query
    query.edit_message_caption(weed_message, reply_markup=sub_main_12en)


def backen_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(ua_picture, 'rb'), caption=ua_message,
                          reply_markup=main_keyboard, supports_streaming=True)
    #query.edit_message_caption(welcome_message, reply_markup=main_keyboard)

def back_rusen_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(rus_picture, 'rb'), caption=rus_message,
                          reply_markup=main_keyboard1, supports_streaming=True)

def back_kazaen_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(kaza_picture, 'rb'), caption=kaza_message,
                          reply_markup=main_keyboard_kaza, supports_streaming=True)


def back_beloen_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(belo_picture, 'rb'), caption=belo_message,
                          reply_markup=main_keyboard_belo, supports_streaming=True)


def back_aren_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(ar_picture, 'rb'), caption=ar_message,
                          reply_markup=main_keyboard_ar, supports_streaming=True)

def back_uzen_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(uz_picture, 'rb'), caption=uz_message,
                          reply_markup=main_keyboard_uz, supports_streaming=True)

def back_turen_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(tur_picture, 'rb'), caption=tur_message,
                          reply_markup=main_keyboard_tur, supports_streaming=True)

def back_azeren_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(azer_picture, 'rb'), caption=azer_message,
                          reply_markup=main_keyboard_azer, supports_streaming=True)

def back_tdjen_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(tdj_picture, 'rb'), caption=tdj_message,
                          reply_markup=main_keyboard_tdj, supports_streaming=True)

def back_molen_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(mol_picture, 'rb'), caption=mol_message,
                          reply_markup=main_keyboard_mol, supports_streaming=True)

def back_kiren_func(update, context):
    #query = update.callback_query
    context.bot.sendPhoto(chat_id=update.effective_user.id, photo=open(kir_picture, 'rb'), caption=kir_message,
                          reply_markup=main_keyboard_kir, supports_streaming=True)



def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
#########################################################################################################################################
def main():
    updater = Updater(bot_token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(sub_main3_func, pattern='sub_main3'))
    dp.add_handler(CallbackQueryHandler(sub_main1_func, pattern='sub_main1'))
    dp.add_handler(CallbackQueryHandler(sub_main4_func, pattern='sub_main4'))
    dp.add_handler(CallbackQueryHandler(sub_main5_func, pattern='sub_main5'))
    dp.add_handler(CallbackQueryHandler(sub_main6_func, pattern='sub_main6'))
    dp.add_handler(CallbackQueryHandler(sub_main7_func, pattern='sub_main7'))
    dp.add_handler(CallbackQueryHandler(sub_main8_func, pattern='sub_main8'))
    dp.add_handler(CallbackQueryHandler(sub_main9_func, pattern='sub_main9'))
    dp.add_handler(CallbackQueryHandler(sub_main_10_func, pattern='sub_main_10'))
    dp.add_handler(CallbackQueryHandler(sub_main_11_func, pattern='sub_main_11'))
    dp.add_handler(CallbackQueryHandler(sub_main_12_func, pattern='sub_main_12'))
    dp.add_handler(CallbackQueryHandler(sub_main0_rus_func, pattern='sub_main0_rus'))
    dp.add_handler(CallbackQueryHandler(sub_main0_kaza_func, pattern='sub_main0_kaza'))
    dp.add_handler(CallbackQueryHandler(sub_main0_belo_func, pattern='sub_main0_belo'))
    dp.add_handler(CallbackQueryHandler(sub_main0_ar_func, pattern='sub_main0_ar'))
    dp.add_handler(CallbackQueryHandler(sub_main0_uz_func, pattern='sub_main0_uz'))
    dp.add_handler(CallbackQueryHandler(sub_main0_tur_func, pattern='sub_main0_tur'))
    dp.add_handler(CallbackQueryHandler(sub_main0_azer_func, pattern='sub_main0_azer'))
    dp.add_handler(CallbackQueryHandler(sub_main0_tdj_func, pattern='sub_main0_tdj'))
    dp.add_handler(CallbackQueryHandler(sub_main0_mol_func, pattern='sub_main0_mol'))
    dp.add_handler(CallbackQueryHandler(sub_main0_kir_func, pattern='sub_main0_kir'))

    dp.add_handler(CallbackQueryHandler(sub_main0_func, pattern='sub_main0'))
    dp.add_handler(CallbackQueryHandler(back_rus_func, pattern='main_rus'))
    dp.add_handler(CallbackQueryHandler(back_kaza_func, pattern='main_kaza'))
    dp.add_handler(CallbackQueryHandler(back_belo_func, pattern='main_belo'))
    dp.add_handler(CallbackQueryHandler(back_ar_func, pattern='main_ar'))
    dp.add_handler(CallbackQueryHandler(back_uz_func, pattern='main_uz'))
    dp.add_handler(CallbackQueryHandler(back_tur_func, pattern='main_tur'))
    dp.add_handler(CallbackQueryHandler(back_azer_func, pattern='main_azer'))
    dp.add_handler(CallbackQueryHandler(back_tdj_func, pattern='main_tdj'))
    dp.add_handler(CallbackQueryHandler(back_mol_func, pattern='main_mol'))
    dp.add_handler(CallbackQueryHandler(back_kir_func, pattern='main_kir'))
    #dp.add_handler(CallbackQueryHandler(back_func, pattern='main'))
    dp.add_handler(CallbackQueryHandler(main_main_func, pattern='main_main'))
    dp.add_handler(CallbackQueryHandler(main_ua_func, pattern='main_ua'))
    dp.add_handler(CallbackQueryHandler(back_func, pattern='back'))
    dp.add_handler(CallbackQueryHandler(back_kaza_func, pattern='back_kaza'))
    dp.add_handler(CallbackQueryHandler(back_belo_func, pattern='back_belo'))
    dp.add_handler(CallbackQueryHandler(back_ar_func, pattern='back_ar'))
    dp.add_handler(CallbackQueryHandler(back_uz_func, pattern='back_uz'))
    dp.add_handler(CallbackQueryHandler(back_tur_func, pattern='back_tur'))
    dp.add_handler(CallbackQueryHandler(back_azer_func, pattern='back_azer'))
    dp.add_handler(CallbackQueryHandler(back_tdj_func, pattern='back_tdj'))
    dp.add_handler(CallbackQueryHandler(back_mol_func, pattern='back_mol'))
    dp.add_handler(CallbackQueryHandler(back_kir_func, pattern='back_kir'))

    dp.add_handler(CallbackQueryHandler(sub_main3en_func, pattern='sub_main3en'))
    dp.add_handler(CallbackQueryHandler(sub_main1en_func, pattern='sub_main1en'))
    dp.add_handler(CallbackQueryHandler(sub_main4en_func, pattern='sub_main4en'))
    dp.add_handler(CallbackQueryHandler(sub_main5en_func, pattern='sub_main5en'))
    dp.add_handler(CallbackQueryHandler(sub_main6en_func, pattern='sub_main6en'))
    dp.add_handler(CallbackQueryHandler(sub_main7en_func, pattern='sub_main7en'))
    dp.add_handler(CallbackQueryHandler(sub_main8en_func, pattern='sub_main8en'))
    dp.add_handler(CallbackQueryHandler(sub_main9en_func, pattern='sub_main9en'))
    dp.add_handler(CallbackQueryHandler(sub_main_10en_func, pattern='sub_main_10en'))
    dp.add_handler(CallbackQueryHandler(sub_main_11en_func, pattern='sub_main_11en'))
    dp.add_handler(CallbackQueryHandler(sub_main_12en_func, pattern='sub_main_12en'))
    dp.add_handler(CallbackQueryHandler(sub_main0_rusen_func, pattern='sub_main0_rusen'))
    dp.add_handler(CallbackQueryHandler(sub_main0_kazaen_func, pattern='sub_main0_kazaen'))
    dp.add_handler(CallbackQueryHandler(sub_main0_beloen_func, pattern='sub_main0_beloen'))
    dp.add_handler(CallbackQueryHandler(sub_main0_aren_func, pattern='sub_main0_aren'))
    dp.add_handler(CallbackQueryHandler(sub_main0_uzen_func, pattern='sub_main0_uzen'))
    dp.add_handler(CallbackQueryHandler(sub_main0_turen_func, pattern='sub_main0_turen'))
    dp.add_handler(CallbackQueryHandler(sub_main0_azeren_func, pattern='sub_main0_azeren'))
    dp.add_handler(CallbackQueryHandler(sub_main0_tdjen_func, pattern='sub_main0_tdjen'))
    dp.add_handler(CallbackQueryHandler(sub_main0_molen_func, pattern='sub_main0_molen'))
    dp.add_handler(CallbackQueryHandler(sub_main0_kiren_func, pattern='sub_main0_kiren'))

    dp.add_handler(CallbackQueryHandler(sub_main0en_func, pattern='sub_main0en'))
    dp.add_handler(CallbackQueryHandler(back_rusen_func, pattern='main_rusen'))
    dp.add_handler(CallbackQueryHandler(back_kazaen_func, pattern='main_kazaen'))
    dp.add_handler(CallbackQueryHandler(back_beloen_func, pattern='main_beloen'))
    dp.add_handler(CallbackQueryHandler(back_aren_func, pattern='main_aren'))
    dp.add_handler(CallbackQueryHandler(back_uzen_func, pattern='main_uzen'))
    dp.add_handler(CallbackQueryHandler(back_turen_func, pattern='main_turen'))
    dp.add_handler(CallbackQueryHandler(back_azeren_func, pattern='main_azeren'))
    dp.add_handler(CallbackQueryHandler(back_tdjen_func, pattern='main_tdjen'))
    dp.add_handler(CallbackQueryHandler(back_molen_func, pattern='main_molen'))
    dp.add_handler(CallbackQueryHandler(back_kiren_func, pattern='main_kiren'))
    #dp.add_handler(CallbackQueryHandler(backen_func, pattern='mainen'))
    dp.add_handler(CallbackQueryHandler(main_en_func, pattern='main_en'))
    dp.add_handler(CallbackQueryHandler(main_uaen_func, pattern='main_uaen'))
    dp.add_handler(CallbackQueryHandler(backen_func, pattern='backen'))
    dp.add_handler(CallbackQueryHandler(back_kazaen_func, pattern='back_kazaen'))
    dp.add_handler(CallbackQueryHandler(back_beloen_func, pattern='back_beloen'))
    dp.add_handler(CallbackQueryHandler(back_aren_func, pattern='back_aren'))
    dp.add_handler(CallbackQueryHandler(back_uzen_func, pattern='back_uzen'))
    dp.add_handler(CallbackQueryHandler(back_turen_func, pattern='back_turen'))
    dp.add_handler(CallbackQueryHandler(back_azeren_func, pattern='back_azeren'))
    dp.add_handler(CallbackQueryHandler(back_tdjen_func, pattern='back_tdjen'))
    dp.add_handler(CallbackQueryHandler(back_molen_func, pattern='back_molen'))
    dp.add_handler(CallbackQueryHandler(back_kiren_func, pattern='back_kiren'))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
