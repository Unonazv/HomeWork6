import re

UKRAINIAN_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")

TRANS = {}  # таблица сопоставления для транслитерации 

for key, value in zip(UKRAINIAN_SYMBOLS, TRANSLATION):
    TRANS[ord(key)] = value  # для нижнего регистра
    TRANS[ord(key.upper())] = value.upper() # для верхнего регистра

def normalize(name: str) -> str:
    name, *extension = name.split('.')
    new_name = name.translate(TRANS)
    new_name = re.sub(r'\W', '_', new_name) # ругулярные выражения \W- все что НЕ буква, цифра, нижнее подчеркивание заменяется на "_"
    return f"{new_name}.{'.'.join(extension)}"
if __name__ == '__main__':
    print(normalize('={H6йVЇQ.tar.gz'))