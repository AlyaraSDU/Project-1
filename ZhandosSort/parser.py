import pandas as pd

# Load the dataset from the provided file
file_path = 'D:job_listings_all_pages.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows to understand the structure of the data
df.head()


# Count the occurrences of each job title to determine demand
job_demand = df['Job Title'].value_counts().reset_index()
job_demand.columns = ['Job Title', 'Demand']  # Rename columns for clarity

# Sort the data in descending order by demand
job_demand = job_demand.sort_values(by='Demand', ascending=False)

# Save the sorted data to a new Excel file
output_file_path = "C:\\Users\\Zhandos Mukhtarov\\Documents\\it_jobs_demand_sorted.xlsx"

job_demand.to_excel(output_file_path, index=False)

output_file_path
