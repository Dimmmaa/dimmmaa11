import telebot

#cities
city_list = ["♦️ Москва","♦️ Санкт-Петербург","♦️ Тула","♦️ Екатеринбрг","♦️ Барнаул","♦️ Томск","♦️ Тюмень","♦️ Нижний Новгород","♦️ Самара","♦️ Омск","♦️ Саратов","♦️ Краснодар","♦️ Воронеж", "♦️ Екатеринбург"]
rayon_list = ["♦️ САО","♦️ ЦАО","♦️ ЮАО","♦️ ЮВАО","♦️ ЗАО","♦️ Василеостровский","♦️ Выборгский","♦️ Калининский","♦️ Кировский","♦️ Колпинский","♦️ Красногвардейский","♦️ Красносельский","♦️ Курортный","♦️ Кронштадтский","♦️ Московский","♦️ Невский","♦️ Петроградский","♦️ Петродворцовый","♦️ Приморский","♦️ Пушкинский","♦️ Фрунзенский","♦️ Центральный",
              "♦️ Зареченский","♦️ Привокзальный","♦️ Пролетарский","♦️ Советский","♦️ Центральный","♦️ Верх-Исетский","♦️ Железнодорожный","♦️ Кировский","♦️ Октябрьский","♦️ Ордожиникидзевский","♦️ Чкаловский", "♦️ Железнодорожный","♦️ Индустриальный","♦️ Ленинский","♦️ Октябрьский","♦️ Кировский","♦️ Ленинский","♦️ Октрябрьский","♦️ Советский",
              "♦️ Восточный","♦️ Ленинский", "♦️ Автозаводский","♦️ Канавинский","♦️ Нижегородский","♦️ Приокский", "♦️ Сормовский", "♦️ Куйбышевский ","♦️ Самарский","♦️ Промышленный","♦️ Красноглинский", "♦️ Заводской район","♦️ Фрунзенский","♦️ Волжский", "♦️ ЖМР","♦️ СМР","♦️ ЗИП","♦️ РИП","♦️ ШМР","♦️ ЮМР","♦️ КМР","♦️ ПМР","♦️ ГМР","♦️ ЧМР",
              "♦️ Железнодорожный","♦️ Коминтерновский","♦️ Левобережный","♦️ Авиастроительный","♦️ Вахитовский","♦️ Ново-Савиновский","♦️ Приволжский","♦️ Дзержинский","♦️ Мотовилихинский","♦️ Орджоникидзевский","♦️ Свердловский","♦️ Дзержинский","♦️ Заельцовский","♦️ Первомайский","♦️ Курчатовский","♦️ Металлургический","♦️ Тракторозаводской"
             ]
tovar_list = {"♦️ Гашиш (1г)-700p" : "700","♦️ Гашиш (5г)-3300p" : "3300","♦️ Гашиш (10г)-5900p" : "5900","♦️ Шишки (1г)-1100p" : "1100","♦️ Шишки (2г)-2000p" : "2000",
"♦️ Шишки (5г)-3500p" : "3500","♦️ Шишки (10г)-6500p" : "6500","♦️ Амфетамин (1гр)-800p": "800","♦️ Амфетамин (3гр)-2100p" : "2100","♦️ Амфетамин (5гр)-3000p" : "3000",
"♦️ Амфетамин (10гр)-5500p" : "5500","♦️ Амфетамин (25гр)-10000p" : "10000","♦️ Мефедрон (1гр)-1300p" : "1300p","♦️ Медерон (3гр)-3700p" : "3700",
"♦️ МДМА (1гр)-2800p" : "2800","♦️ МДМА (2гр)-5600p" : "5600","♦️ МДМА (5гр)-11600p" : "11600","♦️ Кокаин MQ (1гр)-4000p" : "4000","♦️ Кокаин HQ (0,3гр)-2500p" : "2500",
"♦️ Кокаин HQ (1гр)-7500p" : "7500","♦️ Кокаин HQ (0,5гр)-4250p" : "4250","♦️ Кокаин HQ (1,5гр)-11400p" : "11400","♦️ Кокаин MQ (2гр)-8650p" : "8650",
"♦️ LSD(180мкг) (5шт)-3500p" : "3500","♦️ LSD(180мкг) (10шт)-7700p" : "7700","♦️ Метамфетамин HQ(Крис) (1гр) -3400p" : "3400"}

