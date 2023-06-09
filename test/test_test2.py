# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_test2(self):
    self.driver.get("http://localhost:3000/")
    self.driver.set_window_size(786, 824)
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".group:nth-child(1) .inline-block").click()
    self.vars["win4664"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win4664"])
    self.driver.switch_to.window(self.vars["root"])
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".group:nth-child(3) > .mb-3").click()
    self.vars["win7901"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win7901"])
    element = self.driver.find_element(By.CSS_SELECTOR, ".card_card__ydZD_:nth-child(1) .card_demo-link__htT6e")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".card_card__ydZD_:nth-child(1) > .card_card-content__P_nI_ svg")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.LINK_TEXT, "CSS Modules")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.switch_to.window(self.vars["root"])
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".group:nth-child(4) > .mb-3").click()
    self.vars["win3798"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win3798"])
    self.driver.find_element(By.CSS_SELECTOR, ".list_geistListItem__82_ac:nth-child(4) .geist-ellipsis").click()
    self.driver.execute_script("window.scrollTo(0,0)")
  
