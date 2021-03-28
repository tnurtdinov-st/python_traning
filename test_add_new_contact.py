# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_new_contact import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_main(app):
    app.login(username="admin", password="secret")
    app.add_new_contact()
    app.fill_data(Contact("Test", "Test", "Testov", "SuperTest", "Title", "Company", "Moscow", "88005553535",
                   "88005553535", "88005553535", "88005553535", "email1@mail.ru", "email2@mail.ru",
                   "email3@mail.ru", "yandex.ru", "4", "August", "1991", "1", "December", "2000", "TestAddress",
                   "Moscow", "TestNotes"))
    app.logout()

def test_alt(app):
    app.login(username="admin", password="secret")
    app.add_new_contact()
    app.fill_data(Contact("Test1", "Test2", "Test3", "Test4", "Title3", "Company1", "Moscow1", "11111",
                   "1111", "11111", "33333", "email1222@mail.ru", "email2333@mail.ru",
                   "email3444@mail.ru", "rambler.ru", "3", "December", "1990", "1", "December", "2000", "Address",
                   "Moscow111", "Notes"))
    app.logout()
