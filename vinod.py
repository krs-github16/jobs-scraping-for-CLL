#!/usr/bin/env python
# coding: utf-8

import requests
from scrapy.selector import Selector
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

def greenhouse_platform(company_name,companies_details):

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    print(company_name)
    
    try:
        job_type, years_of_experience = [''] * 2
        count = 0
        if 'boards' in career_page_url:
            if '&b=http' in career_page_url:
                domain = career_page_url.strip('/').split('&b=http')[0].split('=')[-1]
            elif 'b=http' in career_page_url:
                domain = career_page_url.strip('/').split('b=http')[0].split('=')[-1].replace('&amp;', '').strip()
            elif '?for=' in career_page_url:
                domain = career_page_url.strip('/').split('=')[-1]
            else:
                if '#' in career_page_url:
                    domain = career_page_url.strip('/').split('/')[-1].split('#')[0]
                else:
                    domain = career_page_url.strip('/').split('/')[-1]
            api_url = 'https://boards-api.greenhouse.io/v1/boards/%s/jobs?content=true' % (domain.strip())
        else:
            if 'www' in career_page_url or 'tourlane' in career_page_url:
                domain = career_page_url.strip('/').split('/')[2].split('.')[1]
            else:
                domain = career_page_url.strip('/').split('/')[2].split('.com')[0]
                if '.' in domain:
                    domain = domain.split('.')[-1]
            api_url = 'https://api.greenhouse.io/v1/boards/%s/jobs?content=true' % domain.strip()
        df = pd.DataFrame(columns=fields_needed)
        js_response = requests.get(api_url).json()
        jobs_info = js_response.get('jobs', [])
        for job in jobs_info:
            job_title = job.get('title', '')
            job_specific_url = job.get('absolute_url', '')
            try:
                job_department = job.get('departments', [])[0].get('name', '')
            except:
                job_department = ''
            job_location = job.get('location', {}).get('name', '')
            desc = job.get('content', '')
            sel = Selector(text=desc)
            job_desc_text = ''.join(sel.xpath('//text()').extract()).strip()
            sel1 = Selector(text=job_desc_text)
            job_description = ''.join(sel1.xpath('//text()').extract()).replace('\n', '' ).replace(u'\xa0', '').strip()
            df = df.append(pd.Series(data=[company_name, job_title, job_description, job_location,
                               job_type, years_of_experience, job_department, job_specific_url,
                               career_page_url,sector], index=fields_needed), ignore_index=True)
        return df

    except Exception as error:
        print(error)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)

def workday_cognex(company_name,companies_details):

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    print(company_name)

    count=0
    job_description, job_type, years_of_experience, job_department = [''] * 4
    try:
        headers = {
            'Accept': 'application/json,application/xml'
        }

        params = (
            ('clientRequestID', 'ae57d4dfd821446ba7863a0113c5bd2b'),
        )
        df = pd.DataFrame(columns=fields_needed)
        response = requests.get('https://cognex.wd1.myworkdayjobs.com/en-US/External_Career_Site', headers=headers,params=params).json()

        jobs = response.get('body', {}).get('children', [])[0].get('children', [])[0].get('listItems', [])

        for job in jobs:
            job_title = job.get('title', {}).get('instances', [])[0].get('text', '')
            job_specific_url = 'https://cognex.wd1.myworkdayjobs.com' + job.get('title', {}).get('commandLink', '')
            job_location = job.get('subtitles', [])[1].get('instances', [])[0].get('text', '')
            df = df.append(pd.Series(data=[company_name, job_title, job_description, job_location,
                                           job_type, years_of_experience, job_department, job_specific_url,
                                           career_page_url,sector], index=fields_needed), ignore_index=True)
        return df
    except Exception as error:
        print(error)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)


def kla_tencor(company_name,companies_details):

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    print(company_name)

    count, page = 0, 1
    job_description, job_type, years_of_experience, job_department = [''] * 4
    try:
        df = pd.DataFrame(columns=fields_needed)
        while True:
            response = requests.get('https://careers.kla-tencor.com/jobs/search?page=%s#' % str(page))
            sel = Selector(response)
            nodes = sel.xpath('//div[@class="jobs-section__item"]//div[@class="row"]')
            if not nodes:
                print("<<<<<<<<<<<<<< Pagination completed %s >>>>>>>>>>>>>>>>" % page)
                break
            for node in nodes:
                job_title = ''.join(node.xpath('./div[@class="large-5 columns"]//h2//a//text()').extract()).strip()
                job_specific_url = ''.join(node.xpath('./div[@class="large-5 columns"]//h2//a/@href').extract()).strip()
                job_location = ''.join(node.xpath('./div[@class="large-3 columns"]/text()').extract()).strip()
                job_department = ''.join(node.xpath('./div[@class="large-2 columns"][2]/text()').extract()).strip()
                df = df.append(pd.Series(data=[company_name, job_title, job_description, job_location,
                       job_type, years_of_experience, job_department, job_specific_url,
                       career_page_url,sector], index=fields_needed), ignore_index=True)
            page += 1
        return df
    except Exception as error:
        print(error)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)
        


