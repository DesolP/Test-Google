from locator import *
from element import BasePageElement
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SearchTextElement(BasePageElement):
    locator = " "

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self, title):
        return title in self.driver.title

    def click_button(self, button):
        element = self.driver.find_element(*button)
        element.click()

    def is_element_visible(self, element):
        try:
            elem = self.driver.find_element(*element)
        except:
            return False
        else:
            return elem.is_displayed()

    def get_text_from_search_bar(self):
        text = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        return text.get_attribute("value")

    def check_application_bubble_visibility(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*MainPageLocators.FUNCTION_BUTTON)
        action.move_to_element(element)
        action.perform()
        time.sleep(1)
        element = self.driver.find_element(*MainPageLocators.APPLICATION_BUBBLE)
        return element.is_displayed()

    def switch_to_iframe(self):
        iframe = self.driver.find_element(*MainPageLocators.IFRAME)
        self.driver.switch_to.frame(iframe)




class SearchResultsPage(BasePage):

    def is_result_found(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'OotqVd')))
        except:
            return True
        else:
            return False

    def is_element_type_found(self, search):
        return search in self.driver.page_source

    def is_video_preview_available(self, video):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*video)
        action.move_to_element(element)
        action.perform()
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="V1Ddwd"]/video')))
        except:
            return False
        else:
            return True

    def is_video_preview_running(self, video):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*video)
        action.move_to_element(element)
        action.perform()
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="V1Ddwd"]/video')))
        except:
            return False
        else:
            action.move_to_element(self.driver.find_element(*MainPageLocators.SEARCH_FIELD))
            action.perform()
            time.sleep(1)
            stateNotPointed = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="V1Ddwd"]/video'))).get_attribute("style")
            print(stateNotPointed)
            action.move_to_element(element)
            action.perform()
            statePointed = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="V1Ddwd"]/video'))).get_attribute("style")
            print(statePointed)
            return not stateNotPointed == statePointed

    def click_parent_element(self, button):
        element = self.driver.find_element(*button)
        clickable_element = element.find_element(By.XPATH, "..")
        clickable_element.click()