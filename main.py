size, alphabet = 0, ''
# заменяю стандартную функцию ord, т.к. в ней в русском алфавите
# за буквой Е следует буква Ж (а не Ё)
def ORD(c):
    return alphabet.index(c)


def main():
    print('Добро пожаловать в программу шифрования методом Виженера!')
    while True:  # программа работает пока пользователь не нажмет кнопку выход (что вы хотите сделать -> 3)
        what_to_do = input('Что вы хотите сделать:\n'
                           '1) Зашифровать текст\n'
                           '2) Расшифровать текст\n'
                           '3) Выход\n')
        if what_to_do == '3':
            return 0
        lang = input('Выберите язык текста:\n1) Русский\n2) Английский\n')
        text = input('Введите текст:\n\n')
        if lang == '2':
            al = 'abcdefghijklmnopqrstuvwxyz'
        else:
            al = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        global size, alphabet
        size, alphabet = len(al), al

        if what_to_do == '1':
            task = input('\nВы хотите зашифровать текст, используя:\n'
                         '1) Повторение короткого лозунга (слово-пароль)\n'
                         '2) Самоключ Виженера по открытому тексту\n'
                         '3) Самоключ Виженера по зашифрованному тексту\n')
            eval(f'encrypt_{task}')(text, task)

        elif what_to_do == '2':
            task = input('\nВы хотите расшифровать текст, зашифрованного при помощи:\n'
                         '1) Повторения короткого лозунга (слова-пароля)\n'
                         '2) Самоключа Виженера по открытому тексту\n'
                         '3) Самоключа Виженера по зашифрованному тексту\n')
            eval(f'decrypt_{task}')(text, task)


# функция encrypt_i / decrypt_i (i = 1,2,3) - зашифрование/расшифрование текста с помощью i-ого типа гаммирования
def encrypt_1(text, task):
    count = -1
    encrypted_text = ''
    word = input('Введите слово-пароль:\n').lower()
    for x_i in text:
        if x_i.lower() not in alphabet:
            encrypted_text += x_i
            continue
        count += 1
        gamma_i = word[count % len(word)]
        reg = x_i.lower() == x_i  # сохраняем регистр буквы
        y_i = alphabet[(ORD(x_i.lower()) + ORD(gamma_i)) % size]
        y_i = y_i if reg else y_i.upper()  # делаем букву исходного регистра
        encrypted_text += y_i
    print('\nЗашифрованный текст:\n\n' + encrypted_text + '\n')


def decrypt_1(text, task):
    count = -1
    decrypted_text = ''
    word = input('Введите слово-пароль:\n').lower()
    for y_i in text:
        if y_i.lower() not in alphabet:
            decrypted_text += y_i
            continue
        count += 1
        gamma_i = word[count % len(word)]
        reg = y_i.lower() == y_i  # сохраняем регистр буквы
        x_i = alphabet[(ORD(y_i.lower()) - ORD(gamma_i)) % size]
        x_i = x_i if reg else x_i.upper()  # делаем букву исходного регистра
        decrypted_text += x_i
    print('\nРасшифрованный текст:\n\n' + decrypted_text + '\n')


def encrypt_2(text, task):
    encrypted_text = ''
    char = input('Введите первый символ для зашифрования:\n')
    gamma_i = char
    for x_i in text:
        if x_i.lower() not in alphabet:
            encrypted_text += x_i
            continue
        reg = x_i.lower() == x_i  # сохраняем регистр буквы
        y_i = alphabet[(ORD(x_i.lower()) + ORD(gamma_i.lower())) % size]

        # в зависимости от типа гаммирования к гамме добавляется или буква открытого текста, или буква шифртекста
        gamma_i = x_i if task == '2' else y_i

        y_i = y_i if reg else y_i.upper()  # делаем букву исходного регистра
        encrypted_text += y_i
    print('\nЗашифрованный текст:\n\n' + encrypted_text + '\n')


def decrypt_2(text, task):
    decrypted_text = ''
    char = input('Введите первый символ для расшифрования:\n')
    gamma_i = char
    for y_i in text:
        if y_i.lower() not in alphabet:
            decrypted_text += y_i
            continue
        reg = y_i.lower() == y_i  # сохраняем регистр буквы
        x_i = alphabet[(ORD(y_i.lower()) - ORD(gamma_i.lower())) % size]
        # в зависимости от типа гаммирования к гамме добавляется или буква открытого текста, или буква шифртекста
        gamma_i = x_i if task == '2' else y_i
        x_i = x_i if reg else x_i.upper()  # делаем букву исходного регистра
        decrypted_text += x_i
    print('\nРасшифрованный текст:\n\n' + decrypted_text + '\n')


# гаммирования для 3 типа работает почти аналогично второму
# лишь с разницей какую букву добавлять (для этого есть проверка на тип гаммирования в функциях encrypt_2 и decrypt_2)
# с учетом этой проверки функция гаммирования для 3 типа аналогична второму
encrypt_3 = encrypt_2
decrypt_3 = decrypt_2
main()
