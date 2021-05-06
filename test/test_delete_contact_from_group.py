# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_add_contact_to_group(app, db):
    #Запрос всех групп с контактами
    groups_list = db.get_groups_with_contacts_list()
    group = random.choice(groups_list)
    #Выбор рандомного контакта из группы
    contact_list = db.get_contacts_from_certian_group(group.id)
    contact = random.choice(contact_list)
    #Удаление контакта из группы
    app.contact.delete_contact_from_group(contact.id, group.id)
    #Проверка удаления контакта из группы
    res = db.check_contact_with_id(contact.id)
    assert res==[]