all_list = ["📢 Информация", "❓ Помощь", "Перейти к выбору товара", "Вернутся к выбору города", "✅Я оплатил товар!", "♦️ Москва","♦️ Санкт-Петербург","♦️ Тула","♦️ Екатеринбург","♦️ Барнаул","♦️ Томск","♦️ Тюмень","♦️ Нижний Новгород","♦️ Самара","♦️ Омск","♦️ Саратов","♦️ Краснодар","♦️ Воронеж", "♦️ САО","♦️ ЦАО","♦️ ЮАО","♦️ ЮВАО","♦️ ЗАО","♦️ Василеостровский","♦️ Выборгский","♦️ Калининский","♦️ Кировский","♦️ Колпинский","♦️ Красногвардейский","♦️ Красносельский","♦️ Курортный","♦️ Кронштадтский","♦️ Московский","♦️ Невский","♦️ Петроградский","♦️ Петродворцовый","♦️ Приморский","♦️ Пушкинский","♦️ Фрунзенский","♦️ Центральный",
              "♦️ Зареченский","♦️ Привокзальный","♦️ Пролетарский","♦️ Советский","♦️ Центральный","♦️ Верх-Исетский","♦️ Железнодорожный","♦️ Кировский","♦️ Октябрьский","♦️ Ордожиникидзевский","♦️ Чкаловский", "♦️ Железнодорожный","♦️ Индустриальный","♦️ Ленинский","♦️ Октябрьский","♦️ Кировский","♦️ Ленинский","♦️ Октрябрьский","♦️ Советский",
              "♦️ Восточный","♦️ Ленинский", "♦️ Автозаводский","♦️ Канавинский","♦️ Нижегородский","♦️ Приокский", "♦️ Сормовский", "♦️ Куйбышевский ","♦️ Самарский","♦️ Промышленный","♦️ Красноглинский", "♦️ Заводской район","♦️ Фрунзенский","♦️ Волжский", "♦️ ЖМР","♦️ СМР","♦️ ЗИП","♦️ РИП","♦️ ШМР","♦️ ЮМР","♦️ КМР","♦️ ПМР","♦️ ГМР","♦️ ЧМР",
              "♦️ Железнодорожный","♦️ Коминтерновский","♦️ Левобережный","♦️ Авиастроительный","♦️ Вахитовский","♦️ Ново-Савиновский","♦️ Приволжский","♦️ Дзержинский","♦️ Мотовилихинский","♦️ Орджоникидзевский","♦️ Свердловский","♦️ Дзержинский","♦️ Заельцовский","♦️ Первомайский","♦️ Курчатовский","♦️ Металлургический","♦️ Тракторозаводской",
              "♦️ Гашиш (1г)-700p","♦️ Гашиш (5г)-3300p","♦️ Гашиш (10г)-5900p","♦️ Шишки (1г)-1100p","♦️ Шишки (2г)-2000p",
              "♦️ Шишки (5г)-3500p","♦️ Шишки (10г)-6500p","♦️ Амфетамин (1гр)-800p","♦️ Амфетамин (3гр)-2100p","♦️ Амфетамин (5гр)-3000p",
              "♦️ Амфетамин (10гр)-5500p","♦️ Амфетамин (25гр)-10000p","♦️ Мефедрон (1гр)-1300p","♦️ Медерон (3гр)-3700p",
              "♦️ МДМА (1гр)-2800p","♦️ МДМА (2гр)-5600p","♦️ МДМА (5гр)-11600p","♦️ Кокаин MQ (1гр)-4000p","♦️ Кокаин HQ (0,3гр)-2500p",
              "♦️ Кокаин HQ (1гр)-7500p","♦️ Кокаин HQ (0,5гр)-4250p","♦️ Кокаин HQ (1,5гр)-11400p","♦️ Кокаин MQ (2гр)-8650p",
              "♦️ LSD(180мкг) (5шт)-3500p","♦️ LSD(180мкг) (10шт)-7700p","♦️ Метамфетамин HQ(Крис) (1гр) -3400p"
               ]

