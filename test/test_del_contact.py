

def test_del_first_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact()
    app.session.logout()