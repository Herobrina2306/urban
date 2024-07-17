
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    pob_list1 = recipient.split('.')
    pob_list2 = sender.split('.')
    if '@' not in recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif pob_list1[-1] != 'com' and pob_list1[-1] != 'ru' and pob_list1[-1] != 'net':
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif pob_list2[-1] != 'com' and pob_list2[-1] != 'ru' and pob_list2[-1] != 'net':
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
