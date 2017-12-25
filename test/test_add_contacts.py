# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.template import Template


@pytest.fixture
def tmp(request):
    fixture = Template()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(tmp):
    tmp.login(username="admin", password="secret")
    tmp.create_contact(Contact(firstname="qqqqqqqq", middlename="wwwwwww", nickname="eeefdeeee", title="vvvvvvvvvv", lastname="eeeeeeeee", company="xccccccccc",
                            adress="ffcvcxvcvcxvxcvx", home="23144124214", mobile="45565656678", work="56678678678", fax="67867868686",
                            email="wap@mail.ru", email2="trest@mail.ru", email3="big@mail.ru", homepage="http://wwwww.ru", byear="1985", ayear="2000",
                            adress2="sdfdsfsdfsdfsd", phone2="sdfsdfsdfsdfsdf", notes="sfsdfsdfdssdfsdfs"))
    tmp.logout()


