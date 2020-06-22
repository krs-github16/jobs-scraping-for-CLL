import numpy as np
import pandas as pd
import requests, re
from bs4 import BeautifulSoup as BS
from urllib.request import urljoin

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


def abto(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    try:

        html = requests.get(career_page_url).text
        soup = BS(html, 'lxml')
        loc = []

        df = pd.DataFrame(columns=fields_needed)

        for item in soup.findAll("a", {"class": "vacancy-item"}):
            job_specific_url = item.get("href")

            for body in item.findAll("div", {"class": "vacancy-body"}):
                for title in body.findAll("div", {"class": "vacancy-title"}):
                    job_title = title.text.strip()

            for ul in body.findAll('ul'):
                for li in ul.findAll('li'):
                    loc.append(li.text.strip())  # take the first element

            for dept in item.findAll("div", {"class": "vacancy-department"}):
                job_department = dept.text.strip()

            job_description = np.nan

            job_location = loc[0]

            job_type = np.nan

            years_of_experience = np.nan

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


def kritikal(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    df = pd.DataFrame(columns=fields_needed)

    try:
        html = requests.get(career_page_url).text
        soup = BS(html, 'lxml')

        for item in soup.findAll("article", {"id": "blog-grid"}):
            for name in item.findAll("h3"):
                job_title = name.text.strip()

            for a in name.findAll('a'):
                job_specific_url = a.get('href')

            for e in item.findAll('span', {'class': 'slide-meta-exp'}):
                years_of_experience = e.text.strip()

            for l in item.findAll('span', {'class': 'slide-meta-loc'}):
                job_location = l.text.strip()

            for d in item.findAll('div', {'class': 'entry-content'}):
                job_description = d.text.strip()

            job_type = np.nan

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


def atlas_elektronik(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    df = pd.DataFrame(columns=fields_needed)

    try:
        html = requests.get(career_page_url).text
        soup = BS(html, 'lxml')

        for item in soup.findAll("div", {"class": "jobs-item"}):
            for a in item.findAll("a"):
                job_specific_url = urljoin(career_page_url, a.get('href'))

            for job in item.findAll("span", {"class": "job-item--title"}):
                job_title = job.text.strip()

            for loc in item.findAll("span", {"class": "job-region--name"}):
                job_location = loc.text.strip()

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
    except Exception as error:

        print(error)

        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)

    return df


def tobii(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    df = pd.DataFrame(columns=fields_needed)

    try:
        html = requests.get(career_page_url).text
        soup = BS(html, 'lxml')

        for item in soup.findAll("div", {"class": "job-listing-container"}):
            for ul in item.findAll('ul'):
                for li in ul.findAll('li'):
                    for a in li.findAll('a'):
                        job_specific_url = urljoin(career_page_url, a.get('href'))

                    for j in li.findAll("span", {"class": "title"}):
                        job_title = j.text.strip()

                    for t in li.findAll("span", {"class": "meta"}):
                        ty = t.text.strip()

                    ty_split = ty.split('-', 1)

                    job_type = ty_split[0]

                    job_location = ty_split[1]

                    job_description = np.nan

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
    except Exception as error:

        print(error)

        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)

    return df


def philips(company_name,companies_details):
    career_page_url =  companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    df = pd.DataFrame(columns=fields_needed)

    try:
        html = requests.get(career_page_url).text
        soup = BS(html, 'lxml')

        for itemAll in soup.findAll("div", {"id": "direct_container"}):
            for item in itemAll.findAll('li', {'class': 'direct_joblisting'}):
                for a in item.findAll('a'):
                    job_specific_url = urljoin(career_page_url, a.get('href'))

                for t in item.findAll('span', {"class": "resultHeader"}):
                    job_title = t.text.strip()

                for l in item.findAll('span', {"class": "hiringPlace"}):
                    job_location = l.text.strip().replace("\n", "")

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
    except Exception as error:

        print(error)

        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)

    return df


def tno(company_name, companies_details):

    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    df = pd.DataFrame(columns=fields_needed)

    html = requests.get(career_page_url).text
    soup = BS(html, 'lxml')

    try:

        for itemAll in soup.findAll('section', {'class': 'block__landing--vacancies'}):
            for item in itemAll.findAll('a'):
                job_specific_url = urljoin(career_page_url, item.get('href'))

                for n in item.find('h3'):
                  job_title = n
                for l in item.find('li'):
                  job_location = l

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
    except Exception as error:

        print(error)

        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)

    return df


def visenze(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    try:
        html = requests.get(career_page_url).text
        soup = BS(html, 'lxml')
        df = pd.DataFrame(columns=fields_needed)
        for itemAll in soup.findAll('div', {'class': 'container'}):
            for item in itemAll.findAll('div', {'class': ['col-12', 'aos-init', 'aos-animate']}):
                job_title_raw = item.find('h3')
                try:
                    job_title= item.find('h3').get_text()
                    #print(job_title)
                except AttributeError as e:
                    #print(repr(e))
                    continue
                for z in item.findAll('a'):
                    job_specific_url = z.get('href')
                if job_title_raw!= None:
                    i = item.find('p')
                    s = []
                    for a in i.findAll('span'):
                        s.append([a.text])
                    job_department = s[0][0]
                    job_location = s[1][0]
                    job_description = np.nan
                    job_type = np.nan
                    years_of_experience = np.nan
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


def axis(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    try:
        html = requests.get(career_page_url).text
        soup = BS(html, 'lxml')
        df = pd.DataFrame(columns=fields_needed)
        for itemAll in soup.findAll('td', {'class': 'views-field-field-workday-application-url'}):
            job_location = np.nan
            for a in itemAll.findAll('a'):
                job_title = a.text
                job_specific_url = a.get('href')
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
    except Exception as error:
        print(error)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)
    return df


def vathos(company_name, companies_details):
    career_page_url = companies_details[company_name]['career_page_url']
    sector = companies_details[company_name]['sector']

    print(company_name)

    try:
        html = requests.get(career_page_url).text
        soup = BS(html, 'lxml')
        df = pd.DataFrame(columns=fields_needed)
        for item in soup.findAll('div', {'class': 'vc_tta-panel'}):
            job_title = item.find('span').text
            job_description = item.find('div', {'class': 'wpb_wrapper'}).text
            job_description = job_description.replace('\n', '')
            job_description = job_description.replace('Read more', '')
            for a in item.findAll('a'):
                job_specific_url = urljoin(career_page_url, a.get('href'))
            job_location = np.nan
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

    except Exception as error:
        print(error)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)
    return df

#abto('abto software',companies_details)
#kritikal('KritiKal Solutions',companies_details)
#atlas_elektronik('atlas elektronik',companies_details)
#tobii('tobii',companies_details)
#philips('philips',companies_details)
#tno('TNO',companies_details)
#visenze('visenze',companies_details)
#axis('axis communications',companies_details)
#vathos('Vathos Robotics',companies_details)

