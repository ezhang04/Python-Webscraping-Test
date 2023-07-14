from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

search_term = input("Enter the item you want to search on Amazon: ")
url = f"https://www.amazon.com/s?k={search_term.replace(' ', '+')}"

soup = BeautifulSoup(driver.page_source, 'lxml')

while True:
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    product_titles = soup.select('.a-size-medium.a-text-normal')
    product_prices_whole = soup.select('.a-price-whole')
    product_prices_fractional = soup.select('.a-price-fraction')

    for title, price_whole, price_fractional in zip(product_titles, product_prices_whole, product_prices_fractional):
        price = f"{price_whole.text}{price_fractional.text}"
        print()
        print(f"{title.text}: ${price}")

    next_button = driver.find_elements(By.CSS_SELECTOR,'.s-pagination-container .s-pagination-next')
    if next_button:
        next_button[0].click()
        url = driver.current_url
    else:
        break 

driver.quit()