from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHepler


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(120)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHepler(self)

    def open_home_page(self):
        wd = self.wd
        # Open homepage
        wd.get("http://localhost/addressbook")

    def destroy(self):
        self.wd.quit()
