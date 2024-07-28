import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from time import sleep

class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()
        driver.implicitly_wait(20)
    
    
    def test_search_ps4(self):
       
        driver = self.driver

        country = self.driver.find_element(By.ID, 'CO')
        country.click()

        sleep(1)

        search_field = driver.find_element(By.NAME, 'as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        
        sleep(1)

        location = driver.find_element(By.PARTIAL_LINK_TEXT, 'Bogotá D.C.')
        self.driver.execute_script("arguments[0].click();", location)

        sleep(1)

        condition = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo')
        self.driver.execute_script("arguments[0].click();", condition)

        sleep(1)


        order_menu = driver.find_element(By.CLASS_NAME, 'andes-dropdown__trigger')
        order_menu.click()
        higher_price = driver.find_element(By.CSS_SELECTOR, '#\:R2m55e6\:-menu-list-option-price_desc > div > div > span')
        higher_price.click()

        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element(By.CSS_SELECTOR, f'/html/body/main/div/div[3]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)

            article_price = driver.find_element(By.CSS_SELECTOR, f'/html/body/main/div/div[3]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]').text
            prices.append(article_price)

        print(articles, prices)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)