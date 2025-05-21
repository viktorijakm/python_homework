from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time
import os

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

PAUSE_TIME = 2

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)
time.sleep(PAUSE_TIME)


# Replace 'cp-search-result-item' with the actual class you found in the <li>
results_li = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")

print(f"Found {len(results_li)} search results.")

results = []

for item in results_li:
    try:
        # Get title
        title_elem = item.find_element(By.CSS_SELECTOR, "h2.cp-title span.title-content")  # Adjust class if needed
        title = title_elem.text.strip()

        # Get authors (could be more than one)
        author_elems = item.find_elements(By.CSS_SELECTOR, "span.cp-by-author-block a.author-link")  # Adjust class if needed
        authors = "; ".join([author.text.strip() for author in author_elems if author.text.strip()])

        format_div = item.find_element(By.CSS_SELECTOR, "div.cp-format-info")
        format_year_elem = item.find_element(By.CSS_SELECTOR, "span.display-info-primary")  # Parent div
        format_year = format_year_elem.text.strip()

        # Append the book data
        results.append({
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        })

    except Exception as e:
        print(f"Skipping one result due to error: {e}")

# Create and print DataFrame
df = pd.DataFrame(results)
print(df)


# Save DataFrame to CSV
csv_path = "get_books.csv"
df.to_csv(csv_path, index=False, encoding="utf-8")
print(f"Saved {len(results)} records to {csv_path}")

# Save to JSON
json_path = "get_books.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"Saved JSON data to {json_path}")

# Close the browser
driver.quit()





