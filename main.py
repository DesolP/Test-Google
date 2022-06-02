import unittest
from selenium import webdriver
import page
import time
from locator import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.google.com/")

        try:
            button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "L2AGLb")))
            button.click()
        except:
            True


    def test_title(self):
        print("Running test: test_title")
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches("Google")

    def test_search_bar(self):
         print("Running test: test_search_bar")
         mainPage = page.MainPage(self.driver)
         page.SearchTextElement.locator = "q"
         search = "test"
         mainPage.search_text_element = search
         try:
            mainPage.click_button((MainPageLocators.SEARCH_BUTTON))
         except:
             assert False, "SEARCH_BUTTON button not found."

         WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.ID, "gsr")))
         search_result_page = page.SearchResultPage(self.driver)
         assert search_result_page.is_result_found(search)

    def test_search_bar_clear_button(self):
        print("Running test: test_search_bar")
        mainPage = page.MainPage(self.driver)
        page.SearchTextElement.locator = "q"
        search = "test"
        mainPage.search_text_element = search
        time.sleep(1)
        try:
            mainPage.click_button((MainPageLocators.SEARCH_FIELD_X))
        except:
            assert False, "SEARCH_FIELD_X button not found."
        assert not mainPage.get_text_from_search_bar()

    def test_search_bar_suggestions_visible(self):
        print("Running test: test_search_bar_suggestions_visible")
        mainPage = page.MainPage(self.driver)
        page.SearchTextElement.locator = "q"
        search = "test"
        mainPage.search_text_element = search
        mainPage.click_button((MainPageLocators.SEARCH_FIELD))
        time.sleep(1)
        assert mainPage.is_element_visible((MainPageLocators.SUGGESTIONS_BAR))

    def test_click_search_suggestion(self):
        print("Running test: test_click_search_suggestion")
        mainPage = page.MainPage(self.driver)
        page.SearchTextElement.locator = "q"
        search = "test"
        mainPage.search_text_element = search
        mainPage.click_button((MainPageLocators.SEARCH_FIELD))
        time.sleep(1)
        if mainPage.is_element_visible((MainPageLocators.SUGGESTIONS_BAR)) == True:
            mainPage.click_button((MainPageLocators.SEARCH_SUGGESTION))
        else:
            assert False, "SUGGESTIONS_BAR bar not visible"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "gsr")))
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found(search)

    def test_empty_search_bar(self):
         print("Running test: test_empty_search_bar")
         mainPage = page.MainPage(self.driver)
         page.SearchTextElement.locator = "q"
         search = ""
         mainPage.search_text_element = search
         try:
             mainPage.click_button((MainPageLocators.SEARCH_BUTTON))
         except:
             assert False, "SEARCH_BUTTON button not found."
         assert mainPage.is_title_matches("Google")

    def test_invisible_keyboard(self):
        print("Running test: test_invisible_keyboard")
        mainPage = page.MainPage(self.driver)
        try:
            mainPage.click_button((MainPageLocators.KEYBOARD_BUTTON))
        except:
            assert False, "KEYBOARD_BUTTON not found."
        time.sleep(1)
        assert mainPage.is_element_visible((MainPageLocators.KEYBOARD))

    def test_graphics_page(self):
        print("Running test: test_graphics_page")
        mainPage = page.MainPage(self.driver)
        page.SearchTextElement.locator = "q"
        search = "test"
        mainPage.search_text_element = search
        try:
            mainPage.click_button((MainPageLocators.SEARCH_BUTTON))
        except:
            assert False, "SEARCH_BUTTON button not found."
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "gsr")))
        try:
            mainPage.click_parent_element((SearchResultsPagesLocators.GRAPHICS_BUTTON))
        except:
            assert False, "GRAPHICS_BUTTON button not found."
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "islmp")))
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found(".jpeg")

    def test_show_graphic_details(self):
        print("Running test: test_graphics_page")
        mainPage = page.MainPage(self.driver)
        page.SearchTextElement.locator = "q"
        search = "test"
        mainPage.search_text_element = search
        try:
            mainPage.click_button((MainPageLocators.SEARCH_BUTTON))
        except:
            assert False, "SEARCH_BUTTON button not found."
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "gsr")))
        try:
            mainPage.click_parent_element((SearchResultsPagesLocators.GRAPHICS_BUTTON))
        except:
            assert False, "GRAPHICS_BUTTON button not found."
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "islmp")))
        try:
            mainPage.click_button((SearchResultsPagesLocators.GRAPHIC_SEARCH_RESULT))
        except:
            assert False, "GRAPHIC_SEARCH_RESULT button not found."
        assert mainPage.is_element_visible((SearchResultsPagesLocators.GRAPHIC_DETAILS))

    def test_related_images(self):
        print("Running test: test_graphics_page")
        mainPage = page.MainPage(self.driver)
        page.SearchTextElement.locator = "q"
        search = "test"
        mainPage.search_text_element = search
        try:
            mainPage.click_button((MainPageLocators.SEARCH_BUTTON))
        except:
            assert False, "SEARCH_BUTTON button not found."
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "gsr")))
        try:
            mainPage.click_parent_element((SearchResultsPagesLocators.GRAPHICS_BUTTON))
        except:
            assert False, "GRAPHICS_BUTTON button not found."
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "islmp")))
        try:
            mainPage.click_button((SearchResultsPagesLocators.GRAPHIC_SEARCH_RESULT))
        except:
            assert False, "GRAPHIC_SEARCH_RESULT button not found."
        try:
            mainPage.is_element_visible((SearchResultsPagesLocators.GRAPHIC_DETAILS))
        except:
            assert False, "GRAPHIC_DETAILS button not found."
        time.sleep(1)
        assert mainPage.is_element_visible((SearchResultsPagesLocators.RELATED_IMAGE))

    def test_video_preview(self):
        print("Running test: test_video_preview")
        mainPage = page.MainPage(self.driver)
        page.SearchTextElement.locator = "q"
        search = "test"
        mainPage.search_text_element = search
        try:
            mainPage.click_button((MainPageLocators.SEARCH_BUTTON))
        except:
            assert False, "SEARCH_BUTTON button not found."
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "gsr")))
        try:
            mainPage.click_parent_element((SearchResultsPagesLocators.VIDEO_BUTTON))
        except:
            assert False, "VIDEO_BUTTON button not found."
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "rso")))
        assert mainPage.is_video_preview_available((SearchResultsPagesLocators.VIDEO_MINIATURE))

    def test_video_preview_running(self):
        print("Running test: test_video_preview")
        mainPage = page.MainPage(self.driver)
        page.SearchTextElement.locator = "q"
        search = "test"
        mainPage.search_text_element = search
        try:
            mainPage.click_button((MainPageLocators.SEARCH_BUTTON))
        except:
            assert False, "SEARCH_BUTTON button not found."
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "gsr")))
        try:
            mainPage.click_parent_element((SearchResultsPagesLocators.VIDEO_BUTTON))
        except:
            assert False, "VIDEO_BUTTON button not found."
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "rso")))
        assert mainPage.is_video_preview_running((SearchResultsPagesLocators.VIDEO_MINIATURE))

    def test_drop_down_menu(self):
        print("Running test: test_function_button")
        mainPage = page.MainPage(self.driver)
        mainPage.click_button((MainPageLocators.FUNCTION_BUTTON))
        mainPage.switch_to_iframe()
        assert mainPage.is_element_visible((MainPageLocators.DROP_DOWN_MENU))

    def test_account_button_in_drop_down(self):
        print("Running test: test_account_button_drop_down")
        mainPage = page.MainPage(self.driver)
        mainPage.click_button((MainPageLocators.FUNCTION_BUTTON))
        mainPage.switch_to_iframe()
        mainPage.click_button((MainPageLocators.ACCOUNT_BUTTON_DROP_DOWN))
        assert mainPage.is_element_visible((MainPageLocators.ACCOUNT_OVERVIEW))

    def test_application_bubble_visibility(self):
        print("Running test: test_dymek")
        mainPage = page.MainPage(self.driver)
        assert mainPage.check_application_bubble_visibility()


    def test_lucky_button(self):
        print("Running test: test_lucky_button")
        mainPage = page.MainPage(self.driver)
        mainPage.click_button((MainPageLocators.LUCKY_BUTTON))
        search_result_page = page.SearchResultPage(self.driver)
        assert mainPage.is_title_matches("Doodle")

    def tearDown(self):
        time.sleep(1)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
