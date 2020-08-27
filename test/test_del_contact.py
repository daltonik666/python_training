from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="123"))
    app.contact.delete_first_contact()