cities_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
cities_menu.row("♦️ Москва",)
cities_menu.row("♦️ Санкт-Петербург",)
cities_menu.row("♦️ Тула",)
cities_menu.row("♦️ Екатеринбург",)
cities_menu.row("♦️ Барнаул",)
cities_menu.row("♦️ Томск",)
cities_menu.row("♦️ Тюмень",)
cities_menu.row("♦️ Нижний Новгород",)
cities_menu.row("♦️ Самара",)
cities_menu.row("♦️ Омск",)
cities_menu.row("♦️ Саратов",)
cities_menu.row("♦️ Краснодар",)
cities_menu.row("♦️ Воронеж",)
cities_menu.row("♦️ Казань",)
cities_menu.row("♦️ Пермь")
cities_menu.row("♦️ Новосибирск")
cities_menu.row("♦️ Челябинск")
#Drugs
drugs_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
drugs_menu.add(
"♦️ Гашиш (1г)-700p",
"♦️ Гашиш (5г)-3300p",
"♦️ Гашиш (10г)-5900p",
"♦️ Шишки (1г)-1100p",
"♦️ Шишки (2г)-2000p",
"♦️ Шишки (5г)-3500p",
"♦️ Шишки (10г)-6500p",
"♦️ Амфетамин (1гр)-800p",
"♦️ Амфетамин (3гр)-2100p",
"♦️ Амфетамин (5гр)-3000p",
"♦️ Амфетамин (10гр)-5500p",
"♦️ Амфетамин (25гр)-10000p",
"♦️ Мефедрон (1гр)-1300p",
"♦️ Медерон 3гр(-3700p",
"♦️ МДМА (1гр)-2800p",
"♦️ МДМА (2гр)-5600p",
"♦️ МДМА (5гр)-11600p",
"♦️ Кокаин MQ (1гр)-4000p",
"♦️ Кокаин HQ (0,3гр)-2500p",
"♦️ Кокаин HQ (1гр)-7500p",
"♦️ Кокаин HQ (0,5гр)-4250p",
"♦️ Кокаин HQ (1,5гр)-11400p",
"♦️ Кокаин MQ (2гр)-8650p",
"♦️ LSD(180мкг) (5шт)-3500p",
"♦️ LSD(180мкг) (10шт)-7700p",
"♦️ Метамфетамин HQ(Крис) (1гр) -3400p"
) 

#Help
help_menu = telebot.types.ReplyKeyboardMarkup(True, True, True)
help_menu.row("📢 Информация", "❓ Помощь")
help_menu.row("Перейти к выбору товара")
help_menu.row("Вернутся к выбору города")


#Buy Menu
buy_menu = telebot.types.ReplyKeyboardMarkup(True, True, True)
buy_menu.row("✅Я оплатил товар!")
#города

