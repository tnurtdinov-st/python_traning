import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

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

    def get_contact_list(self):
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

    def get_groups_with_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_list.group_id, group_list.group_name, group_list.group_header, group_list.group_footer from group_list, address_in_groups where group_list.group_id = address_in_groups.group_id")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_from_certian_group(self, group_id):
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



    def destroy(self):
        self.connection.close()



