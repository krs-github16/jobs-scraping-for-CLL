import numpy as np
import pandas as pd
import requests, re
import datetime
import json
import time
from selenium import webdriver

from bs4 import BeautifulSoup as BS
from urllib.request import urljoin

from flashtext import KeywordProcessor

#from pytablewriter import MarkdownTableWriter

from krs import niramai,locus, oneorigin, alphasense, sayint, casetext
from manoj import zebra, episource, vicarious, uipath, angel_co, insilico, loginextsolutions, appen, zymergen, kore, nvidia
from vinod import greenhouse_platform, workday_cognex, kla_tencor, hp, \
    lever_api, hire_withgoogle_api, apply_workable
from jagadeesh import Haptik_AI, Gramener, Boost_AI, Lumiq_FreshTeam, neurala,\
    honeywell, IHSMarkit, x_ai, geosys, unbxd, hover, mroads, HHMI_Janelia, Kaggle, philips, GE_Global, Cella_Vision,\
    BitRefine,orbital_insight
from sitaram import abto,kritikal,atlas_elektronik,tobii,philips,tno,visenze,\
    axis,vathos, Artivatic, Pleiades, imageMetrics,sentiosports, L3Harris


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r) %2.2f sec' % \
              (method.__name__, kw, te - ts))
        return result

    return timed


# executable_path=r'chromedriver_win32\chromedriver.exe'

companies_md_url='https://github.com/colearninglounge/co-learning-lounge/blob/master/Technology/Artificial%20Intelligence/companies.md'

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

positive_key_words_list = ['deep learning', 'dl', 'machine learning', 'ml', 'nlp', 'natural language processing', 'computer vision',
           'cv', 'data scientist', 'ds', 'business analyst', 'data engineer', 'research engineer', 'data visualization',
           'data analyst',  'database admin','data architect', 'statistician', 'data and analytics',
           'chatbot', 'conversational AI', 'artificial intelligence', 'AI','business intelligence analyst','python',  'data science',
          'data engineering',  'data analist', 'data infrastructure','datascience','natural language understanding', 'language modeling','imaging scientist']

negative_key_words_list = ['front end','bioinformatics','front-end']

def companiesmd_to_dict(companies_md_url):

    html = requests.get(companies_md_url).text

    soup = BS(html, 'lxml')

    allh2s = soup.find(id="readme").find_all('h2')

    alluls = soup.find(id="readme").find_all('ul')

    dictionary={}

    for allh2, allul in zip(allh2s, alluls):

        sector = allh2.get_text()

        allls = allul.find_all('li')

        for alll in allls:

            career_page_url = alll.a.get('href')

            company_name = alll.a.get_text()

            dictionary[f'{company_name}']={'sector':sector,'career_page_url':career_page_url}

    return dictionary

def in_key_words_list(item,key_words_list):

    keyword_processor = KeywordProcessor()

    keyword_processor.add_keywords_from_list(key_words_list)

    found = keyword_processor.extract_keywords(item)

    if found:
        return found, 'Yes'
    else:
        return "No"

