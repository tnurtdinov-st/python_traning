# -*- coding: utf-8 -*-
from model.contact import Contact

def test_main(app):
    old_contact = app.contact.get_contact_list()
    app.contact.add_new_contact()
    contact = Contact("Test", "Test", "Testov", "SuperTest", "Title", "Company", "Moscow", "88005553535",
                   "88005553535", "88005553535", "88005553535", "email1@mail.ru", "email2@mail.ru",
                   "email3@mail.ru", "yandex.ru", "4", "August", "1991", "1", "December", "2000", "TestAddress",
                   "Moscow", "TestNotes")
    app.contact.fill_data(contact)
    app.contact.submit()
    assert old_contact + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    assert old_contact + 1 == new_contact


def test_alt(app):
    old_contact = app.contact.get_contact_list()
    app.contact.add_new_contact()
    contact=Contact("Test1", "Test2", "Test3", "Test4", "Title3", "Company1", "Moscow1", "11111",
                   "1111", "11111", "33333", "email1222@mail.ru", "email2333@mail.ru",
                   "email3444@mail.ru", "rambler.ru", "3", "December", "1990", "1", "December", "2000", "Address",
                   "Moscow111", "Notes")
    app.contact.fill_data(contact)
    app.contact.submit()
    new_contact = app.contact.get_contact_list()
    assert old_contact + 1 == new_contact
