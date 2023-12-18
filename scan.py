import sys
from pathlib import Path

image_files = list()  # списки для отсортированных по расширению файлов
video_files = list()
docx_files = list()
audio_files = list()
archives = list()
others = list()

folders = list()   #  для хранения  папок
unknown = set() # множество НЕизвестных расширений
extensions = set() # множество известных расширений

registered_extensions = {    # словарь для сортировки файлов по расширению
    'JPEG': image_files,
    'PNG': image_files,
    'JPG': image_files,
    'SVG': image_files,
    'AVI': video_files,
    'MP4': video_files,
    'MOV': video_files,
    'MKV': video_files,
    'DOC': docx_files,
    'DOCX': docx_files,
    'TXT': docx_files,
    'PDF': docx_files,
    'XLSX': docx_files,
    'PPTX': docx_files,
    'MP3': audio_files,
    'OGG': audio_files,
    'WAV': audio_files,
    'AMR': audio_files,
    'ZIP': archives,
    'GZ': archives,
    'TAR': archives
}

def get_extensions(file_name):   # функция для выделения расширения файла    ??? suffix
    return Path(file_name).suffix[1:].upper()   # перевод в верхний регистр чтобы сопоставить со словарем registered_extensions

def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():   
            if item.name not in ('images', 'video', 'documents', 'audio', 'archives', 'other'): # если объект папка, которая подлежит сортировке
                folders.append(item) # добавляется адрес папки в список folders
                scan(item) # переход наслед уровень сканирования
            continue

        extension = get_extensions(file_name=item.name)   # если объект не директория ,т.е. файл - извлекается расширение
        new_name = folder/item.name
        if not extension:    # для файлов без раширения типа _pycach_
            others.append(new_name)
        else:
            try:
                container = registered_extensions[extension]  # список зарегистрированных расширений, которые были в отсканированной папке  
                extensions.add(extension)  # пополнение множества известных расширений
                container.append(new_name)  # пополнение списка файлов с зарегистрированным расширением
            except KeyError:  # обработка для случая отсутствия ключа(расширения)  в словаре registered_extensions
                unknown.add(extension)  # пополнение множества НЕизвестных расширений
                others.append(new_name)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    folder = Path(path)

    scan(folder)

    print(f"images: {image_files}")
    print(f"video: {video_files}")
    print(f"documents: {docx_files}")
    print(f"audio: {audio_files}")
    print(f"archives: {archives}")
    print(f"other: {others}")
    print(f"All extensions: {extensions}")
    print(f"Unknown extensions: {unknown}")
    print(f"Folder: {folders}")