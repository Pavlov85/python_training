# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="qqqqqqqq", middlename="wwwwwww", nickname="eeefdeeee", title="vvvvvvvvvv", lastname="eeeeeeeee", company="xccccccccc",
                               adress="ffcvcxvcvcxvxcvx", home="23144124214", mobile="45565656678", work="56678678678", fax="67867868686",
                               email="wap@mail.ru", email2="trest@mail.ru", email3="big@mail.ru", homepage="http://wwwww.ru", byear="1985", ayear="2000",
                               address2="sdfdsfsdfsdfsd", phone2="sdfsdfsdfsdfsdf", notes="sfsdfsdfdssdfsdfs"))
