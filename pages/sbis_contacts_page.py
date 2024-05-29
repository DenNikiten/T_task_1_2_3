import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.logger import Logger


class SbisContactsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.my_region = "Свердловская обл."
        self.new_region = "Камчатский край"
        self.new_region_info_url = "41-kamchatskij-kraj"
        self.tensor_page_url = "https://tensor.ru/"
        self.banner_tensor = (By.XPATH, "(//a[@href='https://tensor.ru/']/img)[1]")
        self.choose_region_link = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser.ml-16 span")
        self.choose_new_region_field = (By.XPATH, "(//div[@data-qa='controls-Render__field']/input)[1]")
        self.change_region_on = (By.CSS_SELECTOR, f"span[title*='{self.new_region}']")
        self.list_partners = (By.CLASS_NAME, "sbisru-Contacts-List__col-1")
        self.my_region_list = self.save_list_partners_my_region()

    # Getters

    def get_region(self):
        return self.element_is_present(self.choose_region_link)

    def get_region_field(self):
        return self.element_is_present(self.choose_new_region_field)

    def get_new_region(self):
        return self.element_is_present(self.change_region_on)

    def get_list_partners(self):
        list_partners = self.elements_are_present(self.list_partners)
        return list_partners

    # Actions

    def save_list_partners_my_region(self):
        return self.get_list_partners()

    def save_list_partners_new_region(self):
        return self.get_list_partners()

    def click_banner_tensor(self):
        self.element_is_visible(self.banner_tensor).click()
        print("Click banner tensor")

    def click_my_region_btn(self):
        self.get_region().click()
        print("Click region button")

    def input_new_region(self, region):
        self.get_region_field().send_keys(region)
        print("Input new region")

    def click_new_region_btn(self):
        self.get_new_region().click()
        print("Click new region button")

    # Check

    def banner_tensor_displayed(self):
        return self.element_is_displayed(self.banner_tensor)

    def check_selected_region_substituted(self, region):
        return self.text_is_present_in_element(self.choose_region_link, region)

    # Methods

    def select_banner_tensor(self):
        with allure.step("Select banner tensor"):
            Logger.add_start_step(method="select_banner_tensor")
            self.banner_tensor_displayed()
            self.click_banner_tensor()
            Logger.add_end_step(url=self.driver.current_url, method="select_banner_tensor")

    def switch_to_window_tensor(self):
        with allure.step("Switch to window tensor"):
            Logger.add_start_step(method="switch_to_window_tensor")
            self.switch_window(1)
            self.assert_url(self.tensor_page_url)
            Logger.add_end_step(url=self.driver.current_url, method="switch_to_window_tensor")

    def check_region_and_list_partners(self):
        with allure.step("Check region and list partners"):
            Logger.add_start_step(method="check_region_and_list_partners")
            self.assert_word(self.get_region(), self.my_region)
            assert self.save_list_partners_my_region() is not None, "There is no list of partners in my region"
            Logger.add_end_step(url=self.driver.current_url, method="check_region_and_list_partners")

    def change_on_new_region(self):
        with allure.step("Change on new region"):
            Logger.add_start_step(method="change_on_new_region")
            self.click_my_region_btn()
            self.input_new_region(self.new_region)
            self.click_new_region_btn()
            Logger.add_end_step(url=self.driver.current_url, method="change_on_new_region")

    def check_new_region_url_title_list_partners(self):
        with allure.step("Check new region * url * title * list partners"):
            Logger.add_start_step(method="check_new_region_url_title_list_partners")
            assert self.check_selected_region_substituted(self.new_region), "The region has not changed"
            assert self.save_list_partners_new_region() != self.my_region_list, "The list of partners has not changed"
            assert self.new_region_info_url in self.get_current_url(), "Url does not contain " \
                                                                    "information for the selected region"
            self.assert_title(self.new_region)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="check_new_region_url_title_list_partners")