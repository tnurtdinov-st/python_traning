import re
from random import randrange

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_editpage)

def test_phones_on_view_page(app):
    contact_from_viewpage = app.contact.get_contact_from_viewpage(0)
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_viewpage.homephone == contact_from_editpage.homephone
    assert contact_from_viewpage.mobilephone == contact_from_editpage.mobilephone
    assert contact_from_viewpage.workphone == contact_from_editpage.workphone
    assert contact_from_viewpage.phone2 == contact_from_editpage.phone2

def test_random_person_info(app):
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.firstname == contact_from_editpage.firstname
    assert contact_from_homepage.lastname == contact_from_editpage.lastname
    assert contact_from_homepage.id == contact_from_editpage.id
    assert contact_from_homepage.address1 == contact_from_editpage.address1
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_editpage)
    assert contact_from_homepage.all_emails == merge_emails_like_on_homepage(contact_from_editpage)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x !="", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x !="", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email1, contact.email2, contact.email3]))))


def clear(s):
    return re.sub("[() -]", "", s)