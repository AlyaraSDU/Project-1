# This is the main code of project 1 

# SECTION 1
# Parse the hh.kz website and save the data into an excel file

import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

'''
driver = webdriver.Chrome()

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
            # Extract the job title
            try:
                title_element = vacancy.find_element(By.CSS_SELECTOR, "a[data-qa='serp-item__title']")
                title = title_element.text.strip()
                link = title_element.get_attribute('href')
            except:
                title = 'Not specified'
                link = 'Not specified'

            # Extract the company name
            try:
                company_element = vacancy.find_element(By.CSS_SELECTOR, "a[data-qa='vacancy-serp__vacancy-employer']")
                company = company_element.text.strip()
            except:
                company = 'Not specified'

            # Extract experience information
            try:
                experience_element = vacancy.find_element(By.CLASS_NAME, "magritte-tag__label___YHV-o_3-0-13").get_attribute("innerHTML")
            except:
                experience_element = 'Not specified'

            # Extract salary information
            try:
                salary = vacancy.find_element(By.CSS_SELECTOR, "span.magritte-text___pbpft_3-0-15.magritte-text_style-primary___AQ7MW_3-0-15.magritte-text_typography-label-1-regular___pi3R-_3-0-15").text
            except:
                salary = 'Not specified'

            # Extract requirement information
            try:
                requirement_element = vacancy.find_element(By.CSS_SELECTOR, "div[data-qa='vacancy-serp__vacancy_snippet_requirement'] > span").text.strip()
            except:
                requirement_element = 'Not specified'

            # Append the job information
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

    current_page += 1

driver.quit()


# Convert to DataFrame and save as Excel

df = pd.DataFrame(jobs)
print(df)
df.to_excel('job_listings_all_pages.xlsx', index=False)
'''


# SECTION 2
# Research question 1:
# What is the most popular specialization among junior-level developer vacancies?

# Create a DataFrame consisting only of titles and salaries of vacancies

df = pd.read_excel('job_listings_all_pages.xlsx')
df_work = df[['Job Title', 'Salary']]



# Convert every title into lowercase and delete missing values

df_work.loc[:, 'Job Title'] = df_work['Job Title'].str.lower()
df_work = df_work.dropna(subset=['Job Title'])


# Select raws that contain words "junior" and "младший"

junior = df_work[df_work['Job Title'].str.contains('junior|младший')]


# Reset old indexing so new indexing will be from 0 to 25

junior = junior.reset_index(drop=True)


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


# Get series by applying a function that normalizes job titles

# Function that merges different descriptions of the same profession into one
def normalize_title(title):
    for profession, keywords in result_dic.items():
        if any(keyword in title for keyword in keywords):
            return profession

jobs = junior['Job Title'].apply(normalize_title)


# Count occurrences of each IT profession and display the result

profession_count = jobs.value_counts()
print("\nResearch question 1 answer:\n")
print("\nOccurrences of each IT profession in descending order:\n")
print(profession_count)
print("___________________________________________________________")
# Create a dataframe with columns of job title and salary
junior_with_salaries = junior[junior['Salary'] != 'Not specified']
junior_with_salaries = junior_with_salaries.reset_index(drop=True)
print("\nIT Job Titles and Salaries:\n")
print(junior_with_salaries)

# Create a graph of quantites of IT professions

proffesion_count = profession_count.sort_values(ascending=False)

plt.figure(figsize=(6, 4)) 
plt.barh(profession_count.index, profession_count.values, color='skyblue')
plt.xlabel('Quantity')
plt.ylabel('Professions')
plt.title('Quantities of junior-level IT job offers')
plt.gca().invert_yaxis()
plt.show()
print("___________________________________________________________")


# SECTION 3
# Research question 2:
# Which company is hiring the most, and what levels of specialization are they hiring?

# Count vacancies in each company to get the most hiring one.

df = pd.read_excel('job_listings_all_pages.xlsx')
count_c = df['Company'].value_counts(dropna=False)
print("\nResearch question 2 answer:\n")
print("\nMost hiring companies:\n")
print(count_c)
print("___________________________________________________________")
# Save vacancies of the most hiring company to new DF and refine it

mh_company = df[df['Company']=='АО Народный банк Казахстана'].copy()
mh_company.loc[mh_company['Experience']=='Опыт более 6&nbsp;лет', 'Experience'] = 'Опыт более 6 лет'
experience = mh_company['Experience'].unique().tolist()


# Count how many vacancies are there for each experience level

count_level = mh_company['Experience'].value_counts(dropna=False)
results = [count_c.head(1), count_level]
print("\nNumber of vacancies for each experience level in most hiring company:\n")
print(results)
print("___________________________________________________________")

# SECTION 4
# Research question 3:
# How can parsing IT job listings from Headhunter.kz reveal insights into the most 
# in-demand skills and technologies in Kazakhstan's tech industry?

# Load the dataset from the provided file

file_path = 'job_listings_all_pages.xlsx'
df = pd.read_excel(file_path)


# List of programming languages and technologies to look for

languages = [
    'Python', 'Java', 'JavaScript', 'C#', 'PHP', 'Swift', 'Kotlin', 'Go', 'R',
    'Ruby', 'Perl', 'HTML', 'CSS', 'SQL', 'TypeScript', 'Dart', 'Rust', 'Scala',
    'RPA', 'Frontend', 'Backend', 'Full Stack'
]

# Defining and applying a function to categorize job titles based on programming languages

def extract_languages(job_title):
    found_languages = [lang for lang in languages if re.search(fr'\b{lang}\b', job_title, re.IGNORECASE)]
    return ', '.join(found_languages) if found_languages else 'Other'
    
df['Languages'] = df['Job Title'].apply(extract_languages)

# Count the occurrences of each language/technology to determine demand

language_demand = df['Languages'].value_counts().reset_index()
language_demand.columns = ['Programming Language', 'Demand']
language_demand = language_demand.sort_values(by='Demand', ascending=False)
print("\nResearch question 3 answer:\n")
print("\nOccurences of coding languages and other technologies:\n")
print(language_demand)







