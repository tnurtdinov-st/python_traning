# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_main(app):
    app.contact.edit_contact()
    app.contact.fill_data(Contact("Test1", "Test2", "Test3", "Test4", "Title3", "Company1", "Moscow1", "11111",
                   "1111", "11111", "33333", "email1222@mail.ru", "email2333@mail.ru",
                   "email3444@mail.ru", "rambler.ru", "3", "December", "1990", "1", "December", "2000", "Address",
                   "Moscow111", "Notes"))
    app.contact.update()
