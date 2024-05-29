import allure
from pages.sbis_contacts_page import SbisContactsPage
from pages.sbis_page import SbisPage


@allure.description("Test case 2")
def test_case_2(browser, set_up):
    sp = SbisPage(browser)
    sp.go_to_contacts_section()
    scp = SbisContactsPage(browser)
    scp.check_region_and_list_partners()
    scp.change_on_new_region()
    scp.check_new_region_url_title_list_partners()
