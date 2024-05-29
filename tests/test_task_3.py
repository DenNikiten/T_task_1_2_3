import allure
from pages.sbis_download_page import SbisDownloadPage
from pages.sbis_page import SbisPage


@allure.description("Test case 3")
def test_case_3(browser, set_up):
    sp = SbisPage(browser)
    sp.go_to_sbis_page()
    sp.find_and_go_to_download_sbis()
    sdp = SbisDownloadPage(browser)
    sdp.download_sbis_plugin_for_windows()
    sdp.check_download_file_in_directory()
    sdp.check_size_download_file_and_current_file_on_page()