#<li class="row cp-search-result-item" data-test-id="searchResultItem" style="/* order:0; */" data-key="search-result-item"><div class="col-md-2 visible-md visible-lg item-column"><a href="/item/show/18011361981" tabindex="-1" aria-hidden="true" target="_parent" data-key="bib-image-link"><img alt="Real-World Spanish: The Conversation Learning System - Camila Vega Rivera" src="https://cover.hoopladigital.com/dvf_9798347721009_270.jpeg" class="cp-jacket-cover img-responsive" loading="lazy"></a></div><div class="col-md-10 item-column"><div class="cp-search-result-item-content"><div class="cp-search-result-item-info"><div class="jacket-cover-wrap hidden-md hidden-lg"><a href="/item/show/18011361981" title="Real-World Spanish: The Conversation Learning System" target="_parent"><img alt="Real-World Spanish: The Conversation Learning System - Camila Vega Rivera" src="https://cover.hoopladigital.com/dvf_9798347721009_270.jpeg" class="cp-jacket-cover" loading="lazy"></a></div><div><div class="cp-deprecated-bib-brief"><h2 class="cp-title"><a href="/item/show/18011361981" target="_parent" lang="en" rel="noopener" data-test-id="bib-title-S981C18011361" data-key="bib-title"><span aria-hidden="true" class="title-content">Real-World Spanish: The Conversation Learning System</span><span class="cp-screen-reader-message">Real-World Spanish: The Conversation Learning System, eAudiobook</span></a></h2><span class="cp-by-author-block --block">by <span class="cp-author-link"><span><a target="_parent" rel="noopener noreferrer" class="author-link" data-key="author-link" href="/v2/search?origin=core-catalog-explore&amp;query=Camila%20Vega%20Rivera&amp;searchType=author">Camila Vega Rivera</a></span></span></span></div></div></div><div class="info"><div class="row"><div class="col-12 col-xs-12 availability_status"><div class="cp-manifestation-list"><div class="manifestation-item cp-manifestation-list-item row"><div class="manifestation-item-format-call-wrap available"><div class="manifestation-item-format-call-wrap-inner"><svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" class="cp-svg icon-svg-audiobook icon" height="24" viewBox="0 0 24 24" width="24"><path fill="currentColor" fill-rule="evenodd" clip-rule="evenodd" d="M12 2C7.03 2 3 6.03 3 11V18C3 19.66 4.34 21 6 21H9V13H5V11C5 7.13 8.13 4 12 4C15.87 4 19 7.13 19 11V13H15V21H18C19.66 21 21 19.66 21 18V11C21 6.03 16.97 2 12 2Z"></path></svg><div class="manifestation-item-format-info-wrap"><a class="manifestation-item-link" href="/item/show/18011361981" target="_parent" lang="en" rel="noopener" data-test-id="item-link-S981C18011361" data-key="bib-manifestation-item-link"><div class="cp-format-info"><span aria-hidden="true" class="display-info"><span class="display-info-primary">eAudiobook<!-- --> - 2025</span><span class="call-number"></span></span><span class="cp-screen-reader-message">eAudiobook, 2025</span></div></a><div class="manifestation-item-availability-block-wrap"><a href="https://www.hoopladigital.com/title/18011361" rel="noopener noreferrer" target="_blank"><span aria-hidden="true">Check out now on Hoopla<!-- --> <svg focusable="false" aria-hidden="true" class="icon-svg-new-tab " width="16" height="16" viewBox="0 0 16 16"><path fill="currentColor" d="M11 13h-8v-8h4.5l2-2h-8.5v12h12v-8.5l-2 2v4.5z"></path><path fill="currentColor" d="M16 0h-6.5l2.5 2.5-7.5 7.5 1.5 1.5 7.5-7.5 2.5 2.5v-6.5z"></path></svg></span><span class="cp-screen-reader-message">Check out now on Hoopla, opens a new window</span></a></div></div></div></div><div class="manifestation-item-action-toggle hidden-sm hidden-md hidden-lg visible-xs toggled-open"><button class="cp-btn btn cp-text-btn " id="manifestation-item-action-wrap-S981C18011361" aria-expanded="true"><svg focusable="false" aria-hidden="true" class="icon-svg-more undefined" width="20" height="20" viewBox="0 0 16 16" version="1.1"><title></title><path fill="#02729e" d="M6 1h4v4h-4zM6 6h4v4h-4zM6 11h4v4h-4z"></path></svg><span class="cp-screen-reader-message">Toggle transaction button drawer</span></button></div><div class="manifestation-item-action-wrap toggled-open"><div class="add-to-shelf-wrap"><div class="cp-add-to-shelf-combo-button"><div class="cp-combo-btn btn-group "><button class="cp-btn btn cp-default-btn btn-default "><span><svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" class="cp-svg icon-svg-shelves-outline" height="24" viewBox="0 0 24 24" width="24"><path fill="currentColor" fill-rule="evenodd" d="M17,3 L7,3 C5.9,3 5,3.9 5,5 L5,21 L12,18 L19,21 L19,5 C19,3.9 18.1,3 17,3 Z M17,18 L12,15.82 L7,18 L7,5 L17,5 L17,18 Z"></path></svg><span class="shelf-name-text" aria-hidden="true">For Later</span><span class="cp-screen-reader-message">Add <!-- -->Real-World Spanish: The Conversation Learning System, eAudiobook, by Camila Vega Rivera<!-- --> to your for later shelf</span></span></button><div class="cp-popup-manager cp-dropdown" data-key="combo-button-dropdown"><div class="trigger-wrapper"><button class="cp-btn btn cp-default-btn btn-default cp-dropdown-trigger btn-default" aria-hidden="false" tabindex="0" type="button" aria-haspopup="true" aria-expanded="false"><span class="selected-wrapper"><span class="selected-value"><span class="cp-screen-reader-message">Add <!-- -->Real-World Spanish: The Conversation Learning System, eAudiobook, by Camila Vega Rivera<!-- --> to a different shelf</span></span><svg focusable="false" aria-hidden="true" class="icon-svg-arrow-medium-down selected-icon extra-small" width="16" height="16" viewBox="0 0 18 16"><path fill="#000" d="M16 5.5l-2-2-6 6-6-6-2 2 8 8 8-8z"></path></svg></span></button></div></div></div></div></div></div></div></div></div></div></div></div></div></li>   

  #  <span aria-hidden="true" class="title-content">Real-World Spanish: The Conversation Learning System</span>

    #<span class="cp-by-author-block --block">by <span class="cp-author-link"><span><a target="_parent" rel="noopener noreferrer" class="author-link" data-key="author-link" href="/v2/search?origin=core-catalog-explore&amp;query=Camila%20Vega%20Rivera&amp;searchType=author">Camila Vega Rivera</a></span></span></span>

  #<h2 class="cp-title"><a href="/item/show/18011361981" target="_parent" lang="en" rel="noopener" data-test-id="bib-title-S981C18011361" data-key="bib-title"><span aria-hidden="true" class="title-content">Real-World Spanish: The Conversation Learning System</span><span class="cp-screen-reader-message">Real-World Spanish: The Conversation Learning System, eAudiobook</span></a></h2>

