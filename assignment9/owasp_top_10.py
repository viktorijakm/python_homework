from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import os
import time

# Set up headless browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://owasp.org/www-project-top-ten/"
driver.get(url)
time.sleep(3)  # Wait for page to load

# Get <li> elements that have an <a> tag pointing to a Top10 item
top_10_elements = driver.find_elements(By.XPATH, "//li[a[strong and contains(@href, '/Top10/')]]")

top_10 = []

for item in top_10_elements:
    try:
        a_tag = item.find_element(By.TAG_NAME, "a")
        title = a_tag.text.strip()
        href = a_tag.get_attribute("href").strip()

        if title and href:
            top_10.append({
                "Title": title,
                "Link": href
            })
    except Exception as e:
        print(f"Error: {e}")

driver.quit()

# Save results to CSV
df = pd.DataFrame(top_10)
csv_path = "owasp_top_10.csv"
df.to_csv(csv_path, index=False, encoding='utf-8')
print(f"\n Successfully saved {len(top_10)} items to: {csv_path}")

