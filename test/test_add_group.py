# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="Test1", header="Test2", footer="Test3"))

def test_add_emtpy_group(app):
    app.group.create(Group(name="", header="", footer=""))
