import allure
from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_page import SbisPage
from pages.tensor_about_page import TensorAboutPage
from pages.tensor_page import TensorPage


@allure.description("Test case 1")
def test_case_1(browser, set_up):
    sp = SbisPage(browser)
    sp.go_to_contacts_section()
    scp = SbisContactsPage(browser)
    scp.select_banner_tensor()
    scp.switch_to_window_tensor()
    tp = TensorPage(browser)
    tp.check_block_strength_in_people()
    tp.select_more_details_and_check_page_tensor_about_is_open()
    tap = TensorAboutPage(browser)
    tap.check_same_height_and_width()