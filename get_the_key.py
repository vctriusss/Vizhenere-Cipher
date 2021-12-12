# оставим в зашифрованном текста только буквы (уберем знаки препинания и пробелы)
print('Добро пожаловать в программу определения длины ключа Шифра Виженера методом Касиски и частотным анализом')
lang = input('Выберите язык текста:\n1) Русский\n2) Английский\n')
text = input('Введите текст:\n\n').lower()
if lang == '2':
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
else:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
x = ''
for c in text:
    if c in alphabet:
        x += c
# в 1 словаре хранятся столбцы Y_i
# во 2 словаре хранятся значения I_c для каждого солбца
# в 3 словаре хранятся средние значения I_c для каждой длины ключа
dct, ic, avg = dict(), dict(), dict()
# расчитаем индексы совпадений для различных длин ключей
for l in range(1, 10):
    # делим исходный текст на l столбцов (l - длина ключа)
    print(f'Длина ключа: {l}')
    for i, symb in enumerate(x):
        n = i % l
        if f'y_{n}' not in dct.keys():
            dct[f'y_{n}'] = symb
        else:
            dct[f'y_{n}'] += symb
    # расчитаем индексы совпадений для различных длин ключей
    for y, s in dct.items():
        summ = 0
        for letter in alphabet:
            fi = s.count(letter)
            if fi != 0:
                summ += (fi * (fi - 1))
        ic[f'Ic_{y[-1]}'] = summ / (len(s) * (len(s) - 1))  # индекс совпадения для i-того столбца
        print(f"Ic_{y[-1]}: {ic[f'Ic_{y[-1]}']}")
    avg[l] = sum(ic.values()) / l
    print(f'Среднее значение I_c: {avg[l]}\n')
    dct.clear()
    ic.clear()

# определим предположительную длину ключа
maxic = max(avg.values(), key=lambda z: -abs(z - 0.066) if lang == '2' else -abs(z - 0.053))
supp_key = 0
for k, v in avg.items():
    if v == maxic:
        supp_key = k
        break
print('Предположительная длина ключа:', supp_key, f'(Ic = {avg[supp_key]})\n')
# чтобы найти ключ используем предположительную длину ключа как истинную
l = supp_key
dct = dict()
for i, symb in enumerate(x):
    n = i % l
    if f'y_{n}' not in dct.keys():
        dct[f'y_{n}'] = symb
    else:
        dct[f'y_{n}'] += symb
# Для 1 столбца расчитаем его длину, а также кол-во каждой буквы в нем
letters0 = dict()
for c in alphabet:
    letters0[c] = dct['y_0'].count(c)
m0 = len(dct['y_0'])

# для всех столбцов переберем все сдвиги и расчитаем тот, где индекс MI_c максимален
max_mic, max_shift = 0, 0
shifts = [0]
for name, col in dct.items():
    m = len(col)
    if name == 'y_0':
        continue
    for shift in range(len(alphabet)):
        # создаем новый столбец со сдвигом
        new_col = [alphabet[(alphabet.index(c) + shift) % len(alphabet)] for c in col]
        summ = 0
        # расчитываем индекс совпадения
        for c in alphabet:
            summ += new_col.count(c) * letters0[c]
        mic = summ / (m * m0)
        # чем больше MI_c, тем выше шансы, что сдвиг выбран верно, поэтому выбираем максимальную
        if max_mic < mic:
            max_mic = mic
            max_shift = shift
    shifts.append(max_shift)
    print(f'Столбец {name[-1]}: сдвиг {max_shift} (MI_c = {max_mic})')
    max_mic = 0
    max_shift = 0
print('\nВозможные ключи:\n')
# выведем список всех возможных ключей (для каждой буквы алфавита в качестве первой буквы ключа)
count = -4
for c in alphabet:
    for s in shifts:
        print(alphabet[(alphabet.index(c) - s) % len(alphabet)], end='')
    print(['\t\t', '\n'][count % 5 == 0], end='')
    count += 1
