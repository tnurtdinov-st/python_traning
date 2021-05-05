# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import random

def test_edit_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = 'test'))
    old_groups = db.get_group_list()
    group_init = random.choice(old_groups)
    group = Group(name="Test1", header="Test2", footer="Test3")
    app.group.edit_group_by_id(group_init.id, group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
