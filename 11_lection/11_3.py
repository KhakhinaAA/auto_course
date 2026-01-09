# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "/path/to/download/directory", "download.prompt_for_download": False, "download.directory_upgrade": True, }
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=options)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def set_chrome_download_path(download_path: str) -> webdriver.Chrome:
    """Configures Chrome to download files to the specified path.

    Args:
        download_path: The absolute path to the directory where files should be downloaded.

    Returns:
        A Chrome WebDriver instance configured with the specified download path.
    """
    chrome_options = Options()
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Пример использования
download_dir = os.path.abspath("downloads") # Абсолютный путь к папке downloads
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

driver = set_chrome_download_path(download_dir)
driver.get("https://www.thinkbroadband.com/download") # Сайт для теста скачивания

# Находим ссылку для скачивания и кликаем на нее (пример)
download_link = driver.find_element("xpath", "//a[contains(text(), '10MB')]" )
download_link.click()