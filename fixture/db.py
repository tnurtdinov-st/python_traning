import pymysql.cursors
from model.group import Group
from model.contact import Contact
import allure
import time

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    @allure.step('Given a group list')
    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    @allure.step('Then the new group list is equal to the old list with the added group')
    def new_get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        time.sleep(3)
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contacts_not_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname  FROM addressbook WHERE deprecated='0000-00-00 00:00:00' and id NOT IN ( SELECT id FROM address_in_groups WHERE address_in_groups.id = addressbook.id)")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_groups_without_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list WHERE group_id NOT IN ( SELECT group_id FROM address_in_groups WHERE address_in_groups.group_id = group_list.group_id)")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_groups_without_contact(self, contact):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list WHERE group_id IN ( SELECT group_id FROM address_in_groups WHERE address_in_groups.id !="+contact+")")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_groups_with_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list WHERE group_id IN ( SELECT group_id FROM address_in_groups WHERE address_in_groups.group_id = group_list.group_id)")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select addressbook.id, addressbook.firstname, addressbook.lastname from addressbook, address_in_groups where addressbook.deprecated='0000-00-00 00:00:00' and addressbook.id=address_in_groups.id and address_in_groups.group_id='"+group_id+"'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def check_contact_with_id(self, id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select addressbook.id, addressbook.firstname, addressbook.lastname from addressbook, address_in_groups  where addressbook.id='"+id+"' and addressbook.id=address_in_groups.id")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_group_id_of_contact(self, contact):
        group_id_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("Select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                if contact.id == str(id):
                    group_id_list.append(str(group_id))
        finally:
            cursor.close()
        return group_id_list

    def destroy(self):
        self.connection.close()



