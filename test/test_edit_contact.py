# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="321"))
    app.session.logout()