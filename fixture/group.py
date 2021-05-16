from model.group import Group
import random
from model.contact import Contact
import allure
class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        # Return to group page
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
             wd.find_element_by_link_text("groups").click()

    @allure.step('When I add a group "{group}" to the list')
    def create(self, group):
        wd = self.app.wd
        # Init group creation
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fio_group_form(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def fio_group_form(self, group):
        wd = self.app.wd
        # Init group firm
        self.change_filed_value("group_name", group.name)
        self.change_filed_value("group_header", group.header)
        self.change_filed_value("group_footer", group.footer)


    def change_filed_value(self, field_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_groups_page(self):
        wd = self.app.wd
        # Open group page
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
             wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        self.select_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None


    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_group(self, group):
        self.edit_group_by_index(0, group)

    def edit_group_by_index(self, index, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fio_group_form(group)
        # Submit group update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def edit_group_by_id(self, id, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        self.fio_group_form(group)
        # Submit group update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0, new_group_data)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # Edit name
        wd.find_element_by_name("edit").click()
        self.fio_group_form(new_group_data)
        # Submit group update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def find_group_to_add_contact(self, Contact):
        wd = self.app.wd
        self.app.open_home_page()
        groups = self.get_group_list()
        self.app.open_home_page()
        while 1:
            group = random.choice(groups)
            wd.find_element_by_name("group").send_keys(group.name)
            wd.find_element_by_css_selector("body").click()
            contacts = self.get_contact_list_in_group()
            if Contact not in contacts:
                wd.find_element_by_name("group").send_keys("[all]")
                wd.find_element_by_css_selector("body").click()
                return group, contacts

    def get_contact_list_in_group(self):
            wd = self.app.wd
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
            return list(self.contact_cache)

    def group_contacts(self, Group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("group").send_keys(Group.name)
        wd.find_element_by_css_selector("body").click()
        contacts = self.get_contact_list_in_group()
        wd.find_element_by_name("group").send_keys("[all]")
        wd.find_element_by_css_selector("body").click()
        return contacts