from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def get_crypto_data(headless=True):

    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless")

    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get("https://coinmarketcap.com/")

    time.sleep(5)

    rows = driver.find_elements(
        By.CSS_SELECTOR,
        "table tbody tr"
    )

    crypto_data = []

    for row in rows[:10]:

        try:
            columns = row.find_elements(
                By.TAG_NAME,
                "td"
            )

            name = columns[2].text
            price = columns[3].text
            change_24h = columns[4].text
            market_cap = columns[7].text

            crypto_data.append({
                "Name": name,
                "Price": price,
                "24h Change": change_24h,
                "Market Cap": market_cap
            })

        except Exception as e:
            print("Error:", e)

    driver.quit()

    return crypto_data