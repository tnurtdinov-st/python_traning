# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = 'test'))
    app.group.edit_group(Group(name="Test1", header="Test2", footer="Test3"))