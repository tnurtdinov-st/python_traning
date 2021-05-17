import pytest
from fixture.application import Application
from fixture.db import DbFixture
import json
import os.path
from model.group import Group
from model.contact import Contact
import time

class AddressBook:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config = "target.json", browser = "chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixture(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config['baseUrl'])
        self.fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
        db_config = self.target['db']
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['database'], user=db_config['user'], password=db_config['password'])

    def destroy_fixture(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def get_contact_list(self):
        return self.dbfixture.get_contact_list()

    def new_contact(self, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax, email,
                email2, email3, homepage, address2, phone2, notes, bday, bmonth, byear, aday, amonth, ayear):
        return Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
                   company=company, address1=address, homephone=home, mobilephone=mobile, workphone=work, fax=fax,
                   email1=email, email2=email2, email3=email3, homepage=homepage, bdaydate=bday, bmonth=bmonth,
                   aday=aday, amonth=amonth, byear=byear, ayear=ayear, address2=address2, phone2=phone2, notes1=notes)

    def create_contact(self, contact):
        self.fixture.contact.add_new_contact()
        self.fixture.contact.fill_data(contact)
        self.fixture.contact.submit()

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)


    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def edit_contact(self, contact):
        self.fixture.contact.edit_contact_by_id(contact.id)


    def edited_contact(self, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax, email,
                email2, email3, homepage, address2, phone2, notes, bday, bmonth, byear, aday, amonth, ayear):
        return Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
                   company=company, address1=address, homephone=home, mobilephone=mobile, workphone=work, fax=fax,
                   email1=email, email2=email2, email3=email3, homepage=homepage, bdaydate=bday, bmonth=bmonth,
                   aday=aday, amonth=amonth, byear=byear, ayear=ayear, address2=address2, phone2=phone2, notes1=notes)

    def update_contact(self, contact):
        self.fixture.contact.fill_data(contact)
        self.fixture.contact.update()
        time.sleep(5)

    def edit_old_list(self, old_contact,  contact):
        for i in old_contact:
            if i.id==contact.id:
                i.firstname = contact.firstname
                i.lastname = contact.lastname
        return old_contact