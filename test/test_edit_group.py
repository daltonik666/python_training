from model.group import Group

def test_edit_group(app):
    app.group.edit(Group(name="groupname1", header="headre1", footer="footer1"))

