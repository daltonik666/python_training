


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def create(self, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        # init group creation
        driver.find_element_by_name("new").click()
        self.fill_group_form(new_group_data)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def edit(self, group):
        driver = self.app.driver
        self.open_groups_page()
        # select first group
        driver.find_element_by_name("selected[]").click()
        # init group edit
        driver.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit group edit
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        driver = self.app.driver
        self.type("group_name", group.name)
        self.type("group_header", group.header)
        self.type("group_footer", group.footer)

    def type(self, field_name, text) :
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        driver.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))


