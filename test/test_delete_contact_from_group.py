# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new_contact()
        contact = Contact("Test", "Test", "Testov", "SuperTest", "Title", "Company", "Moscow", "88005553535",
                          "88005553535", "88005553535", "88005553535", "email1@mail.ru", "email2@mail.ru",
                          "email3@mail.ru", "yandex.ru", "4", "August", "1991", "1", "December", "2000", "TestAddress",
                          "Moscow", "TestNotes")
        app.contact.fill_data(contact)
        app.contact.submit()
    #Запрос всех групп с контактами
    groups_list = db.get_groups_with_contacts_list()
    group = random.choice(groups_list)
    #Выбор рандомного контакта из группы
    contact_list = db.get_contacts_from_certian_group(group.id)
    contact = random.choice(contact_list)
    #Удаление контакта из группы
    app.contact.delete_contact_from_group(contact.id, group.id)
    #Проверка удаления контакта
    res = db.check_contact_with_id(contact.id)
    assert res==[]
