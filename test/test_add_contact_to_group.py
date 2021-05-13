# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group

import random

def test_add_contact_to_group(app, db):
    #Добавление пустой группы если нет группы
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    #Добавление контакта если нет контактов
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact()
        contact = Contact("Test", "Test", "Testov", "SuperTest", "Title", "Company", "Moscow", "88005553535",
                          "88005553535", "88005553535", "88005553535", "email1@mail.ru", "email2@mail.ru",
                          "email3@mail.ru", "yandex.ru", "4", "August", "1991", "1", "December", "2000", "TestAddress",
                          "Moscow", "TestNotes")
        app.contact.fill_data(contact)
        app.contact.submit()
    contact = random.choice(db.get_contacts_not_in_group())
    group = random.choice(db.get_groups_without_contact(contact.id))
    old_contact = db.get_contacts_in_group(group.id)
    app.contact.add_contact_to_group(contact.id, group.id)
    new_contact = db.get_contacts_in_group(group.id)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    assert group.id in db.get_group_id_of_contact(contact)