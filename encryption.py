import pyAesCrypt
import os
import sys

def encryption(file, password):
    #розмір буфера
    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + "crp",
        password,
        buffer_size
    )

    print("[Файл '" + str(os.path.splitext(file)[0]) + "'зашифрован]")

    os.remove(file)

def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)

password = str(input("Ваш пароль: "))
walking_by_dirs("C:\\Users\\maksa\\Desktop\\succes\\Нова папка", password)
