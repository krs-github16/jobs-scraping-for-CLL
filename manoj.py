from selenium import webdriver

from bs4 import BeautifulSoup as BS
import requests
import numpy as np
import json
import time
import pandas as pd

fields_needed = ['Company Name',
               'Job Title',
               'Job Description',
               'Job Location',
               'Job Type',
               'Years of Experience',
               'Job Department',
               'Job Specific URL',
               'Career Page URL',
               'Market/Sector']
gecko_path = r'C:\Users\krajasekhara\PycharmProjects\CLL jobs scraping\drivers\geckodriver\geckodriver.exe'

def zebra(company_name,companies_details):

    # company_name = 'Zebra Medical Vision'
    # career_page_url = 'https://www.zebra-med.com/careers'

    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    df = pd.DataFrame(columns=fields_needed)
    try:
        response = requests.get(career_page_url, headers=headers)
        if response:
            for job in BS(response.text,'html.parser').find_all('a',class_='comeet-position'):
            #   print(job.find(class_='comeet-position-meta').text.strip())
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

    print(company_name)

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

    print(company_name)

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

    print(company_name)

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


def angel_co(company_name, companies_details):

    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    df = pd.DataFrame(columns=fields_needed)
    driver = webdriver.Firefox(executable_path=gecko_path)

    try:
        driver.get(career_page_url)
        time.sleep(2)
        page_source = driver.page_source
        count = 0

        for job in BS(page_source, 'html.parser').find_all(class_='component_e6bd3'):
            try:
                if job.find('a'):
                    count += 1
                    job_title = job.find('h4').text.strip()
                    job_specific_url = 'https://angel.co' + job.find('a').get('href')
                    job_location = job.find(class_='location_5ec2b').text
                    job_description = job.find(class_='descriptionSnippet_9f121').text
                    job_type = np.nan
                    years_of_experience = np.nan
                    job_department = job.find('h6').text
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
    except Exception as e:
        print(e)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)
    driver.close()
    return df


def insilico(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)
    count = 0
    df = pd.DataFrame(columns = fields_needed)
    for job in BS(requests.get(career_page_url,"lxml").text).find_all(class_='t649__col'):
        try:
            count += 1

            job_title = job.find(class_='t649__title').text.strip()
            job_specific_url = career_page_url
            job_type = np.nan
            years_of_experience = np.nan
            job_description = job.find(class_='t649__text').text
            job_location = np.nan
            if 'Location' in job.find(class_='t649__text').find('strong').text:
                job_location = job.find(class_='t649__text').find('strong').next_sibling
            job_department = np.nan

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
        except Exception as error:

            print(error)

            print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)

    return df


def loginextsolutions(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)
    count = 0
    df = pd.DataFrame(columns = fields_needed)
    response = BS(requests.get(career_page_url,"lxml").text)
    for domain in response.find_all(class_='panel'):
        for job in domain.find(class_='panel-contain').find_all('a', target="_blank"):
            try:
                count += 1
                job_title = job.find(class_='title').text.strip()
                job_specific_url = job.get('href')
                job_location = job.find(class_='position-location').text.strip()

                job_description = job.find(class_='disc').text.strip()
                job_type = np.nan
                years_of_experience = np.nan
                job_department = domain.find(class_='position-name').text.strip()

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
            except Exception as error:

                print(error)

                print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)

    return df


def appen(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    url = 'https://talent-appen.icims.com/jobs/search?pr={}&in_iframe=1'
    count = 0
    page = 0
    job_table = BS(requests.get(url.format(str(page))).text, 'lxml').find(class_='iCIMS_JobsTable')
    count = 0
    df = pd.DataFrame(columns=fields_needed)
    while True:
        for job in job_table.find_all(class_='row'):
            try:
                count += 1
                job_title = job.find('a').find_all('span')[1].text.strip()
                job_description = job.find(class_='description').text.strip()
                job_specific_url = job.find('a').get('href')
                job_location = np.nan
                if 'Locations' in job.find('span').text:
                    job_location = job.find('span').find_next('span').text.strip()

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
                                               career_page_url,
                                               sector], index=fields_needed), ignore_index=True)
            except Exception as e:
                print(e)
        page += 1
        job_table = BS(requests.get(url.format(str(page))).text, 'lxml').find(class_='iCIMS_JobsTable')
        if not job_table:
            break
    return df


