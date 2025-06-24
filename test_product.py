from selenium import webdriver
from selenium.webdriver.common.by import By

def test_product_card():
    driver = webdriver.Chrome()
    driver.get("https://vk.com/club225299895?w=product-225299895_10044406")

    # 1. Наличие элементов карточки
    assert driver.find_element(By.CSS_SELECTOR, ".product-name").is_displayed()
    # 2. Цена
    assert driver.find_element(By.CLASS_NAME, "price").text != ""
    # 3. Кнопка "Купить"
    assert driver.find_element(By.ID, "buy-button").is_enabled()
    
    driver.quit()
