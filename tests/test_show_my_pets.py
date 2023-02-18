# cd tests
# python -m pytest -v --driver chrome --driver-path /test/chrom test_show_my_pets.py
import pytest
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./test/chrom')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   '''Проверяем что мы оказались на странице "Мои питомцы"'''
   # Устанавливаем явное ожидание
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   pytest.driver.find_element(By.ID,'email').send_keys(valid_email)
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element (By.CSS_SELECTOR,'button[type="submit"]').click()
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))

   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element (By.TAG_NAME,'h1').text == "PetFriends"

