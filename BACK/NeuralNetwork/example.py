from text_analyser import TextAnalyser

analyser = TextAnalyser()

line1 = 'Сегодня самый счастливый день в моей жизни! Я наконец-то добился того, к чему так долго шёл! Я не могу поверить, что это происходит со мной! '
line2 = 'Я так рад! Маму в рот ебал, потому что я крутой. '
line3 = 'Птицы порхали с ветки на ветку, радуя меня своим щебетом. Бабочки с разноцветными крыльями порхали над цветами. Пчелы собирали нектар, жужжа своим мелодичным гулом. '
line4 = 'Я босиком ступил на мягкую траву, чувствуя под ногами прохладу и свежесть. Я закрыл глаза и глубоко вдохнул. '
line5 = 'В этот момент я почувствовал единение с природой, и все мои заботы и тревоги мгновенно растворились. '
line6 = 'Я долго гулял по лесу, наслаждаясь чистым воздухом и пением птиц. Я фотографировал красивые цветы и бабочек, чтобы сохранить эти чудесные мгновения в своей памяти.'

result = analyser.summary(line1 + line2 + line3 + line4 + line5 + line6)

# Первым идет стандартный вывод по предложениям
sentence_result = result[0]

#Далее - список предложений с анализом
for sample in sentence_result:
    # Первый элемент - текст
    text = sample[0]
    print(text)
    # Второй - предсказание
    prediction = sample[1]
    print(prediction)
    # С третьего по восьмой - вероятности
    print('Neutral: ', sample[2], '%')
    print('Joy: ', sample[3], '%')
    print('Sadness: ', sample[4], '%')
    print('Surprise: ', sample[5], '%')
    print('Fear: ', sample[6], '%')
    print('Anger: ', sample[7], '%')
    # Девятый - флаг о наличии мата в тексте
    if sample[8]:
        print('Profanity detected!\n')
    else:
        print('\n')

# Вторым идет анализ всего текста
total_result = result[1]

print('Total: ')
# Первый элемент - предсказание
prediction = total_result[0]
# Со второго по седьмой - вероятности
print('Neutral: ', total_result[1], '%')
print('Joy: ', total_result[2], '%')
print('Sadness: ', total_result[3], '%')
print('Surprise: ', total_result[4], '%')
print('Fear: ', total_result[5], '%')
print('Anger: ', total_result[6], '%\n')

# Третьим - анализ стиля текста
style_result = result[2]
print('\nStyle analys: ')
# Первый элемент - предсказание
prediction = style_result[0]
# Со второго по шестой - вероятности
print('Artistic: ', style_result[1], '%')
print('Publicistic: ', style_result[2], '%')
print('Scientific: ', style_result[3], '%')
print('Conversational: ', style_result[4], '%')
print('Official: ', style_result[5], '%')