if __name__=='__main__':

    frames = []
    date=datetime.datetime.today().strftime('%B %d, %Y at %I %p')

    companies_details = companiesmd_to_dict(companies_md_url)
    print(companies_details)

    for index,func in enumerate([
                                 angel_co('streamingo.ai',companies_details),
                                 angel_co('orbo.ai',companies_details),
                                 zymergen('zymergen', companies_details),
                                 kore('kore.ai', companies_details),
                                 nvidia('nVidia',companies_details),
                                philips('philips healthcare', companies_details),
                                GE_Global('GE Global Research', companies_details),
                                Cella_Vision('Cella Vision', companies_details),
                                BitRefine('BitRefine Group', companies_details),
                                orbital_insight('orbital insight', companies_details),
                                 apply_workable('Pony.ai', companies_details),
                                 HHMI_Janelia('HHMI',companies_details),
                                 Kaggle('Kaggle', companies_details),
                                 insilico('inSilico medicine', companies_details),
                                 loginextsolutions('logiNext', companies_details),
                                 appen('figure eight', companies_details),
                                 Artivatic("artivatic.ai", companies_details),
                                 Pleiades("pleiades tech", companies_details),
                                 imageMetrics("Image Metrics", companies_details),
                                 sentiosports("SentioSports", companies_details),
                                 L3Harris("exelis vis", companies_details),
                                 locus('locus.sh',companies_details),
                                 niramai('niramai',companies_details),
                                 oneorigin('oneorigin',companies_details),
                                 alphasense('alphaSense',companies_details),
                                 zebra('Zebra medical vision',companies_details),
                                 episource('Episource LLC',companies_details),
                                 vicarious('vicarious',companies_details),
                                 uipath('UI path',companies_details),
                                 greenhouse_platform('immersive labs', companies_details),
                                 workday_cognex('COGNEX', companies_details),
                                 kla_tencor('Kla Tencor', companies_details),
                                 hp('hp labs',companies_details),
                                 Haptik_AI('haptik.ai',companies_details),
                                 Gramener('Gramener',companies_details),
                                 Boost_AI('boost.ai',companies_details),
                                 Lumiq_FreshTeam('lumiq.ai',companies_details),
                                 sayint('sayint.ai',companies_details),
                                 casetext('casetext',companies_details),
                                 greenhouse_platform('tempus', companies_details),
                                 greenhouse_platform('soundhound', companies_details),
                                 greenhouse_platform('rasa', companies_details),
                                 greenhouse_platform('clarifai', companies_details),
                                 greenhouse_platform('freenome', companies_details),
                                 greenhouse_platform('nauto', companies_details),
                                 neurala('neurala',companies_details),
                                 honeywell('honeywell',companies_details),
                                 IHSMarkit('IHS Markit',companies_details),
                                 x_ai('x.ai',companies_details),
                                 abto('abto software',companies_details),
                                 kritikal('KritiKal Solutions',companies_details),
                                 atlas_elektronik('atlas elektronik',companies_details),
                                 tobii('tobii',companies_details),
                                 philips('philips',companies_details),
                                 tno('TNO',companies_details),
                                 visenze('visenze',companies_details),
                                 axis('axis communications',companies_details),
                                 vathos('Vathos Robotics',companies_details),
                                 greenhouse_platform('aeye', companies_details),
                                 greenhouse_platform('C3', companies_details),
                                 lever_api('openAI',companies_details),
                                 hire_withgoogle_api('cognitive scale',companies_details),
                                 hire_withgoogle_api('avaamo',companies_details),
                                 angel_co('niki.ai',companies_details),
                                 angel_co('vernacular.ai',companies_details),
                                 angel_co('saarthi.ai',companies_details),
                                 angel_co('Ori',companies_details),
                                 angel_co('floatbot.ai',companies_details),
                                 angel_co('Butterfly Network',companies_details),
                                 angel_co('arya.ai',companies_details),
                                 angel_co('pixuate',companies_details),
                                 angel_co('couture.ai',companies_details),
                                 geosys('geosys',companies_details),
                                 unbxd('UNBXD',companies_details),
                                 hover('hover',companies_details),
                                 mroads('mroads',companies_details),
                                 greenhouse_platform('GumGum', companies_details),
                                 greenhouse_platform('iris automation', companies_details),
                                 hire_withgoogle_api('imimtek',companies_details)
                                 ],1):

        # print(index,func.shape)
        frames.append(func)

    jobs_df = pd.concat(frames, axis=0, ignore_index=True)

    #jobs_df = pd.read_excel(r'outputs//all jobs.xlsx')

    jobs_df['in_key_words_list'] = jobs_df['Job Title'].apply(lambda s: in_key_words_list(str(s).strip(), positive_key_words_list))

    jobs_df['out_key_words_list'] = jobs_df['Job Title'].apply(lambda s: in_key_words_list(str(s).strip(), negative_key_words_list))

    jobs_df['job title length'] = jobs_df['Job Title'].apply(len)

    jobs_df.to_excel(r'outputs//'+'all jobs.xlsx', sheet_name=f'{date}',index=False)

    max_length = 65

    jobs_df = jobs_df[(jobs_df['in_key_words_list']!='No') & (jobs_df['out_key_words_list']=='No') & (jobs_df['job title length']<=max_length)].drop(columns=['in_key_words_list','out_key_words_list','job title length']).reset_index()

    jobs_df['Company Name'] = "[" + jobs_df['Company Name'].astype(str) + "]" + "(" + jobs_df['Career Page URL'].astype(str) + ")"

    jobs_df['Job Title'] = "[" +jobs_df['Job Title'].astype(str) +"]" +"(" +jobs_df['Job Specific URL'].astype(str) +")"

    jobs_df = jobs_df[['Market/Sector','Company Name','Job Title','Job Location']].sort_values(by=['Market/Sector','Company Name'], ascending=True).reset_index(drop=True)

    jobs_df.to_excel(r'outputs//'+'filtered jobs in required format.xlsx', sheet_name=f'{date}',index=False)

    print('end')


#df.groupby(['name','month'])['text'].apply(lambda x: ','.join(x)).reset_index()
