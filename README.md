# hh.kz Data Scraping and Analysis
Data parser that scrapes vacancy information from the hh.kz
and a data analysis code that gives insights about the job 
market by answering the following questions:  
1. What is the most popular junior-level IT job?  
2. What company is hiring the most IT professionals and what experience do they demand?  
3. What are the most in-demand skills and technologies?

## IMPORTANT
- Use main_code.ipynb in the front page only to view the code
- Use src folder to execute the code

## Table of Contents
- [Installation and Usage](#installation-and-usage)
- [Project Structure](#project-structure)
- [Team Members](#team-members)
- [Acknowledgments](#acknowledgements)

## Installation and usage
1. Clone the repository:
   ```bash
   git clone https://github.com/AlyaraSDU/Project-1
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run in Jupyter Notebook:
   ```bash
   jupyter notebook
4. Run only using python:
   ```bash
   python src/main_code.py
5. Note that the dataset scraped using our parser may not include necessary
   information due to the change of class names in HTML. 
   Thus, it is recommended to use the dataset that we provided.

## Project Structure

 - 'main_code.ipynb' : main code in the front page for ease of access, recommended only for viewing
 - 'src/' : main source code files, recommended for executing
 - 'data/': contains parsed data
 - 'requirements.txt': lists project libraries
 - 'Alyara/': code and files of Alyara
 - 'Yernur/': code and files of Yernur
 - 'Zhandos/': code and files of Zhandos

## Team Members

- **Alyara Abilbashar** - Parsing the website and documentation
- **Yernur Demessin** - Organization and merging the codes
- **Zhandos Mukhtarov** - Editing and uploading the project video

## Acknowledgements

- Thanks to Professor Birzhan Moldagaliyev for lectures on Pandas.
- This project uses the [Selenium](https://www.selenium.dev/) library for parsing the website.
- We also used [Pandas](https://pandas.pydata.org/) library for data manipulation
