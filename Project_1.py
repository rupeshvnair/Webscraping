from bs4 import BeautifulSoup
import requests
import re

f = open('C:/Users/Sreerupu/Desktop/Rupesh/Dev/Webscraping/Webscraping/Results/College_5_data.csv','a')
f.write('Name,College_Type,Course,Contact,Email,Website,Address\n')
for i in range(36,37):
    website = requests.get(f'http://education-india.in/Education/Colleges/?PageNumber={i}').text
    soup_obj = BeautifulSoup(website,'lxml')
    college_list = soup_obj.find('table',class_='index')
    college_link = college_list.find_all('a')
    for links in college_link:
        direct_data = links['href']
        college_data = requests.get(f'http://education-india.in/Education/Colleges/{direct_data}').text
        college_data_1 = re.sub('\n',' ',college_data)
        college_details = BeautifulSoup(college_data_1,'lxml')
        college_body = college_details.find('table',class_='detail')

        if college_body is None:
            pass
        else:
            college_rows = college_body.find_all('tr')
            Name =''
            College_Type =''
            Course = ''
            Contact = ''
            Email = ''
            Website = ''
            Address = ''
            for row in college_rows:
                if row.text == ' ':
                    pass
                elif row.th.text == 'Name':
                    Name = row.td.text.replace(","," or ").strip()
                elif row.th.text == 'College Type':
                    College_Type = row.td.text.replace(","," or ").strip()
                elif row.th.text == 'Course Type':
                    Course = row.td.a.text.replace(","," or ").strip()
                    for nw in row.td.br:
                        Course = Course + ',' + row.td.br.text.replace(","," or ").strip()
                elif row.th.text == 'Contact':
                    Contact = row.td.text.replace(","," or ").strip()
                elif row.th.text == 'Email ID':
                    Email = row.td.text.replace(","," or ").strip()
                elif row.th.text == 'Website':
                    Website = row.td.text.replace(","," or ").strip()
                elif row.th.text == 'Address':
                    Address = row.td.text.replace(","," | ").strip()
                else:
                    pass
            f.write(f'{Name},{College_Type},{Course},{Contact},{Email},{Website},{Address}\n')