def zymergen(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    df = pd.DataFrame()
    response = requests.get(career_page_url)
    for script in BS(response.text, 'html.parser').find_all('script', type='text/javascript'):
        if 'ghjb_d=true;ghjb_a=0;ghjb_job' in str(script):
            total_jobs = []
            for i in \
            str(script).replace('<script type="text/javascript">', '').replace('</script>', '').split('ghjb_jobs = ')[
                1].replace('},];ghjb_json =', '}];ghjb_json =').split(',"meta":')[0].split(';ghjb_json = {"jobs":'):
                total_jobs.extend(json.loads(i))
            for i in total_jobs:
                job_title = i.get('title').strip()
                job_description = BS(BS(i.get('content'), 'html.parser').text, 'html.parser').text
                job_specific_url = i.get('absolute_url')
                job_location = i.get('location').get('name')

                job_type = np.nan
                years_of_experience = np.nan
                job_department = i.get('departments')[0].get('name')

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


def kore(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    df = pd.DataFrame(columns=fields_needed)
    for job in BS(requests.get(career_page_url).text, 'html.parser').find(class_='w-tabs-sections-h').find_all(
            class_='wpb_text_column')[3:]:
        if job.find('a', class_=True):
            if 'in' in job.find('a').get('class')[0] or 'jobdesc' in job.find('a').get('class')[0]:
                job_title = job.find('p').text.split('Location')[0].strip()
                job_description = np.nan
                job_specific_url = job.find('a').get('href')
                job_location = job.find('p').find_next(class_='careers-location').text.split('Location:')[1].strip()

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
                                               career_page_url,
                                               sector], index=fields_needed), ignore_index=True)
    return df


def nvidia(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    df = pd.DataFrame(columns=fields_needed)
    offset = 0
    response = requests.get(
        career_page_url + '/fs/searchPagination/318c8bb6f553100021d223d9780d30be/{}?clientRequestID=958a11e44f0d4967ab077e9f2b761db0'.format(
            str(offset)))
    jobs = response.json().get('body').get('children')[0].get('children')[0].get('listItems')
    count = 0
    while jobs:
        for job in jobs:
            count += 1
            job_title = job.get('title').get('instances')[0].get('text')
            job_specific_url = 'https://nvidia.wd5.myworkdayjobs.com' + job.get('title').get('commandLink')
            job_location = job.get('subtitles')[-2].get('instances')[0].get('text')
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
                                           career_page_url,
                                           sector], index=fields_needed), ignore_index=True)
        offset += len(jobs)
        response = requests.get(
            career_page_url + '/fs/searchPagination/318c8bb6f553100021d223d9780d30be/{}?clientRequestID=958a11e44f0d4967ab077e9f2b761db0'.format(
                str(offset)))
        if response:
            jobs = response.json().get('body').get('children')[0].get('children')[0].get('listItems')
        else:
            jobs = []
    return df

#  zebra('Zebra Medical Vision','https://www.zebra-med.com/careers'),
#  episource('Episource LLC','https://www.episource.com/careers/'),
#  vicarious('Vicarious','https://www.vicarious.com/careers/'),
#  uipath('UI Path','https://www.uipath.com/company/careers/jobs')
#  angel_co('niki.ai',companies_details),
#  angel_co('vernacular.ai',companies_details),
#  angel_co('saarthi.ai',companies_details),
#  angel_co('Ori',companies_details),
#  angel_co('floatbot.ai',companies_details),
#  angel_co('Butterfly Network',companies_details),
#  angel_co('arya.ai',companies_details),
#  angel_co('pixuate',companies_details),
#  angel_co('couture.ai',companies_details)
# angel_co('streamingo.ai',companies_details),
# angel_co('orbo.ai',companies_details),
# zymergen('zymergen', companies_details),
# kore('kore.ai', companies_details),
# nvidia('nVidia',companies_details)
