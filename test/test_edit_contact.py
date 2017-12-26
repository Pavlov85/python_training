from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="a", middlename="b", nickname="c", title="d", lastname="e", company="f",
                               adress="g", home="1", mobile="2", work="3", fax="4",
                               email="wapxl@mail.ru", email2="best@mail.ru", email3="123@mail.ru", homepage="http://test.ru", byear="1986", ayear="2017",
                               address2="as", phone2="df", notes="fg"))
    app.session.logout()