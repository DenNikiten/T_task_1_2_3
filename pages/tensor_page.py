import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.logger import Logger


class TensorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.tensor_about_page_url = "https://tensor.ru/about"
        self.move_to_section_strength_in_people = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg")
        self.block_strength_in_people = (By.XPATH, "//p[contains(text(),'Сила в людях')]")
        self.more_details_link = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-bg p:last-child a")

    # Getters

    def get_section_strength_in_people(self):
        return self.element_is_visible(self.move_to_section_strength_in_people)

    def get_more_details_link(self):
        return self.element_is_present(self.more_details_link)

    # Check

    def is_block_strength_in_people_exist(self):
        return self.is_element_exist(self.block_strength_in_people)

    def is_link_more_details_exist(self):
        return self.is_element_exist(self.more_details_link)

    # Actions

    def action_move_to_section_strength_in_people(self):
        self.action_move_to(self.get_section_strength_in_people())
        print("Action move to section strength in people")

    def click_more_details_link(self):
        self.get_more_details_link().click()
        print("Click more details link")

    # Method

    def check_block_strength_in_people(self):
        with allure.step("Check block strength in people"):
            Logger.add_start_step(method="check_block_strength_in_people")
            self.action_move_to_section_strength_in_people()
            assert self.is_block_strength_in_people_exist(), "block 'Strength in people' does not exist "
            Logger.add_end_step(url=self.driver.current_url, method="check_block_strength_in_people")

    def select_more_details_and_check_page_tensor_about_is_open(self):
        with allure.step("Select More details and check page tensor about is open"):
            Logger.add_start_step(method="select_more_details_and_check_the_site_is_open")
            self.is_link_more_details_exist()
            self.click_more_details_link()
            self.assert_url(self.tensor_about_page_url)
            Logger.add_end_step(url=self.driver.current_url,
                                method="select_more_details_and_check_page_tensor_about_is_open")