def month(number_of_the_month: int, lang="ru") -> str:
    """Имя of the month 2.0"""
    BOTH_MONTHS = {
        'ru': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
               'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
    }
    # print(both_months[lang][number_of_the_month])
    return BOTH_MONTHS[lang][number_of_the_month - 1]


print(month(2))