def hp(company_name,companies_details):

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    print(company_name)

    count = 0
    try:
        params = (
        ('api-version', '1.0'),
        )

        data1 = '{"FilterOnly":"false","ClientId":17960,"SiteId":1,"JobQuery":{},"HistogramFacets":{"CustomAttributeHistogramFacets":[{"Key":"ShortTextField1","StringValueHistogram":"true"},{"Key":"ShortTextField2","StringValueHistogram":"true"},{"Key":"City","StringValueHistogram":"true"},{"Key":"FullCountryName","StringValueHistogram":"true"},{"Key":"FullStateName","StringValueHistogram":"true"}]},"sid":"0dd103bf-505e-45ae-ac4d-654aa1efcfbc","uid":"32462de5-816a-4865-8412-883eec8dc693","PageSize":100,"Offset":0,"JobFields":"UrlJobTitle,JobId,GoogleJobName,JobTitle,ShortTextField1,ShortTextField8,LongTextField2"}'
        offset = 0
        df = pd.DataFrame(columns=fields_needed)
        job_description, job_type, years_of_experience, job_department, job_location = [''] * 5
        while True:
            data = json.loads(data1)
            data.update({'offset': str(offset)})
            response = requests.post('https://sfapi.azure-api.net/cloudjobs/odata/Search', params=params, data=json.dumps(data)).json()
            jobs_list = response.get('matchingJobs', [])
            if not jobs_list:
                print("<<<<<<<<<<<<<< Pagination completed >>>>>>>>>>>>>>>")
                break
            for job in jobs_list:
                count += 1
                job_title = job.get('jobTitle', '')
                job_category = job.get('shortTextField1', '')
                job_location = job.get('shortTextField8', '')
                job_specific_url = 'https://jobs.hp.com/en-us/showjob/jobid/%s' % job.get('jobId', '')
                df = df.append(pd.Series(data=[company_name, job_title, job_description, job_location,
                       job_type, years_of_experience, job_department, job_specific_url,
                       career_page_url,sector], index=fields_needed), ignore_index=True)
            offset += 100
        return df
    except Exception as error:
        print(error)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)


def lever_api(company_name,companies_details):

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    count = 0
    df = pd.DataFrame(columns=fields_needed)
    job_description, job_type, years_of_experience, job_department, job_location = [''] * 5
    try:
        if 'www' in career_page_url:
            domain = career_page_url.strip('/').split('/')[2].split('.')[1]
        elif 'jobs.' in career_page_url:
            domain = career_page_url.strip('/').split('/')[-1]
        else:
            domain = career_page_url.strip('/').split('/')[2].split('.com')[0]
        response = requests.get('https://api.lever.co/v0/postings/%s?group=team&mode=json' % domain).json()
        for job_response in response:
            jobs_data = job_response.get('postings', [])
            for job in jobs_data:
                job_title = job.get('text', '')
                job_specific_url = job.get('hostedUrl', '')
                job_description = job.get('descriptionPlain', '')
                job_location = job.get('categories', {}).get('location', '')
                job_type = job.get('categories', {}).get('commitment', '')
                job_department = job.get('categories', {}).get('team', '')
                count += 1
                df = df.append(pd.Series(data=[company_name, job_title, job_description, job_location,
                                               job_type, years_of_experience, job_department, job_specific_url,
                                               career_page_url,sector], index=fields_needed), ignore_index=True)

        return df
    except Exception as error:
        print(error)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)


def hire_withgoogle_api(company_name,companies_details):

    career_page_url = companies_details[company_name]['career_page_url']
    sector =  companies_details[company_name]['sector']

    df = pd.DataFrame(columns=fields_needed)
    if 'withgoogle' in career_page_url:
        domain = career_page_url.strip('/').split('/')[-1]
    else:
        domain = career_page_url.split('/')[2].replace('.', '')
    job_description, job_type, years_of_experience, job_department, job_location = [''] * 5
    count = 0
    try:
        response = requests.get('https://hire.withgoogle.com/v2/api/t/%s/public/jobs' % domain).json()
        for job in response:
            job_title = job.get('title', '').strip()
            job_specific_url = job.get('url', '')
            descp_data = job.get('description', '')
            sel = Selector(text=descp_data)
            job_description = ' '.join(sel.xpath('//text()').extract()).strip()
            job_location = job.get('jobLocation', {}).get('address', '').get('addressLocality', '') + ', ' + \
                           job.get('jobLocation', {}).get('address', '').get('addressRegion', '') + ', ' + \
                           job.get('jobLocation', {}).get('address', '').get('addressRegion', '')
            job_type = job.get('employmentType', '')
            job_department = job.get('hiringOrganization', {}).get('department', {}).get('name', '')
            count += 1
            df = df.append(pd.Series(data=[company_name, job_title, job_description, job_location,
                                           job_type, years_of_experience, job_department, job_specific_url,
                                           career_page_url,sector], index=fields_needed), ignore_index=True)

        return df
    except Exception as error:
        print(error)
        print("<<<<<<<<<<<<<<<<<<<<< This company got an issue %s >>>>>>>>>>>>>>>>>>>>>>>" % career_page_url)