from model.contact import Contact
from random import randrange


def test_del_random_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new_contact()
        contact = Contact("Test", "Test", "Testov", "SuperTest", "Title", "Company", "Moscow", "88005553535",
                          "88005553535", "88005553535", "88005553535", "email1@mail.ru", "email2@mail.ru",
                          "email3@mail.ru", "yandex.ru", "4", "August", "1991", "1", "December", "2000", "TestAddress",
                          "Moscow", "TestNotes")
        app.contact.fill_data(contact)
        app.contact.submit()
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete_contact_by_index(index)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index:index+1] = []
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)

