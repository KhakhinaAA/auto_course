# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
from pathlib import Path

options = Options()

options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2,  # disable all notice
    "profile.default_content_setting_values.media_stream_mic": 2,  # disable microphone
    "profile.default_content_setting_values.media_stream_camera": 2,  # disable camera
    "profile.default_content_setting_values.geolocation": 2,  # disable geolocations
})

driver = webdriver.Chrome(options=options)

sbis_site = 'https://sbis.ru/'


try:

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

        drivers = webdriver.Chrome(options=chrome_options)

        return drivers

    # Абсолютный путь к папке downloads
    download_dir = os.path.abspath("11_lection")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Перейти на  https://sbis.ru/
    driver = set_chrome_download_path(download_dir)
    driver.get(sbis_site)
    driver.maximize_window()

    # В Footer'e найти "Скачать СБИС"
    footer_downoload = driver.find_element(By.CSS_SELECTOR,
                                           ".sbisru-Footer__list--hidden [href=\"/download\"]")
    footer_downoload.click()

    # Скачать СБИС Плагин для вашей ОС в папку с данным тестом
    downaload = driver.find_element(By.CSS_SELECTOR,
                                    '[href="https://update.saby.ru/SabyDesktop/master/win32/saby-setup.exe"]'
                                    ' .controls-Button__text')
    downaload.click()

    sleep(4)

    # Убедиться, что плагин скачался
    download_dir = "C:/Users/user/project_auto/11_lection/11_lection/"
    download_file = "saby-setup.exe"  # Имя скаченного файла
    file_path = os.path.join(download_dir, download_file)
    # Ждём, пока файл скачается (максимум 10 секунд)
    if os.path.exists(file_path):
        print("Файл успешно скачан!")
        sleep(1)  # ожидаем 1 секунду
    else:
        print("Файл не был скачан.")

    # Вывести на печать размер скачанного файла в мегабайтах
    file_path = Path("C:/Users/user/project_auto/11_lection/11_lection/saby-setup.exe")
    size_in_bytes = file_path.stat().st_size
    size_in_mb = size_in_bytes * 0.000001
    print(f"Размер файла: {size_in_mb} мегабайт")
finally:
    # Удаление скачанного файла на случай падения
    file_path = Path("C:/Users/user/project_auto/11_lection/11_lection/saby-setup.exe")
    while os.path.exists(file_path):
        os.remove(file_path)

    driver.quit()
