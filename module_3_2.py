# Домашняя работа по уроку "Способы вызова функции"

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    len_r = len(recipient)
    len_s = len(sender)
    if ((recipient.find("@") == -1 or sender.find("@") == -1) or \
            (recipient[(len_r - 4):len_r] != ".com" and \
             recipient[(len_r - 4):len_r] != ".net" and \
             recipient[(len_r - 3):len_r] != ".ru" \
                    ) or \
            (sender[(len_s - 4):len_s] != ".com" and \
             sender[(len_s - 4):len_s] != ".net" and \
             sender[(len_s - 3):len_s] != ".ru" \
                    ) \
            ):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if recipient == sender:
        print(
            "Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        return
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

#send_email('Msg', 'universit.help@gmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')