
class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        # Return to group page
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
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

    def open_groups_page(self):
        wd = self.app.wd
        # Open group page
        wd.find_element_by_link_text("groups").click()
