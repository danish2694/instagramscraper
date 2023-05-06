from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from csv import writer
import sys

class InstaScraper:
    def __init__(self, page):
        self.page = page
        self.domain = "https://www.instagram.com"
        self.set_options()
        self.driver = webdriver.Chrome(executable_path="chromedriver")

    def set_options(self):
        """
        Function to set any desired/required options to run chrome with
        params:
            None
        Returns:
            None
        """
        options = Options()
        options.headless = True
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")

    def csv_writer(file, row):
        """
        Function to append new row at the end of the csv file
        params:
            row -> (list) List of row items
        Returns:
            None
        """
        with open(file, 'a') as file_object:
            writer_object = writer(file_object)
            writer_object.writerow(row)
        
    def get_bs4_soup(self, url):
        """
        This function opens the instagram page in chrome, extracts the source code, generates bs4 object and returns it
        params:
            None
        Returns:
            BS4 soup object
        """
        self.driver.get(url)
        time.sleep(4)
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        return soup
    
    def collect_posts_links(self):
        """
        This function extracts every individual post's URL and saves it in a list
        this list is then used to extract post details like caption, image/video, date etc.
        params:
            None
        Returns:
            List of instagram page posts URLs
        """
        soup = self.get_bs4_soup(self.domain + "/"+ self.page +"/")
        script = soup.find_all("div", class_="_aabd")
        post_links = []
        for link in script:
            post_link = self.domain + link.find("a").get("href")
            post_links.append(post_link)
        return post_links
    
    def extract_post_details(self):
        with open('page_data.csv', 'w') as f:
            writer_object = writer(f)
            writer_object.writerow(["Video", "Image", "Caption", "PostTime"])

        post_links = self.collect_posts_links()
        for link in post_links:
            soup = self.get_bs4_soup(link)
            try:
                caption = soup.find("h1", class_="_aacl").text
            except Exception as e:
                caption = ""
            try:
                post_time = soup.find("time", class_="_a9ze").text
            except:
                post_time = ""
            
            try:
                video = soup.find("video", class_="x1lliihq").get("src")
            except:
                video = ""
            
            try:
                image = soup.find("img", class_="x5yr21d").get("src")
            except:
                image = ""
            self.csv_writer([image, video, caption, post_time])

try:
    page = sys.argv[1]
except:
    raise AssertionError("Please provide page name i.e. instagram")
scrape = InstaScraper(page)
posts = scrape.extract_post_details()
