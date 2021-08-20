from bs4 import BeautifulSoup
import requests
import time

def new_job_search(input_var,i):
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text
    soup_file = BeautifulSoup(html_text,'lxml')
    jobs = soup_file.find_all('li',class_='clearfix job-bx wht-shd-bx')
    job_search = input_var
    print("Searching for jobs in ",job_search)
    for job in jobs:
        post_dt = job.find('span',class_ = 'sim-posted').text.replace(" ","")
        if 'today' in post_dt:
            skills_req = job.find('span',class_ = 'srp-skills').text.replace(" ","")
            if job_search in skills_req:
                company_name = job.find('h3',class_='joblist-comp-name').text.replace(" ","")
                more_info = job.header.h2.a['href']
                f = open(f'C:/Users/Sreerupu/Desktop/Rupesh/Dev/Webscraping/Webscraping/Results/{i}_{job_search}','a')
                f.write(f"Company Name: {company_name.strip()}\n")
                f.write(f"Skills: {skills_req.strip()}\n")
                f.write(f"More Info: {more_info.strip()}\n")
                f.write(" ")

if __name__ == '__main__':
    i = 1
    variab = input("Enter the skill you have:")
    while True:
        new_job_search(variab,i)
        time_wait = 60
        print("Waiting 60 seconds")
        time.sleep(time_wait*1)
        i = i +1
