# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="qqqqqqqq", middlename="wwwwwww", nickname="eeefdeeee", title="vvvvvvvvvv", lastname="eeeeeeeee", company="xccccccccc",
                               adress="ffcvcxvcvcxvxcvx", home="23144124214", mobile="45565656678", work="56678678678", fax="67867868686",
                               email="wap@mail.ru", email2="trest@mail.ru", email3="big@mail.ru", homepage="http://wwwww.ru", byear="1985", ayear="2000",
                               address2="sdfdsfsdfsdfsd", phone2="sdfsdfsdfsdfsdf", notes="sfsdfsdfdssdfsdfs")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)