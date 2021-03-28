from selenium import webdriver
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def return_to_group_page(self):
        wd = self.wd
        # Return to group page
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        # Init group creation
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        # Init group firm
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def open_home_page(self):
        wd = self.wd
        # Open homepage
        wd.get("http://localhost/addressbook")

    def open_groups_page(self):
        wd = self.wd
        # Open group page
        wd.find_element_by_link_text("groups").click()

    def destroy(self):
        self.wd.quit()
