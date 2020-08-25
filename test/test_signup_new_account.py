import string
import random
import time

def random_username(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_signup_new_account(app):
    username = random_username("user_", 10)# maxlen=10
    email = username + "@localhost" #т.к. адреса на локальной машине
    password = "test"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    # app.session.login(username, password)#9.4 pop3
    # assert app.session.is_logged_in_as(username) #9.4 pop3
    # app.session.logout() #9.4 pop3
    assert app.soap.can_login(username, password)# делаем проверку через SOAP интерфейс