import simplecrypt

with open("encrypted.bin", "rb") as inp:
    ciphertext = inp.read()

with open("passwords.txt", "r") as inp:
    for password in inp:
        try:
            print('try ', password)
            plaintext = simplecrypt.decrypt(password.strip(), ciphertext)
            # the decrypted plaintext is bytes, but we can convert it back to a string
            print("plaintext: %s" % plaintext)
            print("plaintext as string: %s" % plaintext.decode('utf8'))
        except:
            print('wrong pasword: ', password)

'''
Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.
'''