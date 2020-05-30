from bs4 import BeautifulSoup as BS
import requests
import numpy as np
import json
import pandas as pd

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

def zebra(company_name,companies_details):

    # company_name = 'Zebra Medical Vision'
    # career_page_url = 'https://www.zebra-med.com/careers'

    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    df = pd.DataFrame(columns=fields_needed)
    try:
        response = requests.get(career_page_url, headers=headers)
        if response:
            for job in BS(response.text,'html.parser').find_all('a',class_='comeet-position'):
            #     print(job.find(class_='comeet-position-meta').text.strip())
                job_title = job.find(class_='comeet-position-name').text.strip()
                job_specific_url = job.get('href')
                job_location =np.nan
                job_description = np.nan
                job_type = np.nan
                years_of_experience = np.nan
                job_department = np.nan
                df = df.append(pd.Series(data=[company_name,
                                                   job_title,
                                                   job_description,
                                                   job_location,
                                                   job_type,
                                                   years_of_experience,
                                                   job_department,
                                                   job_specific_url,
                                               career_page_url,sector], index=fields_needed), ignore_index=True)
    except Exception as e:
        print(e)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)
    return df


def episource(company_name,companies_details):

    # company_name = 'Episource LLC'
    # career_page_url = 'https://www.episource.com/careers/'

    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }

    df = pd.DataFrame(columns=fields_needed)
    try:
        response = requests.get(career_page_url,headers=headers)
        if response:
            for job in BS(response.text, 'html.parser').find_all('a',title='READ MORE'):

                job_title = job.find('h3').text.strip()
                job_description = np.nan
                job_location = job.get('href').split('l=')[-1].upper()
                job_type = np.nan
                years_of_experience = np.nan
                job_department = np.nan
                job_specific_url = job.get('href')

                df = df.append(pd.Series(data=[company_name,
                                                   job_title,
                                                   job_description,
                                                   job_location,
                                                   job_type,
                                                   years_of_experience,
                                                   job_department,
                                                   job_specific_url,
                                               career_page_url,sector], index=fields_needed), ignore_index=True)
    except Exception as e:
        print(e)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)
    return df


def vicarious(company_name,companies_details):

    # company_name = 'Vicarious'
    # career_page_url = 'https://www.vicarious.com/careers/'

    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    df = pd.DataFrame(columns=fields_needed)
    try:
        response = requests.get('https://api.lever.co/v0/postings/vicarious?mode=json')
        if response:
            for job in response.json():

                job_title = job.get('text')
                job_description = job.get('descriptionPlain')
                job_location = job.get('location')
                job_type = job.get('categories').get('commitment')
                years_of_experience = np.nan
                job_department = job.get('categories').get('team')
                job_specific_url = job.get('hostedUrl')

                df = df.append(pd.Series(data=[company_name,
                                                   job_title,
                                                   job_description,
                                                   job_location,
                                                   job_type,
                                                   years_of_experience,
                                                   job_department,
                                                   job_specific_url,
                                               career_page_url,sector], index=fields_needed), ignore_index=True)
    except Exception as e:
        print(e)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)
    return df
    


def uipath(company_name,companies_details):

    # company_name = 'UI Path'
    # career_page_url = 'https://www.uipath.com/company/careers/jobs'

    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    df = pd.DataFrame(columns=fields_needed)
    try:
        response = requests.get('https://smartdreamers.com/api/postings/uipath')
        if response:
            for place in response.json():
                for job in place.get('postings'):

                    job_title = job.get('text')
                    job_description = np.nan
                    job_location = job.get('location')
                    job_type = job.get('categories').get('commitment')
                    years_of_experience = np.nan
                    job_department = job.get('categories').get('team')
                    job_specific_url = job.get('jobURL')

                    df = df.append(pd.Series(data=[company_name,
                                                       job_title,
                                                       job_description,
                                                       job_location,
                                                       job_type,
                                                       years_of_experience,
                                                       job_department,
                                                       job_specific_url,
                                                   career_page_url,sector], index=fields_needed), ignore_index=True)
    
    except Exception as e:
        print(e)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)
    return df

# zebra('Zebra Medical Vision','https://www.zebra-med.com/careers'),
#  episource('Episource LLC','https://www.episource.com/careers/'),
#  vicarious('Vicarious','https://www.vicarious.com/careers/'),
#  uipath('UI Path','https://www.uipath.com/company/careers/jobs')
