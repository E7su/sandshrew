# Шифр Цезаря

# строка, которая будут зашифрована/расшифрована
lang = input('Выберите язык исходного сообщения. (р - русский, а - английский)\n')
message = input('Пожалуйста, введите сообщение:\n')
# message = 'This is my secret message. WEBSERVER IS DOWN!!1'   # пример

# ключ
key = input('Выберите размер ключа:\n')
# key = 13  # пример

# режим работы программы (расшифровка/зашифровка)
mode = 'encrypt'  # 'encrypt' или 'decrypt'

# символы для шифрования

if lang == 'р':
    LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
elif lang == 'а':
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
else:
    print('Введено неверное значение.')

# хранит зашифрованную/дешифрованную форму сообщения
translated = ''

# приводит сообщение к верхнему регистру
message = message.upper()

# запускает код для посимвольного шифрования/дешифрования исходного сообщения
for symbol in message:
    if symbol in LETTERS:
        # находит номер для данного символа (зашифрованного или расшифрованного)
        num = LETTERS.find(symbol)  # берёт номер данного символа
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # выравнивание разрядной сетки исходного сообщения и алфавита
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # добавляет зашифрованный/расшифрованный символ в конец
        translated = translated + LETTERS[num]

    else:
        # добаляет символ без шифрования/дешифрования
        translated = translated + symbol

# вывод зашифрованного/расшифрованного сообщения
print(translated)
