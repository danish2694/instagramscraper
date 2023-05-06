# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
# from bs4 import BeautifulSoup

# options = Options()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")

# driver = webdriver.Chrome(executable_path="chromedriver")

# driver.get("https://instagram.com/instagram/")
# time.sleep(3)
# soup = BeautifulSoup(driver.page_source, "html.parser")
# script = soup.find_all("div", class_="_aabd")
# links = []
# for link in script:
#     post_link = "https://www.instagram.com" + link.find("a").get("href")
#     links.append(post_link)

# print(driver.title)
# print(len(links), "posts found")

# for link in links:
#     driver.get(link)
#     time.sleep(5)
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     try:
#         caption = soup.find("h1", class_="_aacl").text
#     except Exception as e:
#         caption = ""
#     print(caption)
#     print()
#     print("------------------------------------------")

import csv
# Create the dictionary (=row)
# Open the CSV file in "append" mode
with open('my_file.csv', 'w') as f:
    writer_object = csv.writer(f)
    writer_object.writerow(["Video", "Image", "Caption", "PostTime"])
    # Create a dictionary writer with the dict keys as column fieldnames
    