import os
import time
import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.logger import Logger


class SbisDownloadPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.download_dir = os.getcwd() + "\\tests\\downloads\\"
        self.web_installer = "sbisplugin-setup-web.exe"
        self.sbis_download_page_url_text_plugin = "tab=plugin"
        self.sbis_plugin_tab_btn = (By.CSS_SELECTOR, "[data-id='plugin'] > div:last-child")
        self.download_web_installer_link = (By.PARTIAL_LINK_TEXT, "Скачать (Exe")

    """Method of waiting until the file is downloaded"""

    def is_file_downloaded(self, download_dir, file_name, attempts=20):
        file_path = download_dir + file_name
        while attempts > 0:
            if os.path.exists(file_path):
                print("File Downloaded Successfully..")
                break
            time.sleep(1)
            attempts -= 1

    """Method add missing support for chrome "send_command"  to selenium webdriver"""

    def enable_download_in_chrome(self, download_dir):
        self.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        self.driver.execute("send_command", params)

    # Getters

    def get_sbis_plugin(self):
        return self.element_is_present(self.sbis_plugin_tab_btn)

    def get_download_web_installer(self):
        return self.element_is_visible(self.download_web_installer_link)

    def get_text_downloaded_file(self):
        return self.get_text(self.get_download_web_installer())

    # Actions

    def click_sbis_plugin(self):
        self.get_sbis_plugin().click()
        print("Click sbis plugin")

    def click_download_web_installer(self):
        self.get_download_web_installer().click()
        print("Click download web installer")

    # Check

    # Methods

    def download_sbis_plugin_for_windows(self):
        with allure.step("Download sbis plugin for windows"):
            Logger.add_start_step(method="download_sbis_plugin_for_windows")
            self.click_sbis_plugin()
            self.text_contains_in_url(self.sbis_download_page_url_text_plugin)
            self.enable_download_in_chrome(self.download_dir)
            self.click_download_web_installer()
            self.is_file_downloaded(self.download_dir, self.web_installer)
            Logger.add_end_step(url=self.driver.current_url, method="download_sbis_plugin_for_windows")

    def check_download_file_in_directory(self):
        with allure.step("Check download file in directory"):
            Logger.add_start_step(method="download_file_in_directory")
            self.assert_file_in_directory(self.download_dir, self.web_installer)
            Logger.add_end_step(url=self.driver.current_url, method="download_file_in_directory")

    def check_size_download_file_and_current_file_on_page(self):
        with allure.step("Check size download file and current file on page"):
            Logger.add_start_step(method="check_size_download_file_and_current_file_on_page")
            self.assert_file_size(self.download_dir, self.web_installer, self.get_text_downloaded_file())
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="check_size_download_file_and_current_file_on_page")
