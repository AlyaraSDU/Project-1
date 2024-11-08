import pandas as pd
import re

# Load the dataset from the provided file
file_path = 'D:job_listings_all_pages.xlsx'

df = pd.read_excel(file_path)

# Display the first few rows to understand the structure of the data
df.head()

# List of programming languages and technologies to look for
languages = [
    'Python', 'Java', 'JavaScript', 'C#', 'PHP', 'Swift', 'Kotlin', 'Go', 'R',
    'Ruby', 'Perl', 'HTML', 'CSS', 'SQL', 'TypeScript', 'Dart', 'Rust', 'Scala',
    'RPA', 'Frontend', 'Backend', 'Full Stack'
]

# Function to categorize job titles based on programming languages
def extract_languages(job_title):
    found_languages = [lang for lang in languages if re.search(fr'\b{lang}\b', job_title, re.IGNORECASE)]
    return ', '.join(found_languages) if found_languages else 'Other'

# Apply the function to create a new column with extracted languages
df['Languages'] = df['Job Title'].apply(extract_languages)

# Count the occurrences of each language/technology to determine demand
language_demand = df['Languages'].value_counts().reset_index()
language_demand.columns = ['Programming Language', 'Demand']  # Rename columns for clarity

# Sort the data in descending order by demand
language_demand = language_demand.sort_values(by='Demand', ascending=False)

# Save the sorted data to a new Excel file
output_file_path = "C:\\Users\\Zhandos Mukhtarov\\Documents\\it_jobs_demand_sorted.xlsx"

language_demand.to_excel(output_file_path, index=False)

output_file_path


