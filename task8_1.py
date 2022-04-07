import re

def email_parse(txt):
    pattern = re.compile(r'\b[\w.-]+?@[\w-]+?\.\w+?\b')
    result = re.findall(pattern, txt)
    return result

if __name__ == '__main__':
    txt = 'Добрый день, меня зовут Татьяна Лысенко, по всем вопросам мне можно писать на адрес' \
          'электронной почты tatyana_lysenko@mail.ru или же на рабочую почту - tatyana.lysenko@roto-frank.com'
    print(email_parse(txt))