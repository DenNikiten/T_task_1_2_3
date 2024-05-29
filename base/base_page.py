import datetime
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    """Method of going to the site"""

    def go_to_site(self, base_url):
        self.driver.get(base_url)

    """Methods for finding elements"""

    def element_is_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    """Method wait until text to be present in element"""

    def text_is_present_in_element(self, locator, region, timeout=10):
        return Wait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, region))

    """Method wait until url contains text"""

    def text_contains_in_url(self, text, timeout=15):
        return Wait(self.driver, timeout).until(EC.url_contains(text))

    """Method element visible"""

    def is_element_exist(self, locator, timeout=5):
        element = Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return bool(element)

    """Method displayed element"""

    def element_is_displayed(self, locator):
        get_element = self.element_is_present(locator)
        get_element.is_displayed()
        print("Element is displayed")

    """Method get text"""

    def get_text(self, element):
        get_text = element.text
        print(f"Current text: {get_text}")
        return get_text

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")
        return get_url

    """Method switch to window"""

    def switch_window(self, num_window):
        self.driver.switch_to.window(self.driver.window_handles[num_window])

    """Method move to element"""

    def action_move_to(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f"True value url: {get_url}"), f"Url does not match. Expected: {result}, Actual: {get_url}"

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("True value word"), f"Word does not match. Expected: {result}, Actual: {value_word}"

    """Method assert title"""

    def assert_title(self, result):
        title = self.driver.title
        assert result in title
        print("True value title"), f"Title does not match. Expected {result} in {title}"

    """Method assert file in directory"""

    def assert_file_in_directory(self, download_dir, file_name):
        file_path = download_dir + file_name
        assert os.access(file_path, os.F_OK) == True, "The file has not been downloaded"
        print("Required file in directory")

    """Method of comparing the size of a downloaded file with the current one on the site"""

    def assert_file_size(self, download_dir, file_name, size_current_file):
        file_path = download_dir + file_name
        size_download_file = f"{round(os.path.getsize(file_path) / (1024 * 1024), 2)} МБ"
        assert size_download_file in size_current_file, f"File size doesn't match. " \
                                                        f"Expected {size_download_file} in {size_current_file}"

    """Method for deleting a file from a directory"""

    def remove_file(self, download_dir):
        os.remove(download_dir)

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = f"screenshot_{now_date}.png"
        path = '.\\screen\\'
        self.driver.save_screenshot(path + name_screenshot)


