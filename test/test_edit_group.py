# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="groupname1", header="headre1", footer="footer1"))
    app.session.logout()