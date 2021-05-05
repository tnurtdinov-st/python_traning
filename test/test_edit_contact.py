# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_edit_random_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact()
        contact = Contact("Test", "Test", "Testov", "SuperTest", "Title", "Company", "Moscow", "88005553535",
                    "88005553535", "88005553535", "88005553535", "email1@mail.ru", "email2@mail.ru",
                    "email3@mail.ru", "yandex.ru", "4", "August", "1991", "1", "December", "2000", "TestAddress",
                    "Moscow", "TestNotes")
        app.contact.fill_data(contact)
        app.contact.submit()
    old_contact = db.get_contact_list()
    contact_init = random.choice(old_contact)
    app.contact.edit_contact_by_id(contact_init.id)
    contact = Contact("7Alex", "7Song", "Test3", "Test4", "Title3", "Company1", "Moscow1", "11111",
                   "1111", "11111", "33333", "email1222@mail.ru", "email2333@mail.ru",
                   "email3444@mail.ru", "rambler.ru", "3", "December", "1990", "1", "December", "2000", "Address",
                   "Moscow111", "Notes")
    contact.id = contact_init.id
    app.contact.fill_data(contact)
    app.contact.update()
    new_contact = db.get_contact_list()
    for i in old_contact:
        if i.id==contact.id:
            i.firstname = contact.firstname
            i.lastname = contact.lastname
            break
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
