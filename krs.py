import numpy as np
import pandas as pd
import requests, re
import datetime
import time
from selenium import webdriver

from bs4 import BeautifulSoup as BS
from urllib.request import urljoin
from pytablewriter import MarkdownTableWriter

#from run import executable_path
executable_path=r'C:\Users\krajasekhara\PycharmProjects\CLL jobs scraping\chromedriver_win32\chromedriver.exe'

fields_needed=['Company Name',
                 'Job Title',
                 'Job Description',
                 'Job Location',
                 'Job Type',
                 'Years of Experience',
                 'Job Department',
                 'Job Specific URL',
                 'Career Page URL',
                  'Market/Sector']


def niramai(company_name,companies_details):
    # company_name = 'NIRAMAI'
    # career_page_url = 'https://www.niramai.com/careers/'

    print(company_name)

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    html = requests.get(career_page_url).text
    soup = BS(html, 'lxml')

    divs = soup.find('div', {'class': 'sjb-listing'})
    divs_all = divs.find_all('div', {'class': 'list-data'})

    df = pd.DataFrame(columns=fields_needed)

    for div in divs_all:
        job_title = div.find('span', {"class": "job-title"}).get_text().strip()

        job_description = div.find('div', {"class": "job-description"}).find_all('p')[0].get_text().strip()

        job_location = div.find('div', {'class': 'job-location'}).get_text().strip()

        job_type = div.find('div', {'class': 'job-type'}).get_text().strip()

        years_of_experience = np.nan

        job_department = np.nan

        job_specific_url = div.find('div', {"class": "job-description"}).find_all('p')[1].find('a')['href']
        # job_specific_url = urljoin(career_page_url,div.find('h4').find('a')['href'])

        df = df.append(pd.Series(data=[company_name,
                                       job_title,
                                       job_description,
                                       job_location,
                                       job_type,
                                       years_of_experience,
                                       job_department,
                                       job_specific_url,
                                       career_page_url,
                                       sector], index=fields_needed), ignore_index=True)
    return df


def locus(company_name,companies_details):
    # company_name = 'Locus'
    # career_page_url = 'https://locus.freshteam.com/jobs'

    print(company_name)

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    html = requests.get(career_page_url).text
    soup = BS(html, 'lxml')

    divs_all = soup.find('div', {'class': 'job-role-list'}).find_all('li')

    df = pd.DataFrame(columns=fields_needed)

    for div in divs_all:

        job_title = div.find('a', {"class": "job-title"}).get_text().strip()

        job_description = np.nan
        # job_description = div.find('a', {"class": "job-desc text"}).get_text().strip() #company intro available

        job_location = re.sub('[\s]+', ' ',div.find('div', {'class': 'job-location'}).find('a').get_text().strip().replace("\n"," ")).split(" ")[0]

        job_type = " ".join(re.sub('[\s]+', ' ',div.find('div', {'class': 'job-location'}).find('a').get_text().strip().replace("\n"," ")).split(" ")[1:])

        years_of_experience = np.nan

        if div.find('h5') is None:

            try:

                job_department = job_department

            except Exception as e:

                job_department = np.nan

        else:

            job_department = re.sub('[\s]+', ' ', div.find('h5').get_text().strip()).split(" ")[0]

        job_specific_url = urljoin(career_page_url, div.find('a', {"class": "job-title"})['href'])

        df = df.append(pd.Series(data=[company_name,
                                       job_title,
                                       job_description,
                                       job_location,
                                       job_type,
                                       years_of_experience,
                                       job_department,
                                       job_specific_url,
                                       career_page_url,
                                       sector], index=fields_needed), ignore_index=True)
    return df


def oneorigin(company_name,companies_details):
    # company_name = 'ONEORIGIN'
    # career_page_url = 'https://www.oneorigin.us/careers/'

    print(company_name)

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    headers = {'User-Agent': 'Mozilla/5.0'}

    html = requests.get(career_page_url, headers=headers).text
    soup = BS(html, 'lxml')

    divs = soup.find('div', {'class': 'column medium-12 col-md-12'})
    divs_all = divs.find_all('div', {'class': 'job-preview clearfix'})

    df = pd.DataFrame(columns=fields_needed)

    for div in divs_all:
        job_title = div.find('div', {"class": "job-content"}).find('h5').find('span').get_text().strip()

        job_description = div.find('div', {"class": "job_custom_message"}).get_text().strip()

        job_location = np.nan

        job_type = div.find('div', {"class": "job-additional-information"}).find('span').get_text().strip()

        years_of_experience = np.nan

        job_department = np.nan

        job_specific_url = urljoin(career_page_url,
                                   div.find('div', {"class": "job-content"}).find('h5').find('a')['href'])

        df = df.append(pd.Series(data=[company_name,
                                       job_title,
                                       job_description,
                                       job_location,
                                       job_type,
                                       years_of_experience,
                                       job_department,
                                       job_specific_url,
                                       career_page_url,
                                       sector], index=fields_needed), ignore_index=True)
    return df


