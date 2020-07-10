from bs4 import BeautifulSoup as BS

import numpy as np
import pandas as pd
import requests
import datetime

companies_md_url = 'https://github.com/colearninglounge/co-learning-lounge/blob/master/Technology/Artificial%20Intelligence/companies.md'

def companies_md(companies_md_url):

    html = requests.get(companies_md_url).text

    soup = BS(html, 'lxml')

    allh2s = soup.find(id="readme").find_all('h2')

    alluls = soup.find(id="readme").find_all('ul')

    min_fields = ['Company Name', 'Market/Sector', 'Career Page URL']

    df = pd.DataFrame(columns=min_fields)

    for allh2, allul in zip(allh2s, alluls):

        sector = allh2.get_text()

        allls = allul.find_all('li')

        for alll in allls:

            career_page_url = alll.a.get('href')

            company_name = alll.a.get_text()

            df = df.append(pd.Series(data=[company_name,
                                           sector,
                                           career_page_url], index=min_fields), ignore_index=True)

    return df

if __name__=='__main__':

    date = datetime.datetime.today().strftime('%B %d, %Y at %I %p')

    companies_md_df=companies_md(companies_md_url)

    sector_counts_df = pd.DataFrame(companies_md_df.groupby('Market/Sector').count()['Company Name'].sort_values(ascending=False))

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(r'outputs//'+'companies.xlsx', engine='xlsxwriter')

    companies_md_df.to_excel(writer,sheet_name='company career page urls',index=False)

    sector_counts_df.to_excel(writer,sheet_name='sector_counts', index=True)

    writer.save()

    print('end')