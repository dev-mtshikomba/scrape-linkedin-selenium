"""Example to scrape a list of Companies, and put overviews in csv form"""

from scrape_linkedin import CompanyScraper
import pandas as pd

# LIST YOUR COMPANIES HERE
my_company_list = ['facebook', 'linkedin']

company_data = []

with CompanyScraper(timeout=180, cookie='AQEFALoBAAAAAAOTYYwAAAFzjoGKQgAAAXOyjg5CVgAAXXVybjpsaTplbnRlcnByaXNlUHJvZmlsZToodXJuOmxpOmVudGVycHJpc2VBY2NvdW50OjIyMTEwOTAsMTA0NzY0MTk1KV51cm46bGk6bWVtYmVyOjM0NjY2ODIwNsCH3CVUAtUsah') as scraper:
    # Get each company's overview, add to company_data list
    for name in my_company_list:
        overview = scraper.scrape(company=name).overview
        if (overview != None):
            overview['company_name'] = name
            company_data.append(overview)

# Turn into dataframe for easy csv output
df = pd.DataFrame(company_data)
df.to_csv('out.csv', index=False)