def alphasense(company_name,companies_details):

    # company_name = 'ALPHASENSE'
    # career_page_url = 'https://www.alpha-sense.com/careers'

    print(company_name)

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    driver = webdriver.Chrome(executable_path=executable_path)

    driver.get(career_page_url)

    # driver.maximize_window()

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;") #;var lenOfPage=document.body.scrollHeight;return lenOfPage;

    time.sleep(15)

    df = pd.DataFrame(columns=fields_needed)

    try:

        departments = driver.find_elements_by_class_name('department')

        for department in departments:

            job_department = department.find_element_by_tag_name('h4').text.title()

            jobs = department.find_elements_by_class_name('job')

            for job in jobs:

                job_title = job.find_element_by_class_name('description').text.split('\n')[0]

                job_description = np.nan

                job_location = job.find_element_by_class_name('location').text

                job_type = np.nan

                years_of_experience = np.nan

                job_specific_url = job.find_element_by_class_name('cta').find_element_by_tag_name('a').get_attribute('href')

                df = df.append(pd.Series(data=[company_name,
                                               job_title,
                                               job_description,
                                               job_location,
                                               job_type,
                                               years_of_experience,
                                               job_department,
                                               job_specific_url,
                                               career_page_url,
                                               sector], index=fields_needed), ignore_index=True)
    except Exception as e:

        print(e)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)

    finally:

        driver.quit()

    return df

def sayint(company_name,companies_details):

    #     company_name = 'sayint'
    #     career_page_url = 'https://sayint.freshteam.com/jobs'

    print(company_name)

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    html = requests.get(career_page_url).text
    soup = BS(html, 'lxml')

    divs = soup.find('div', {'class': 'job-role-list'})

    divs_roles = divs.find_all('ul', {'class': 'open-list'})

    df = pd.DataFrame(columns=fields_needed)

    for div_role in divs_roles:

        job_department = re.sub('[\s]+', ' ',div_role.find('div', {"class": "role-title"}).h5.get_text().strip().replace("\n"," ")).split(" ")[0]

        divs_all = div_role.find_all('li', {'class': 'heading'})

        for div in divs_all:

            job_title = div.find('a', {"class": "job-title"}).get_text().strip()

            job_description = div.find('a', {"class": "job-desc text"}).get_text().strip()

            job_location = re.sub('[\s]+', ' ',div.find('div', {'class': 'job-location'}).find('a').get_text().strip().replace("\n"," ")).split(" ")[0]

            job_type = " ".join(re.sub('[\s]+', ' ',div.find('div', {'class': 'job-location'}).find('a').get_text().strip().replace("\n", " ")).split(" ")[1:])

            years_of_experience = np.nan

            job_specific_url = urljoin(career_page_url, div.find('div').find('a', {"class": "job-desc text"})['href'])

            df = df.append(pd.Series(data=[company_name,
                                           job_title,
                                           job_description,
                                           job_location,
                                           job_type,
                                           years_of_experience,
                                           job_department,
                                           job_specific_url,
                                           career_page_url,
                                           sector], index=fields_needed), ignore_index=True)

    return df


def casetext(company_name,companies_details):

    #     company_name = 'CASETEXT'
    #     career_page_url = 'https://jobs.lever.co/casetext/'

    print(company_name)

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    html = requests.get(career_page_url).text
    soup = BS(html, 'lxml')

    div_posting = soup.find('div', {'class': 'postings-group'})

    divs_posting = div_posting.find_all('div', {'class': 'posting'})

    df = pd.DataFrame(columns=fields_needed)

    for div in divs_posting:
        job_title = div.find('a', {"class": "posting-title"}).find('h5').get_text().strip()

        job_description = np.nan

        job_location = div.find('span',
                                {"class": "sort-by-location posting-category small-category-label"}).get_text().strip()

        job_type = np.nan

        years_of_experience = np.nan

        job_department = div.find('span',
                                  {"class": "sort-by-team posting-category small-category-label"}).get_text().strip()

        job_specific_url = urljoin(career_page_url, div.find('a', {"class": "posting-title"})['href'])

        df = df.append(pd.Series(data=[company_name,
                                       job_title,
                                       job_description,
                                       job_location,
                                       job_type,
                                       years_of_experience,
                                       job_department,
                                       job_specific_url,
                                       career_page_url,
                                       sector], index=fields_needed), ignore_index=True)
    return df


#niramai('Niramai','https://www.niramai.com/careers/')
#locus('Locus','https://locus.freshteam.com/jobs')
#oneorigin('OneOrigin', 'https://www.oneorigin.us/careers/')
#alphasense('alphaSense', 'https://www.alpha-sense.com/careers')
#sayint('sayint','https://sayint.freshteam.com/jobs')
#casetext('CASETEXT','https://jobs.lever.co/casetext/')