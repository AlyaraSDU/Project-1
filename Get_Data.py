#!/usr/bin/env python
# coding: utf-8

# In[21]:


import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up the WebDriver (ensure ChromeDriver is installed and in PATH)
driver = webdriver.Chrome()

# Load the initial webpage
base_url = "https://almaty.hh.kz/search/vacancy?L_save_area=true&text=&excluded_text=&professional_role=156&professional_role=160&professional_role=150&professional_role=25&professional_role=165&professional_role=36&professional_role=96&professional_role=104&professional_role=157&professional_role=112&professional_role=113&professional_role=148&professional_role=114&professional_role=116&professional_role=121&professional_role=124&professional_role=125&area=160&salary=&currency_code=KZT&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=vacancy_search_filter&page="
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

            # Extracting the job location
            #try:
             #   location = vacancy.find_element(By.CSS_SELECTOR, "span[data-qa='vacancy-serp__vacancy-address']").text.strip()
            #except:
               # location = 'Not specified'

            # Extracting experience information
            try:
                experience_element = vacancy.find_element(By.CLASS_NAME, "magritte-tag__label___YHV-o_3-0-13").get_attribute("innerHTML")
            except:
                experience_element = 'Not specified'

            # Extracting salary information
            try:
                salary = vacancy.find_element(By.CSS_SELECTOR, "span.magritte-text___pbpft_3-0-15.magritte-text_style-primary___AQ7MW_3-0-15.magritte-text_typography-label-1-regular___pi3R-_3-0-15").text
            # Use regex to extract the numeric value
            #number = re.findall(r'\d+', span_text.replace('\u202f', ''))
            #numeric_value = "".join(number)
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
                #'Location': location,
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


# In[25]:


import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up the WebDriver (ensure ChromeDriver is installed and in PATH)
driver = webdriver.Chrome()

# Load the initial webpage (only the first page)
url = "https://almaty.hh.kz/search/vacancy?L_save_area=true&text=&excluded_text=&professional_role=156&professional_role=160&professional_role=150&professional_role=25&professional_role=165&professional_role=36&professional_role=96&professional_role=104&professional_role=157&professional_role=112&professional_role=113&professional_role=148&professional_role=114&professional_role=116&professional_role=121&professional_role=124&professional_role=125&area=160&salary=&currency_code=KZT&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=vacancy_search_filter"
jobs = []

# Visit the URL
driver.get(url)
time.sleep(5)

# Scroll down to ensure all elements are loaded
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

# Extract job data using Selenium for consistency
vacancies = driver.find_elements(By.CSS_SELECTOR, "div.vacancy-info--umZA61PpMY07JVJtomBA")

for vacancy in vacancies:
    try:
        # Extracting the job location
        try:
            requirement_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-qa='vacancy-serp__vacancy_snippet_requirement'] span"))
            )
            requirement_text = requirement_element.text.strip() if requirement_element else 'Not specified'
        except:
            requirement_text = 'Not specified'

        # Append the job information
        jobs.append({
            'Salary': requirement_text,
        })
        
    except Exception as e:
        print(f"Error while extracting data for a job: {e}")

# Close the WebDriver
driver.quit()

# Convert to DataFrame and print
df = pd.DataFrame(jobs)
print(df)


# In[ ]:




