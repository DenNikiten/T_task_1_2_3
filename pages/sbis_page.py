import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.logger import Logger


class SbisPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.sbis_page_url = "https://sbis.ru/"
        self.sbis_contacts_page_url_text = "tab=clients"
        self.sbis_download_page_url_text = "tab=ereport"
        self.contacts_link = (By.CSS_SELECTOR, ".sbisru-Header__menu.ws-flexbox li:nth-child(2) a")
        self.download_sbis_link = (By.CSS_SELECTOR, "[href='/download']")
        self.move_to_section_footer = (By.CSS_SELECTOR, ".sbisru-Footer__container")

    # Getters

    def get_contacts(self):
        return self.element_is_visible(self.contacts_link)

    def get_section_footer(self):
        return self.element_is_visible(self.move_to_section_footer)

    def get_download_sbis(self):
        return self.element_is_visible(self.download_sbis_link)

    # Check

    def download_sbis_link_in_footer_exist(self):
        return self.is_element_exist(self.download_sbis_link)

    # Actions

    def click_contacts(self):
        self.get_contacts().click()
        print("Click contacts")

    def action_move_to_section_footer(self):
        self.action_move_to(self.get_section_footer())
        print("Action move to section footer")

    def click_download_sbis(self):
        self.get_download_sbis().click()
        print("Click download sbis")

    # Methods

    def go_to_contacts_section(self):
        with allure.step("Go to contacts section"):
            Logger.add_start_step(method="go_to_contacts_section")
            self.go_to_site(self.sbis_page_url)
            self.click_contacts()
            assert self.text_contains_in_url(self.sbis_contacts_page_url_text), "Url does not match"
            Logger.add_end_step(url=self.driver.current_url, method="go_to_contacts_section")

    def go_to_sbis_page(self):
        with allure.step("Go to sbis page"):
            Logger.add_start_step(method="go_to_sbis_page")
            self.go_to_site(self.sbis_page_url)
            self.assert_url(self.sbis_page_url)
            Logger.add_end_step(url=self.driver.current_url, method="go_to_sbis_page")

    def find_and_go_to_download_sbis(self):
        with allure.step("Find and go to download sbis"):
            Logger.add_start_step(method="find_and_go_to_download_sbis")
            self.download_sbis_link_in_footer_exist()
            self.action_move_to_section_footer()
            self.click_download_sbis()
            assert self.text_contains_in_url(self.sbis_download_page_url_text)
            Logger.add_end_step(url=self.driver.current_url, method="find_and_go_to_download_sbis")
