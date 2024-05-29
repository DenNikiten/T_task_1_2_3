import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.logger import Logger


class TensorAboutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.section_working = (By.CLASS_NAME, "tensor_ru-About__block3")
        self.images_block_working = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image.new_lazy.loaded")

    # Getters

    def get_section_working(self):
        return self.element_is_visible(self.section_working)

    def get_img_elements(self):
        return self.elements_are_visible(self.images_block_working)

    def get_width(self):
        width = [item.get_attribute("width") for item in self.get_img_elements()]
        return width

    def get_height(self):
        height = [item.get_attribute("height") for item in self.get_img_elements()]
        return height

        # Check

    def is_section_working_exist(self):
        return self.is_element_exist(self.section_working)

    def same_height_and_width(self):
        return len(set(self.get_width())), len(set(self.get_height()))

    # Actions

    def action_move_to_section_working(self):
        self.action_move_to(self.get_section_working())
        print("Action move to section working")

    # Method

    def check_same_height_and_width(self):
        with allure.step("Check the same height and width"):
            Logger.add_start_step(method="check_same_height_and_width")
            self.is_section_working_exist()
            self.action_move_to_section_working()
            assert self.same_height_and_width() == (1, 1), "Photos are not the same height and width"
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="check_same_height_and_width")

