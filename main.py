from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re
import pandas as pd

def scrapeBooks(headless = True):
    try:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        url = "https://books.toscrape.com"
        books = {
            "title": [],
            "category": [],
            "rating": [],
            "price": [],
            "stock": [],
            "description": [],
        }
        driver.get(url)
        driver.implicitly_wait(5)
        RATINGS = ["one", "two", "three", "four", "five"]
        bookElements = driver.find_elements(By.XPATH, '//ol/li')
        for index in range(1, len(bookElements) + 1):
            print(f'[{index} of {len(bookElements)} books] Scraping...')
            element = driver.find_element(By.XPATH, f'//ol/li[{index}]//h3/a')
            element.click()
            title = driver.find_element(By.XPATH, '//h1').text
            category = driver.find_element(By.XPATH, '//li[3]/a').text
            rating = driver.find_element(By.XPATH, '//p[contains(@class, "star-rating")]')
            rating = rating.get_attribute('class').split()[-1].lower()
            rating = RATINGS.index(rating) + 1
            price = driver.find_element(By.XPATH, '//p[@class="price_color"]').text
            stock = driver.find_element(By.XPATH, '//p[@class="instock availability"]').text
            stock = re.findall(r'\d+', stock)[0]
            description = driver.find_element(By.XPATH, '//*[@id="content_inner"]/article/p').text
            books["title"].append(title)
            books["category"].append(category)
            books["rating"].append(rating)
            books["price"].append(price)
            books["stock"].append(stock)
            books["description"].append(description)
            driver.back()
    except Exception as ex:
        print(ex)
    finally:
        driver.quit()
        return books

if __name__ == '__main__':
    b = scrapeBooks(False)
    df = pd.DataFrame(b)
    df.to_csv('data.csv')