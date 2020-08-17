


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create_contact(self, contact):
        driver = self.app.driver
        # init contact creation
        driver.find_element_by_link_text("add new").click()
        # fill contact firm
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        # submit contact creation
        driver.find_element_by_name("submit").click()