# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random

def test_delete_contact_to_group(app, db):
    #Проверка наличия групп с контактами
    if len(db.get_groups_with_contacts_list()) == 0:
        #Проверка есть ли вообще группы
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name='test'))
            # проверка есть ли контакты без групп
        if len(db.get_contacts_not_in_group()) == 0:
            app.contact.add_new_contact()
            contact = Contact("Test", "Test", "Testov", "SuperTest", "Title", "Company", "Moscow", "88005553535",
                              "88005553535", "88005553535", "88005553535", "email1@mail.ru", "email2@mail.ru",
                              "email3@mail.ru", "yandex.ru", "4", "August", "1991", "1", "December", "2000",
                              "TestAddress",
                              "Moscow", "TestNotes")
            app.contact.fill_data(contact)
            app.contact.submit()
        #Добавление контакта в групп3
        contact_list = db.get_contacts_not_in_group()
        contact = random.choice(contact_list)
        # Список групп БЕЗ контактов
        groups_list = db.get_groups_without_contacts_list()
        group = random.choice(groups_list)
        # Добавление контакта в группу
        app.contact.add_contact_to_group(contact.id, group.id)

    #Запрос всех групп с контактами
    groups_list = db.get_groups_with_contacts_list()
    group = random.choice(groups_list)
    #Выбор рандомного контакта из группы
    contact_list = db.get_contacts_in_group(group.id)
    contact = random.choice(contact_list)
    #Удаление контакта из группы
    app.contact.delete_contact_from_group(contact.id, group.id)
    #Проверка удаления контакта из группы
    res = db.check_contact_with_id(contact.id)
    assert res==[]
