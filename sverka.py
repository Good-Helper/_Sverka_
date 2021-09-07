#!/usr/bin/python
import bd
import datetime


# Задаем переменную для Даты и Времени
_time = datetime.datetime.now()


# Добавляем текстовый фаил учета и зачитываем его!
bd.baza()
print('*'*15, 'Подключен SQLite', '*'*15)


def convert():
    # Делаем подсказку по сумме в кассе на прошлый день
    hint = '▶ Вчера вечером в кассе было: '
    # print('ˍ' * len(podskazka))
    print(hint)


# формирование отчета
    def int_input():
        error = '\n !!!_Программа обробатывает только целые числа_!!!'
        error = error + "\n" + '▴' * len(error)

        try:
            money_in_the_morning = int(input('\n↦ Касса утром: '))
        except ValueError:
            print(error)
            return int_input()

        try:
            proceeds = int(input('↦ Выручка: '))
        except ValueError:
            print(error)
            return int_input()

        try:
            cashless = int(input('↦ Безнал: '))
        except ValueError:
            print(error)
            return int_input()

        cash_1 = proceeds - cashless

        try:
            print( '↦ Наличными: ', cash_1 )
        except ValueError:
            print( error )
            return int_input()

        try:
            collection = int( input( '↦ Инкассации: ' ) )
        except ValueError:
            print( error )
            return int_input()

        try:
            costs = int( input( '↦ Доп. расходы: ' ) )
        except ValueError:
            print( error )
            return int_input()

        try:
            fact = int( input( '↦ Факт: ' ) )
        except ValueError:
            print( error )
            return int_input()

        # высчитываем наличку
        cash_2 = proceeds - cashless - collection - costs

        # формируем кассу
        kassa = money_in_the_morning + cash_2
        print( '' )

        # Проверка по кассе
        def check(fact, kassa):
            if fact == kassa:
                print( 'В кассе: ' + str( kassa ) + "₽\nКасса ровная! シ " )

            elif fact > kassa:
                print( "В кассе", str( fact ) + "₽",
                       "\nДолжно быть " + str( kassa ) + "₽\nСумма больше на",
                       str( fact - kassa ) + "₽" )

            else:
                print( "В кассе", str( fact ) + "₽"
                                                '\nДолжно быть ' + str( kassa ) + "₽.\nНе хватает",
                       str( kassa - fact ) + "₽" )


        # условия премирования
        priz = 9000
        difference = priz - proceeds

        # инфо о премии
        def premiya(summ_prem, proceeds):
            if proceeds >= summ_prem:
                print( '🏆 ПРЕМИЯ 🥇:\nУраа... Вам положена премия 500₽ за хорошую работу!🎊🎉🎈\n' )

            elif proceeds >= summ_prem - 1000:
                print( 'ПРЕМИЯ 🥈:\n🚖🚖Вам положенно Такси в обе стороны!\n🤬До джекпота не хватило',
                       str( difference ) + ' ₽ 😭\n' )

            elif proceeds >= summ_prem - 2000:
                print( 'ПРЕМИЯ 🥉:\n🚖Вам положенно Такси в одну сторону!\n' )



        # вызов функций
        check( fact, kassa )
        print()
        premiya( priz, proceeds )


        while True:
            flag = input( 'Записать данные? [да/нет]: ' )

            if flag == 'да' or flag == 'y' or flag == '1':
                user = str(input('Введите Ваше имя...'))
                date = datetime.datetime.now()
                bd.record(date, user, money_in_the_morning, proceeds, cashless, cash_1, collection, costs, fact)
                break

            else:
                break

    int_input()


convert()


while True:
    flag = input( 'Посчитать еще раз? [да/нет]: ' )
    if flag == 'да' or flag == 'y' or flag == '1':
        convert()
    else:
        print( '                     ː₨ː v.2.0.1' )
        break
