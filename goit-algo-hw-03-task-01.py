import os
import shutil
import sys

def copy_files(source_dir, dest_dir):
    # Перевіряємо, чи існує директорія призначення, якщо ні - створюємо її
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Рекурсивно копіюємо файли та сортуємо їх
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Отримуємо повний шлях до файлу
            file_path = os.path.join(root, file)
            # Отримуємо розширення файлу
            _, file_extension = os.path.splitext(file)
            # Створюємо піддиректорію за розширенням файлу
            subdir = os.path.join(dest_dir, file_extension[1:].lower())
            # Перевіряємо, чи існує піддиректорія, якщо ні - створюємо її
            if not os.path.exists(subdir):
                os.makedirs(subdir)
            # Копіюємо файл у відповідну піддиректорію
            shutil.copy(file_path, subdir)

if __name__ == "__main__":
    # Перевірка правильності введених аргументів командного рядка
    if len(sys.argv) != 3:
        print("Usage: python goit-algo-hw-03-task-01.py source_directory destination_directory")
        sys.exit(1)

    # Отримуємо шляхи до вихідної та призначенної директорій з аргументів командного рядка
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    try:
        # Викликаємо функцію копіювання файлів
        copy_files(source_directory, destination_directory)
        print("Files copied and sorted successfully!")
    except Exception as e:
        print("An error occurred:", e)
