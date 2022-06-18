

# Метод кодування тексту
def encoding(plaintext):
    # Створюємо словник "ключ-значення", де ключ - символ, значення - кількість таких символів у тексті
    chars_number = {}
    # Цикл, який перевіряє кожен символ тексту
    for i in range(len(plaintext)):
        # Якщо символу немає в словнику
        if chars_number.get(plaintext[i]) is None:
            # Додаємо символ в словник
            chars_number[plaintext[i]] = 1
        # В іншому випадку
        else:
            # Збільшуємо кількість символу на 1
            chars_number[plaintext[i]] += 1
    # Створюємо словник "ключ-значення", де ключ - символ, значення - частота появи символу в тексті
    chars_freq = chars_number.copy()
    # Для кожного символа
    for key in chars_freq.keys():
        # Встановлюємо округлене значення частоти появи символу в тексті
        chars_freq[key] = round(chars_freq.get(key) / len(plaintext), 4)
    # Сортуємо словник по зростанню частоти появи символу в тексті
    sorted_keys = sorted(chars_freq, key=chars_freq.get)
    # Створюємо пустий словник
    sorted_chars = {}
    # Для кожного ключа
    for key in sorted_keys:
        # Заносимо значення по ключу
        sorted_chars[key] = chars_freq[key]
    # Розвертаємо словник, тепер він відсортований по спаданню частоти появи символу в тексті
    chars_freq = {k: v for k, v in reversed(list(sorted_chars.items()))}
    # Створюємо словник "ключ-значення", де ключ - символ, значення - код цього символу
    chars_code = {}
    # Для кожного ключа
    for key in chars_freq.keys():
        # Заносимо в новий словник кожен ключ зі значенням пустого рядка
        chars_code[key] = ''
    # Створюємо список словників, до якого відразу заносимо словник із символами та їх частотою появи в тексті
    list_dicts = [chars_freq]
    # Доки кількість словників у списку не буде дорівнювати кількості символів
    while len(list_dicts) != len(chars_number):
        # Для кожного словника
        for d in list_dicts:
            # Якщо словник не порожній
            if len(d) != 0:
                # Сума всіх значень частоти появи символів словника
                dict_summ = sum(d.values())
                # Створюємо порожній допоміжний словник
                chars_dict = {}
                # Якщо в словнику більше, ніж 1 символ
                if len(d) > 1:
                    # Створюємо лічильник суми
                    summ = 0
                    # Для кожного ключа
                    for key in d.copy():
                        # Якщо лічильник більше або дорівнює сумі всіх значень словника, розділеної на 2
                        if summ >= dict_summ / 2:
                            # Дописуємо до відповідного символа '1'
                            chars_code[key] += '1'
                        # В іншому випадку
                        else:
                            # Дописуємо до відповідного символа '0'
                            chars_code[key] += '0'
                            # Додаємо до лічильника значення ключа
                            summ += d.get(key)
                            # Записуємо значення ключа в допоміжний словник
                            chars_dict[key] = d.get(key)
                            # Видаляємо ключ і його значення зі словника
                            del d[key]
                # Якщо допоміжний словник не порожній
                if len(chars_dict) != 0:
                    # Додаємо допоміжний словник до списку словників
                    list_dicts.append(chars_dict)
    # Створюємо пустий рядок шифротексту
    ciphertext = ''
    # Для кожного символу в тексті
    for char in plaintext:
        # Додаємо закодований символ до шифротексту
        ciphertext += chars_code[char]
    # Повертаємо шифротекст, а також словник "ключ-значення", де ключ - символ, значення - код символу
    return ciphertext, chars_code


# Метод декодування шифротексту
def decoding(ciphertext, chars_code):
    # Створюємо пустий рядок тексту
    plaintext = ''
    # Створюємо лічильник
    count = 1
    # Доки рядок шифротексту не буде пустим
    while len(ciphertext) != 0:
        # Створюємо змінну с і записуємо в неї кількість символів з початку шифротексту рівну лічильнику count
        c = ciphertext[:count]
        # Для кожного ключа
        for key in chars_code:
            # Якщо значення змінної збігається зі значенням ключа (коду символа)
            if c == chars_code.get(key):
                # Дописуємо в текст ключ (символ)
                plaintext += key
                # Видаляємо з рядку шифротексту те, що дописали
                ciphertext = ciphertext[count:]
                # Скидаємо лічильник до 0
                count = 0
                # Виходимо з циклу
                break
        # Збільшуємо лічильник на 1
        count += 1
    # Повертаємо текст
    return plaintext


print('Введіть текст:')
text = input()
encoded_text = encoding(text)[0]
print(f'Зашифрований текст: {encoded_text}')
encoded_chars = encoding(text)[1]
decoded_text = decoding(encoded_text, encoded_chars)
print(f'Розшифрований текст: {decoded_text}')
