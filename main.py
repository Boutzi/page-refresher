import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def refreshPage(driver):
    driver.refresh()
    return driver.page_source
  
def main():
  options = Options()
  options.add_argument("--headless")
  options.add_argument("--disable-gpu")
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  
  # Disable images
  # prefs = {"profile.managed_default_content_settings.images": 2}
  # options.add_experimental_option("prefs", prefs)

  caps = DesiredCapabilities().CHROME
  caps["pageLoadStrategy"] = "eager"

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  driver.get("https://your-website") # your website here

  try:
    while True:
      start_time = time.time()
      refreshPage(driver)
      end_time = time.time()
      print(f"Page refreshed in {end_time - start_time:.2f} seconds")
  finally:
    driver.quit()

if __name__ == "__main__":
  main()