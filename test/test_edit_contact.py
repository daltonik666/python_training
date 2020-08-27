# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="123"))
    app.contact.edit(Contact(firstname="321"))