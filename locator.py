from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class MainPageLocators(object):
# Search bar elements
    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc")
    SEARCH_FIELD_X = (By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.dRYYxd > div.BKRPef.M2vV3 > span.ExCKkf.z1asCe.rzyADb")
    SUGGESTIONS_BAR = (By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb")
    SEARCH_SUGGESTION = (By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.mkHrUc > ul.erkvQe > div > ul > li:nth-child(1)")
    LUCKY_BUTTON = (By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.RNmpXc")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "#search > div > h1")
    KEYBOARD_BUTTON = (By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.dRYYxd > div.Umvnrc")
    KEYBOARD = (By.ID, "kbd")

# Account page elements
    ACCOUNT_OVERVIEW = (By.ID, "overview")

# Main Google page top bar elements
    GMAIL_BUTTON = (By.CSS_SELECTOR, "#gb > div > div:nth-child(1) > div > div:nth-child(1) > a")
    GRAPHIC_BUTTON = (By.CSS_SELECTOR, "#gb > div > div:nth-child(1) > div > div:nth-child(2) > a")
    FUNCTION_BUTTON = (By.CSS_SELECTOR, "#gbwa > div > a > svg")
    DROP_DOWN_MENU = (By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > div > c-wiz > div > div > ul.LVal7b.u4RcUd")
    APPLICATION_BUBBLE = (By.CSS_SELECTOR, "body > div.gb_Oe")

# iFrame elements
    IFRAME = (By.XPATH, "//*[@id='gb']/div/div[3]/iframe")
    ACCOUNT_BUTTON_DROP_DOWN = (By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > div > c-wiz > div > div > ul.LVal7b.u4RcUd > li:nth-child(1) > a")



class SearchResultsPagesLocators(object):
    # Result page elements
    GRAPHICS_BUTTON = (By.CSS_SELECTOR, "#hdtb-msb > div > div > div > a > span > svg > path[d='M14 13l4 5H6l4-4 1.79 1.78L14 13zm-6.01-2.99A2 2 0 0 0 8 6a2 2 0 0 0-.01 4.01zM22 5v14a3 3 0 0 1-3 2.99H5c-1.64 0-3-1.36-3-3V5c0-1.64 1.36-3 3-3h14c1.65 0 3 1.36 3 3zm-2.01 0a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h7v-.01h7a1 1 0 0 0 1-1V5']")
    VIDEO_BUTTON = (By.CSS_SELECTOR, "#hdtb-msb > div > div > div > a > span > svg > path[d='M10 16.5l6-4.5-6-4.5v9zM5 20h14a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1zm14.5 2H5a3 3 0 0 1-3-3V4.4A2.4 2.4 0 0 1 4.4 2h15.2A2.4 2.4 0 0 1 22 4.4v15.1a2.5 2.5 0 0 1-2.5 2.5']")


    # Graphic page elements
    GRAPHIC_SEARCH_RESULT = (By.CSS_SELECTOR, "#islrg > div.islrc > div:nth-child(2)")
    GRAPHIC_DETAILS = (By.CSS_SELECTOR, "#Sva75c > div > div > div.pxAole")
    RELATED_IMAGE = (By.CSS_SELECTOR, "#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.QnfS4e.cZEg1e > div.X5SPld > c-wiz > div > div > div > div.l7VXJc.pZqGvd.sMVRZe > div:nth-child(1) > div:nth-child(1)")
    # Video page elements
    VIDEO_MINIATURE = (By.CSS_SELECTOR, "#rso > div > video-voyager > div > div > div > div.dXiKIc > a > div > div.z9RGvc")
    VIDEO_PREVIEW = (By.XPATH, '//div[@class="V1Ddwd"]/video')