#moscow
moscow_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
moscow_menu.add(
"♦️ САО",
"♦️ ЦАО",
"♦️ ЮАО",
"♦️ ЮВАО",
"♦️ ЗАО",
)
#SPB
spb_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
spb_menu.add(
"♦️ Василеостровский",
"♦️ Выборгский",
"♦️ Калининский",
"♦️ Кировский",
"♦️ Колпинский",
"♦️ Красногвардейский",
"♦️ Красносельский",
"♦️ Курортный",
"♦️ Кронштадтский",
"♦️ Московский",
"♦️ Невский",
"♦️ Петроградский",
"♦️ Петродворцовый",
"♦️ Приморский",
"♦️ Пушкинский",
"♦️ Фрунзенский",
"♦️ Центральный"
)
#Тула
tula_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
tula_menu.add(
"♦️ Зареченский",
"♦️ Привокзальный",
"♦️ Пролетарский",
"♦️ Советский",
"♦️ Центральный"
)
#Екатеринбург
ekb_menu= telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
ekb_menu.add(
"♦️ Верх-Исетский",
"♦️ Железнодорожный",
"♦️ Кировский",
"♦️ Октябрьский",
"♦️ Ордожиникидзевский",
"♦️ Чкаловский"
)
#Барнаул
barnaul_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
barnaul_menu.add(
"♦️ Железнодорожный",
"♦️ Индустриальный",
"♦️ Ленинский",
"♦️ Октябрьский",
"♦️ Центральный"
)
#Томск
tomsk_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
tomsk_menu.add(
"♦️ Кировский",
"♦️ Ленинский",
"♦️ Октрябрьский",
"♦️ Советский"
)
#Тюмень
tumen_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
tumen_menu.add(
"♦️ Восточный",
"♦️ Калининский",
"♦️ Ленинский",
"♦️ Центральный"
)
#Нижний Новгород
nn_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
nn_menu.add(
"♦️ Автозаводский",
"♦️ Канавинский",
"♦️ Ленинский",
"♦️ Московский",
"♦️ Нижегородский",
"♦️ Приокский",
"♦️ Советский",
"♦️ Сормовский"
)
# Самара
samara_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
samara_menu.add(
"♦️ Куйбышевский ",
"♦️ Самарский",
"♦️ Ленинский",
"♦️ Железнодорожный",
"♦️ Октябрьский",
"♦️ Промышленный",
"♦️ Кировский",
"♦️ Красноглинский"
)
#Омск
omsk_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
omsk_menu.add(
"♦️ Советский",
"♦️ Центральный",
"♦️ Кировский",
"♦️ Октябрьский",
"♦️ Ленинский"
)

#Саратов
saratov_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
saratov_menu.add(
"♦️ Заводской район",
"♦️ Октрябрьский",
"♦️ Фрунзенский",
"♦️ Волжский",
"♦️ Ленинский",
"♦️ Кировский"
)
#Краснодар
krasnodar_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
krasnodar_menu.add(
"♦️ ЖМР",
"♦️ СМР",
"♦️ ЗИП",
"♦️ РИП",
"♦️ Центральный",
"♦️ ШМР",
"♦️ ЮМР",
"♦️ КМР",
"♦️ ПМР",
"♦️ ГМР",
"♦️ ЧМР"
)

#Воронеж
voronej_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
voronej_menu.add(
"♦️ Железнодорожный",
"♦️ Коминтерновский",
"♦️ Левобережный",
"♦️ Ленинский",
"♦️ Советский",
"♦️ Центральный"
)
#Казань
kasan_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
kasan_menu.add(
"♦️ Авиастроительный",
"♦️ Вахитовский",
"♦️ Кировский",
"♦️ Московский",
"♦️ Ново-Савиновский",
"♦️ Приволжский",
"♦️ Советский"
)
#Пермь
perm_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
perm_menu.add(
"♦️ Дзержинский",
"♦️ Индустриальный",
"♦️ Кировский",
"♦️ Ленинский",
"♦️ Мотовилихинский",
"♦️ Орджоникидзевский",
"♦️ Свердловский"
)
#Новосибирск
ns_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
ns_menu.add(
"♦️ Дзержинский",
"♦️ Железнодорожный",
"♦️ Заельцовский",
"♦️ Калининский",
"♦️ Кировский",
"♦️ Ленинский",
"♦️ Октябрьский",
"♦️ Первомайский",
"♦️ Советский",
"♦️ Центральный"
)
#Челябинск
chel_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
chel_menu.add(
"♦️ Калининский",
"♦️ Курчатовский",
"♦️ Ленинский",
"♦️ Металлургический",
"♦️ Советский",
"♦️ Тракторозаводской",
"♦️ Центральный"
)
