


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def open_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()


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

    def delete_first_contact(self):
        driver = self.app.driver
        self.open_home_page()
        # select first contact
        driver.find_element_by_name("selected[]").click()
        # submit deletion
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Delete 1 addresses[\s\S]$")
        self.return_to_home_page()


    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    def close_alert_and_get_its_text(self):
        driver = self.app.driver
        try:
            alert = self.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True