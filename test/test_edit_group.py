# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="Test1", header="Test2", footer="Test3"))
    app.session.logout()