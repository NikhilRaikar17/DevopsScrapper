import csv
from jobspy import scrape_jobs
from datetime import datetime

jobs = scrape_jobs(
    site_name=["indeed", "linkedin"],
    search_term="Devops Engineer",
    location="germany",
    results_wanted=30,
    hours_old=72, # (only Linkedin/Indeed is hour specific, others round up to days old)
    country_indeed='germany',  # only needed for indeed / glassdoor
    
    linkedin_fetch_description=True # get full description and direct job url for linkedin (slower)
    # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
    
)
print(f"Found {len(jobs)} jobs")

current_time = datetime.today().strftime('%Y-%m-%d')

jobs.to_csv(f"jobs_{current_time}.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel