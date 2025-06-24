def test_community_page():
    driver = webdriver.Chrome()
    driver.get("https://vk.com/club225299895?w=product-225299895_10044406")

    # 1. Заголовок сообщества
    assert "Название сообщества" in driver.title
    # 2. Список участников
    assert len(driver.find_elements(By.CLASS_NAME, "member")) > 0
    # 3. Кнопка "Присоединиться"
    assert driver.find_element(By.XPATH, "//button[contains(text(),'Присоединиться')]")
    
    driver.quit()
