from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
#options.headless = True
options.add_argument('--headless') #########
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/84.0.4147.89 Safari/537.36
detected_value = browser.find_element(By.ID, "detected_value")

"detected_value"
print(detected_value.text)
browser.quit()