import email #стандартная библиотека для получения почты
import poplib #стандартная библиотека для того, чтобы распарсить текст сообщения
import time

class MailHelper:

    def __init__(self, app):
        self.app = app # сохраняет ссылку на основной объект

    def get_mail(self, username, password, subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config["james"]["host"]) #устанавливаем соединение / получаем из конфигурации
            pop.user(username)# указываем с каким именем и паролем надо открыть сессию
            pop.pass_(password)
            num = pop.stat()[0]# метод возвращает статическую информацию, что имеется в почт.ящике / первый элемент кортежа=колич-во писем
            if num > 0:
                for n in range(num):
                    msglines = pop.retr(n+1)[1]# метод возвращает кортеж = строки
                    msgtext = "\n".join(map(lambda x: x.decode("utf-8"), msglines))
                    msg = email.message_from_string(msgtext)
                    if msg.get("Subject") == subject:
                        pop.dele(n+1)
                        pop.quit()
                        return msg.get_payload()
            pop.close()
            time.sleep(5)
        return None
