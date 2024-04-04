import pyAesCrypt
import os
import sys

def decryption(file, password):
    #розмір буфера
    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    print("[Файл '" + str(os.path.splitext(file)[0]) + "'дешифрован]")

    os.remove(file)

def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)

password = str(input("Ваш пароль: "))
walking_by_dirs("C:\\Users\\maksa\\Desktop\\succes\\Нова папка", password)
