import time
from pynput import keyboard
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = "https://github.com/Boutzi" # your website here

stop = False

def on_press(key):
    global stop
    if key == keyboard.Key.esc:  
        stop = True
        return False

def refreshPage(driver):
    driver.refresh()
    return driver.page_source
  
def main():
  global stop
  options = Options()
  options.add_argument("--headless")
  options.add_argument("--disable-gpu")
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  
  user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
  options.add_argument(f"user-agent={user_agent}")
  
  # Disable images to speed up the process by uncommenting the following lines
  # prefs = {"profile.managed_default_content_settings.images": 2}
  # options.add_experimental_option("prefs", prefs)

  caps = DesiredCapabilities().CHROME
  caps["pageLoadStrategy"] = "eager"

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  driver.get(url)

  listener = keyboard.Listener(on_press=on_press)
  listener.start()

  print(f'{"\033[31m"}Press "Esc" to stop the script\n{"\033[0m"}')

  try:
    while not stop:
      start_time = time.time()
      refreshPage(driver)
      end_time = time.time()
      print(f"Page refreshed in {end_time - start_time:.2f} seconds")
  finally:
    listener.stop()
    driver.quit()

if __name__ == "__main__":
  main()