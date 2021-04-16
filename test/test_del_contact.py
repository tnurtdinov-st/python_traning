from model.contact import Contact

def test_del_first_group(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact()
        contact = Contact("Test", "Test", "Testov", "SuperTest", "Title", "Company", "Moscow", "88005553535",
                          "88005553535", "88005553535", "88005553535", "email1@mail.ru", "email2@mail.ru",
                          "email3@mail.ru", "yandex.ru", "4", "August", "1991", "1", "December", "2000", "TestAddress",
                          "Moscow", "TestNotes")
        app.contact.fill_data(contact)
        app.contact.submit()
    old_contact = app.contact.get_contact_list()
    app.contact.delete_contact()
    new_contact = app.contact.get_contact_list()
    assert old_contact - 1 == new_contact
