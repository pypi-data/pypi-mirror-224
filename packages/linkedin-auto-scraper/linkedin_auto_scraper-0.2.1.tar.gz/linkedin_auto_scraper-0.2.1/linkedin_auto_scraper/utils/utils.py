import json
import os
import re
import time
from dataclasses import dataclass
from typing import List, Optional

import pandas as pd
from fake_useragent import UserAgent
from pydantic import EmailStr
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def get_user_agent():
    return UserAgent().random


@dataclass
class Scraper:
    driver: webdriver = None

    def __get_driver(self):
        if self.driver is None:
            user_agent = get_user_agent()
            options = Options()
            options.add_argument("--no-sandbox")
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument(f"user-agent={user_agent}")
            options.add_argument("--start-maximized")
            options.add_experimental_option(
                "excludeSwitches", ["enable-logging"]
            )
            options.add_experimental_option(
                "excludeSwitches", ["enable-automation"]
            )
            options.add_experimental_option("useAutomationExtension", False)
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options,
            )
            self.driver = driver
        return self.driver

    def quit_driver(self):
        driver = self.__get_driver()
        return driver.quit()

    def linkedin_login(self, email: EmailStr, password: str):
        driver = self.__get_driver()
        driver.get(url="https://www.linkedin.com/login")
        time.sleep(1)
        email_field = driver.find_element(by=By.ID, value="username")
        password_field = driver.find_element(by=By.ID, value="password")
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button = driver.find_element(
            by=By.XPATH,
            value='//button[@data-litms-control-urn="login-submit"]',
        )
        login_button.click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "global-nav"))
        )
        with open("cookies.json", "w") as f:
            json.dump(driver.get_cookies(), f)
        return "Login Successful"

    def scrape_linkedin_job_links(
        self, search_params: str, country_filter_param: Optional[str] = None
    ) -> list:
        links: List = []
        driver = self.__get_driver()
        driver.get("https://www.linkedin.com/feed")
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get(
            url=f"https://www.linkedin.com/search/results/people/?keywords={search_params}&origin=SWITCH_SEARCH_VERTICAL&sid=Cnl"
        )
        time.sleep(2)
        if country_filter_param is not None:
            all_filters_button = driver.find_element(
                by=By.XPATH,
                value='//button[@aria-label="Show all filters. Clicking this button displays all available filter options."]',
            )
            all_filters_button.click()
            time.sleep(1)
            add_location_button = driver.find_element(
                by=By.XPATH,
                value='(//button[@class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view reusable-search-filters-advanced-filters__add-filter-button"])[3]',
            )
            add_location_button.click()
            add_location_input = driver.find_element(
                by=By.XPATH, value='//input[@aria-label="Add a location"]'
            )
            add_location_input.send_keys(country_filter_param)
            try:
                elements = WebDriverWait(driver, 100).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "basic-typeahead__selectable")
                    )
                )
                for element in elements:
                    if element.text == country_filter_param:
                        element.click()
                        break

            except StaleElementReferenceException:
                elements = WebDriverWait(driver, 100).until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "basic-typeahead__selectable")
                    )
                )
                for element in elements:
                    if element.text == country_filter_param:
                        element.click()
                        break
            time.sleep(1)
            apply_filter_button = driver.find_element(
                by=By.XPATH,
                value="//button[@class='reusable-search-filters-buttons search-reusables__secondary-filters-show-results-button artdeco-button artdeco-button--2 artdeco-button--primary ember-view']",
            )
            apply_filter_button.click()
            time.sleep(3)

        try:
            for page in range(1, 101):
                print(f"collecting the links in page {page}")
                people_block = WebDriverWait(driver, 100).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '//main/div[@aria-labelledby="search-srp-prompt"]',
                        )
                    )
                )
                profile_list = people_block.find_elements(
                    by=By.CSS_SELECTOR, value="li"
                )

                for profile in profile_list:
                    all_links = profile.find_elements(
                        by=By.TAG_NAME, value="a"
                    )
                    for a in all_links:
                        if (
                            "linkedin.com/in/" in str(a.get_attribute("href"))
                            and a.get_attribute("href") not in links
                        ):
                            links.append(a.get_attribute("href"))
                        else:
                            pass

                    driver.execute_script(
                        "arguments[0].scrollIntoView();", profile
                    )

                driver.find_element(
                    by=By.XPATH,
                    value=f'//button[@aria-label="Page {page + 1}"]',
                ).click()
                time.sleep(1)
        except:
            pass
        return links

    def __clean_name(self, raw_name: str):
        text = raw_name.lower()
        patterns = re.compile("([\(\[].*?[\)\]])|(acipm.*)|(hrpl.*)|(phri.*)")
        text = re.sub(patterns, "", text)
        return text.title()

    def scarpe_link_info(self, link: str) -> dict:
        scraped_jobs = {}
        driver = self.__get_driver()
        driver.get("https://www.linkedin.com/feed")

        with open("cookies.json", "r") as f:
            cookies = json.load(f)
        try:
            for cookie in cookies:
                driver.add_cookie(cookie)
        except:
            pass
        driver.get(url=link)
        time.sleep(1)
        try:
            top_content = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@class="ph5 pb5"]')
                )
            )
            name = top_content.find_element(by=By.TAG_NAME, value="h1").text
            name = self.__clean_name(name)
            scraped_jobs["Full Name"] = name
            title = top_content.find_element(
                by=By.XPATH,
                value='//div[@class="text-body-medium break-words"]',
            ).text
            scraped_jobs["Job Title"] = title
            location = top_content.find_element(
                by=By.XPATH,
                value='//span[@class="text-body-small inline t-black--light break-words"]',
            ).text
            scraped_jobs["Location"] = location
            other_contents = driver.find_elements(
                by=By.XPATH,
                value='//section[@class="artdeco-card ember-view relative break-words pb3 mt2 "]',
            )
            index = 0
            for element in other_contents:
                heading = element.text.split("\n")[0]
                if heading == "Experience":
                    index = other_contents.index(element) + 1
                    break
            experience_content = driver.find_element(
                by=By.XPATH,
                value=f'//section[@class="artdeco-card ember-view relative break-words pb3 mt2 "][{index}]',
            )
            company = (
                experience_content.find_element(by=By.TAG_NAME, value="li")
                .text.split("\n")[2]
                .split(" · ")[0]
            )
            scraped_jobs["Company"] = company
        except:
            pass

        try:
            driver.get(f"{link}/overlay/contact-info/")
            time.sleep(2)
            email = driver.find_element(
                by=By.XPATH,
                value='//section[@class="pv-contact-info__contact-type ci-email"]',
            ).text
        except NoSuchElementException:
            email = "Email no available on linkedin"
        if len(scraped_jobs) > 0:
            scraped_jobs["Email Address"] = email
        return scraped_jobs


def to_excel(data: List[dict], file_name: str, sheet_name: str):
    df = pd.DataFrame(data)
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    file_path = os.path.join(download_folder, f"{file_name}.xlsx")
    writer = pd.ExcelWriter(file_path, engine="xlsxwriter")
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    writer.save()


def to_console(data: List[dict]):
    df = pd.DataFrame(data)
    return df
