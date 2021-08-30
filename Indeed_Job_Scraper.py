from bs4 import BeautifulSoup
import requests

jobTitle="software engineering"
jobLocation="Canada"

url="https://ca.indeed.com/jobs?q={job}&l={location}".format(job=jobTitle,location=jobLocation)

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="resultsBody")
# print(results.prettify())

job_elements = results.find_all("div", class_="job_seen_beacon")


for job_element in job_elements:
    title_element = job_element.find("h2", class_="jobTitle")
    company_element = job_element.find("span", class_="companyName")
    location_element = job_element.find("div", class_="companyLocation")
    print()
    print("Job Title:",title_element.text.strip())
    print("Company:",company_element.text.strip())
    print("Location:",location_element.text.strip())
    print()