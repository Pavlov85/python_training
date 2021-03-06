from model.contact import Contact
from random import randrange

def test_edit_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="qqqqqqqq", middlename="wwwwwww", nickname="eeefdeeee", title="vvvvvvvvvv",
                                   lastname="eeeeeeeee", company="xccccccccc",
                                   adress="ffcvcxvcvcxvxcvx", home="23144124214", mobile="45565656678",
                                   work="56678678678", fax="67867868686",
                                   email="wap@mail.ru", email2="trest@mail.ru", email3="big@mail.ru",
                                   homepage="http://wwwww.ru", byear="1985", ayear="2000",
                                   address2="sdfdsfsdfsdfsd", phone2="sdfsdfsdfsdfsdf", notes="sfsdfsdfdssdfsdfs"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="a", middlename="b", nickname="c", title="d", lastname="e", company="f",
                               adress="g", home="1", mobile="2", work="3", fax="4",
                               email="wapxl@mail.ru", email2="best@mail.ru", email3="123@mail.ru", homepage="http://test.ru", byear="1986", ayear="2017",
                               address2="as", phone2="df", notes="fg")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)