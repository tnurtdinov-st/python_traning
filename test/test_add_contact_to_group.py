# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group

import random

def test_add_contact_to_group(app, db):
    #Добавление контакта если нет контактов без группы
    if len(db.get_contact_list_without_group()) == 0:
        app.contact.add_new_contact()
        contact = Contact("Test", "Test", "Testov", "SuperTest", "Title", "Company", "Moscow", "88005553535",
                          "88005553535", "88005553535", "88005553535", "email1@mail.ru", "email2@mail.ru",
                          "email3@mail.ru", "yandex.ru", "4", "August", "1991", "1", "December", "2000", "TestAddress",
                          "Moscow", "TestNotes")
        app.contact.fill_data(contact)
        app.contact.submit()
    #Добавление пустой группы если нет группы без контактов
    if len(db.get_groups_without_contacts_list()) == 0:
        app.group.create(Group(name='test'))
    #Список контактов БЕЗ группы
    contact_list = db.get_contact_list_without_group()
    contact = random.choice(contact_list)
    #Список групп БЕЗ контактов
    groups_list = db.get_groups_without_contacts_list()
    group = random.choice(groups_list)
    #Добавление контакта в группу
    app.contact.add_contact_to_group(contact.id, group.id)
    #Переход в группу и проверка наличия контакта с id
    app.contact.check_contact_in_new_group(contact.id, group.id)
