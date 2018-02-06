from model.contact import Contact
import random

def test_delete_contact_by_id(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="qqqqqqqq", middlename="wwwwwww", nickname="eeefdeeee", title="vvvvvvvvvv",
                                   lastname="eeeeeeeee", company="xccccccccc",
                                   adress="ffcvcxvcvcxvxcvx", home="23144124214", mobile="45565656678",
                                   work="56678678678", fax="67867868686",
                                   email="wap@mail.ru", email2="trest@mail.ru", email3="big@mail.ru",
                                   homepage="http://wwwww.ru", byear="1985", ayear="2000",
                                   address2="sdfdsfsdfsdfsd", phone2="sdfsdfsdfsdfsdf", notes="sfsdfsdfdssdfsdfs"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts


# Удаление контакта по индексу
#def test_delete_some_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="qqqqqqqq", middlename="wwwwwww", nickname="eeefdeeee", title="vvvvvvvvvv",
#                                   lastname="eeeeeeeee", company="xccccccccc",
#                                   adress="ffcvcxvcvcxvxcvx", home="23144124214", mobile="45565656678",
#                                   work="56678678678", fax="67867868686",
#                                   email="wap@mail.ru", email2="trest@mail.ru", email3="big@mail.ru",
#                                   homepage="http://wwwww.ru", byear="1985", ayear="2000",
#                                   address2="sdfdsfsdfsdfsd", phone2="sdfsdfsdfsdfsdf", notes="sfsdfsdfdssdfsdfs"))
#    old_contacts = app.contact.get_contact_list()
#    index = randrange(len(old_contacts))
#    app.contact.delete_contact_by_index(index)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) - 1 == len(new_contacts)
#    old_contacts[index:index + 1] = []
#    assert old_contacts == new_contacts

