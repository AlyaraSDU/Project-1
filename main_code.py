# This is the main code of project 1 

# SECTION 1
# Parsing the hh.kz website and saving the data into excel file

!/usr/bin/env python
coding: utf-8

import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import time

# Set up the WebDriver (ensure ChromeDriver is installed and in PATH)

driver = webdriver.Chrome()

# Load the initial webpage

base_url = "https://almaty.hh.kz/search/vacancy?L_save_area=true&text=&excluded_text=&professional_role=156&professional_role=160&professional_role=150&professional_role=25&professional_role=165&professional_role=36&professional_role=96&professional_role=104&professional_role=157&professional_role=112&professional_role=113&professional_role=148&professional_role=114&professional_role=116&professional_role=121&professional_role=124&professional_role=125&area=160&salary=&currency_code=KZT&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=vacancy_search_filter&page="

# Scrape job listings across multiple pages, extracting details like title, 
# company, experience, salary, and requirements, and store them in a list.

current_page = 1
jobs = []

while True:
    # Construct the URL for the current page
    url = f"{base_url}{current_page}"
    driver.get(url)
    time.sleep(5)

    # Scroll down to ensure all elements are loaded
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    # Extract job data using Selenium for consistency
    vacancies = driver.find_elements(By.CSS_SELECTOR, "div.vacancy-info--umZA61PpMY07JVJtomBA")
    if not vacancies:  # Stop if no more vacancies are found
        break

    for vacancy in vacancies:
        try:
            # Extracting the job title
            try:
                title_element = vacancy.find_element(By.CSS_SELECTOR, "a[data-qa='serp-item__title']")
                title = title_element.text.strip()
                link = title_element.get_attribute('href')
            except:
                title = 'Not specified'
                link = 'Not specified'

            # Extracting the company name
            try:
                company_element = vacancy.find_element(By.CSS_SELECTOR, "a[data-qa='vacancy-serp__vacancy-employer']")
                company = company_element.text.strip()
            except:
                company = 'Not specified'

            # Extracting experience information
            try:
                experience_element = vacancy.find_element(By.CLASS_NAME, "magritte-tag__label___YHV-o_3-0-13").get_attribute("innerHTML")
            except:
                experience_element = 'Not specified'

            # Extracting salary information
            try:
                salary = vacancy.find_element(By.CSS_SELECTOR, "span.magritte-text___pbpft_3-0-15.magritte-text_style-primary___AQ7MW_3-0-15.magritte-text_typography-label-1-regular___pi3R-_3-0-15").text
            except:
                salary = 'Not specified'

            # Extracting requirement information
            try:
                requirement_element = vacancy.find_element(By.CSS_SELECTOR, "div[data-qa='vacancy-serp__vacancy_snippet_requirement'] > span").text.strip()
            except:
                requirement_element = 'Not specified'

            # Appending the job information
            jobs.append({
                'Job Title': title,
                'Company': company,
                'Experience': experience_element,
                'Salary': salary,
                'Requirements': requirement_element,
                'Link': link
            })

        except Exception as e:
            print(f"Error while extracting data for a job: {e}")

    # Move to the next page
    current_page += 1

# Close the WebDriver

driver.quit()

# Convert to DataFrame and save as Excel

df = pd.DataFrame(jobs)
print(df)
df.to_excel('job_listings_all_pages.xlsx', index=False)

print("Data has been saved to job_listings_all_pages.xlsx")

# SECTION 2
# Research question 1:
# What is the most popular specialization among junior-level developer vacancies?

# Make an Excel file consisting only of titles of vacancies

df = pd.read_excel('job_listings_all_pages.xlsx')
df_work = df['Job Title']
df_work.to_excel('titles.xlsx', index = False)

# Convert every title to lower case and delete missing values

df_work = df_work.str.lower()
df_work = df_work.dropna()

# Select raws that contain words "junior" and "младший"

junior = df_work[df_work.str.contains('junior|младший')]
junior

# Reset old indexing so new indexing will be from 0 to 25

junior = junior.reset_index(drop=True)
junior.info()

# Create a dictionary of key words that target professions

result_dic = {
    "Helpdesk": ["специалист", "specialist", "поддержки", "l1", "product"],
    "Cybersecurity": ["cyber"],
    "Front end": ["frontend"],
    "Python": ["python"],
    "Analyst": ["analyst", "аналитик", "sales"],
    "Back end": ["backend"],
    "DevOps": ["devops"],
    "Tester": ["qa-engineer", "тестировщик"],
    ".NET developer": [".net"],
    "AI developer": ["ai"],
    "1C developer": ["1с"],
    "Full stack": ["full"]
}
result_dic

# Function that merges different descriptions of the same profession into one

def normalize_title(title):
    for profession, keywords in result_dic.items():
        if any(keyword in title for keyword in keywords):
            return profession

# Create a new column with normalized job titles

jobs = junior.apply(normalize_title)

# Count occurrences of each IT profession and display the result

profession_count = jobs.value_counts()
print(profession_count)

# SECTION 3
# Research question 2:
# Which company is hiring the most, and what levels of specialization are they hiring?

# Read excel file with parsed data as DataFrame

df = pd.read_excel('Project/job_listings_all_pages.xlsx')

# Count vacancies in each company to get the most hiring one.

count_c = df['Company'].value_counts(dropna=False)

# Save vacancies of the most hiring company to new DF. 

mh_company = df[df['Company']=='АО Народный банк Казахстана']

# Change text in Experience column to readable one.

mh_company.loc[mh_company['Experience']=='Опыт более 6&nbsp;лет', 'Experience'] = 'Опыт более 6 лет'

# Write experience levels to a list

experience = mh_company['Experience'].unique().tolist()

# Count how many vacancies are there for each experience level

count_level = mh_company['Experience'].value_counts(dropna=False)

# Write all results to one list

results = [count_c.head(1), count_level]







