import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as BS
from urllib.request import urljoin
import pdb
import re, json, time
from selenium import webdriver

chrome_path = r'C:\Users\krajasekhara\PycharmProjects\CLL jobs scraping\drivers\chromedriver_win32\chromedriver.exe'


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


def Haptik_AI(company_name,companies_details):

	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	html = requests.get(career_page_url).text
	soup = BS(html, 'lxml')

	df = pd.DataFrame(columns=fields_needed)
	# global df

	try:

		trs = soup.find('tbody', {'class': 'tab-content'}).find_all('tr')

	except:

		trs = []

	# print("===len==",len(trs))

	for job in trs[:-1]:

		try:
			tds = job.find_all('td')

			job_title = tds[0].get_text().strip()

			job_description = np.nan

			job_location = tds[1].get_text().strip()

			job_type = np.nan

			years_of_experience = np.nan

			job_department = np.nan

			job_specific_url = job.find('a')['href']

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


def Gramener(company_name,companies_details):

	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	html = requests.get(career_page_url).text
	soup = BS(html, 'lxml')

	df = pd.DataFrame(columns=fields_needed)
	# global df

	divs = soup.find_all('div', {'class': 'gallery-item'})
	# print("===len===",len(divs))

	for job in divs:

		try:

			job_title = job.find('h5').get_text().strip()

			job_description = np.nan

			job_location = job.find('div', {'class': 'custom_color_grey sm1'}).get_text().strip()

			job_type = np.nan

			years_of_experience = np.nan

			job_department = np.nan

			job_specific_url = job.find('a')['href']

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


def Boost_AI(company_name,companies_details):

	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	html = requests.get(career_page_url).text
	soup = BS(html, 'lxml')

	df = pd.DataFrame(columns=fields_needed)
	# global df

	trs = soup.find('table', {'id': 'jobsTable'}).find('tbody').find_all('tr')

	for job in trs:

		try:

			job_title = job.find('a').get_text().strip()

			job_description = np.nan

			job_location = job.find('td', {'class': 'jobtown'}).get_text().strip()

			job_type = np.nan

			years_of_experience = np.nan

			job_department = np.nan

			job_specific_url = job.find('a')['href']

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


def Lumiq_FreshTeam(company_name,companies_details):

	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	base = 'https://lumiq.freshteam.com/'

	html = requests.get(career_page_url).text
	soup = BS(html, 'lxml')

	df = pd.DataFrame(columns=fields_needed)
	# global df

	lis = soup.find('div', {'class': 'job-role-list'}).find('ul', {'class': 'open-list'}).find_all('li',
																								   {'class': None})

	for li in lis:

		li.find('span').decompose()

		job_department = li.find('h5').get_text().strip()

		jobs = li.find_all('li', {'class': 'heading'})

		for job in jobs:

			try:

				job_title = job.find('a').get_text().strip()

				job_description = np.nan

				loc_str = job.find('div', {'class': 'job-location'}).find('a').get_text().strip()

				job_location = loc_str.split('\n')[0].strip()

				job_type = loc_str.split('\n')[-1].strip()

				years_of_experience = np.nan

				href = job.find('a')['href']

				job_specific_url = urljoin(base, href)

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


def neurala(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	html = requests.get(career_page_url).text
	soup = BS(html, 'lxml')

	divs = soup.find_all('div', {'class': 'post-item'})

	df = pd.DataFrame(columns=fields_needed)

	for div in divs:

		try:
			job_title = div.find('a').get_text().strip()

			job_description = np.nan

			job_location = np.nan

			job_type = np.nan

			years_of_experience = np.nan

			job_department = np.nan

			job_specific_url = div.find('a')['href']

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


def honeywell(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	base = 'https://careers.honeywell.com/us/en/job/'
	link_format = 'https://careers.honeywell.com/us/en/search-results?from={}&s=1'
	count = 0

	df = pd.DataFrame(columns=fields_needed)

	for i in range(0, 2001, 10):
		try:
			link = link_format.format(i)
			res = requests.request('GET', link)
			html = res.text
			soup = BS(html, 'lxml')

			js = str(soup.find('script'))      #soup.find('script').get_text().strip()
			reg = re.search(r'"jobs":(.*),"aggregations"', js)
			data = reg.groups()[0]
			jobs = json.loads(data)

			for job in jobs:

				try:

					job_title = job['title']

					job_description = np.nan

					job_location = job['cityStateCountry']

					job_type = np.nan

					years_of_experience = np.nan

					job_department = job['category']

					job_seq = job['jobSeqNo']
					job_specific_url = base + job_seq

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

					count += 1

				except:
					pass

		except:
			pass

	return df


def IHSMarkit(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	base = 'https://careers.ihsmarkit.com/'
	link_format = 'https://careers.ihsmarkit.com/search.php?page={}'
	count = 0

	df = pd.DataFrame(columns=fields_needed)

	for page in range(30):

		try:

			link = link_format.format(page)
			html = requests.get(link).text
			soup = BS(html, 'lxml')

			jobs = soup.find('div', {'id': 'resultslist'}).find_all('div', {'class': 'result-wrap'})

			for job in jobs:

				try:
					job_title = job.find('h4').get_text().strip()

					job_description = np.nan

					job_location = job.find('h5', {'class': 'result-location'}).get_text().strip()

					job_type = np.nan

					years_of_experience = np.nan

					job_department = job.find('p', {'class': 'result-function'}).get_text().strip()

					href = job.find('a')['href']
					job_specific_url = urljoin(base, href)

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

					count += 1

				except:
					pass

		except:
			pass

	return df


def x_ai(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	html = requests.get(career_page_url).text
	soup = BS(html, 'lxml')

	df = pd.DataFrame(columns=fields_needed)

	try:

		jobs = soup.find('section', id=lambda x: x.startswith('jobs-block_')).find_all('article', {'class': 'job'})

	except:

		jobs = []

	for job in jobs:

		try:

			job_title = job.find('a').get_text().strip()

			job_description = np.nan

			job_location = np.nan

			job_type = np.nan

			years_of_experience = np.nan

			job_department = job.find('span', {'class': 'department'}).get_text().strip()

			job_specific_url = job.find('a')['href']

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


def geosys(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	html = requests.get(career_page_url).text
	soup = BS(html, 'lxml')

	divs = soup.find_all('div', {'class': 'lae-team-member-text'})

	df = pd.DataFrame(columns=fields_needed)

	for div in divs:
		try:
			job_title = div.find('a').get_text().strip()

			job_description = np.nan

			job_location = np.nan

			job_type = np.nan

			years_of_experience = np.nan

			job_department = np.nan

			job_specific_url = div.find('a')['href']

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


def unbxd(company_name, companies_details):

	career_page_url = companies_details[company_name]['career_page_url']   #'https://unbxd.com/careers/openings/'
	sector = companies_details[company_name]['sector']

	print(company_name)

	driver = webdriver.Chrome(executable_path=chrome_path)

	driver.minimize_window()

	driver.get(career_page_url)
	time.sleep(5)
	html = driver.page_source
	soup = BS(html, 'lxml')
	jobs = soup.find_all('div', {'class': 'rbox-opening-li'})

	df = pd.DataFrame(columns=fields_needed)

	for job in jobs:

		try:
			job_title = job.find('a').get_text().strip()

			job_description = np.nan

			job.find('span', {'class': 'rbox-opening-position-info'}).decompose()

			loc_str = job.find('div', {'class': 'rbox-job-shortdesc'}).get_text().strip()

			job_location = loc_str.replace('Location:', '')

			job_type = np.nan  # job.find('span',{'class':'rbox-opening-position-info'}).get_text().strip()

			years_of_experience = np.nan

			job_department = np.nan

			job_specific_url = job.find('a')['href']

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

	driver.close()

	return df


def hover(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	df = pd.DataFrame(columns=fields_needed)

	driver = webdriver.Chrome(executable_path=chrome_path)

	driver.minimize_window()
	driver.get(career_page_url)
	time.sleep(10)
	html = driver.page_source
	soup = BS(html, 'lxml')

	try:
		jobs = soup.find('table').find('tbody').find_all('tr')
	except:
		jobs = []

	base = 'https://hover.to/'
	for job in jobs:
		try:
			job_title = job.find('a').get_text().strip()

			job_description = np.nan

			tds = job.find_all('td')

			job_location = len(tds) > 2 and tds[2].get_text().strip() or ''

			job_type = np.nan

			years_of_experience = np.nan

			href = job.find('a')['href']

			job_department = len(tds) > 1 and tds[1].get_text().strip() or ''

			job_specific_url = urljoin(base, href)

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

	driver.close()

	return df


def mroads(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	df = pd.DataFrame(columns=fields_needed)

	driver = webdriver.Chrome(executable_path=chrome_path)

	driver.minimize_window()
	driver.get(career_page_url)
	time.sleep(5)
	html = driver.page_source
	soup = BS(html, 'lxml')
	base = 'https://www.mroads.com/'

	jobs = soup.find_all('li', {'class': 'Pagination__JobNavList__1xHhi'})

	for job in jobs:
		try:
			job_title = job.select('div[class*="JobNavigation__JobParagraph2"]')[0].get_text().strip()

			job_description = np.nan

			job_location = job.select('div[class*="JobNavigation__JobParagraph1"]')[0].get_text().strip()

			job_type = np.nan

			years_of_experience = np.nan

			job_department = np.nan

			href = job.find('a')['href']
			job_specific_url = urljoin(base, href)

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

	driver.close()
	return df


def HHMI_Janelia(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	df = pd.DataFrame(columns=fields_needed)

	html = requests.get(career_page_url).text
	soup = BS(html, 'lxml')
	divs = soup.find_all('div', {'class': 'cssAllJobListPosition'})
	base = 'https://hhmi-openhire.silkroad.com/'

	for div in divs:
		try:
			job_title = div.find('a').get_text().strip()

			job_description = np.nan

			href = div.find('a')['href']
			job_specific_url = urljoin(base, href)

			div.find('a').decompose()
			job_location = div.get_text().strip()

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


def Kaggle(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	df = pd.DataFrame(columns=fields_needed)

	driver = webdriver.Chrome(executable_path=chrome_path)
	driver.minimize_window()
	driver.get(career_page_url)
	time.sleep(10)
	html = driver.page_source
	soup = BS(html, 'lxml')
	base = 'https://www.kaggle.com/'
	jobs = soup.find_all('a', {'class': 'jobs-list-job'})

	for job in jobs:
		try:
			job_title = job.find('div', {'class': 'jobs-list-job__title-contents'}).get_text().strip()

			job_description = np.nan

			job_type = np.nan

			years_of_experience = np.nan

			job_department = np.nan

			job_location = job.find('span', {'class': 'jobs-list-job__location-text'}).get_text().strip()

			href = job['href']
			job_specific_url = urljoin(base, href)

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


		except:
			pass

	driver.close()
	return df


def philips(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	df = pd.DataFrame(columns=fields_needed)

	base = 'https://www.careers.philips.com/professional/apac/en/job/'
	link_format = 'https://www.careers.philips.com/professional/apac/en/search-results?keywords=?from={}&s=1'
	count = 0

	for i in range(0, 100, 50):
		try:
			link = link_format.format(i)
			res = requests.request('GET', link)
			html = res.text
			soup = BS(html, 'lxml')

			js = str(soup.find('script'))
			reg = re.search(r'"jobs":(.*),"aggregations"', js)
			data = reg.groups()[0]
			jobs = json.loads(data)
			for job in jobs:
				try:

					job_title = job['title']
					job_description = np.nan

					job_location = job['cityStateCountry']
					job_type = np.nan
					years_of_experience = np.nan
					job_department = job['category']
					job_seq = job['jobSeqNo']
					job_specific_url = base + job_seq

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
					count += 1

				except:
					pass

		except:
			pass

	return df


def GE_Global(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	df = pd.DataFrame(columns=fields_needed)

	base = 'https://jobs.gecareers.com/global/en/job/'
	link_format = 'https://jobs.gecareers.com/global/en/search-results?from={}&s=1'
	count = 0

	for i in range(0, 1000, 20):
		try:
			link = link_format.format(i)
			res = requests.request('GET', link)
			html = res.text
			soup = BS(html, 'lxml')

			js = str(soup.find('script'))
			reg = re.search(r'"jobs":(.*),"aggregations"', js)
			data = reg.groups()[0]
			jobs = json.loads(data)
			for job in jobs:
				try:

					job_title = job['title']
					job_description = np.nan

					job_location = job['cityStateCountry']

					job_type = np.nan
					years_of_experience = np.nan

					job_department = job['category']

					job_seq = job['jobSeqNo']
					job_specific_url = base + job_seq

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
					count += 1

				except:
					pass

		except:
			pass

	return df


def Cella_Vision(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	df = pd.DataFrame(columns=fields_needed)

	html = requests.get(career_page_url).text
	soup = BS(html, 'lxml')
	jobs = soup.find('div', {'class': 'job-listing-container'}).find_all('li')

	base = 'https://career.cellavision.com/'

	count = 0
	for job in jobs:
		try:
			job_title = job.find('span').get_text().strip()

			job_description = np.nan

			job_location = np.nan

			job_type = np.nan
			years_of_experience = np.nan

			job_department = np.nan

			href = job.find('a')['href']
			job_specific_url = urljoin(base, href)

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
			count += 1

		except:
			pass

	return df


def BitRefine(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	df = pd.DataFrame(columns=fields_needed)

	headers = {
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.64"}
	html = requests.get(career_page_url, headers=headers).text
	soup = BS(html, 'lxml')
	jobs = soup.find('div', {'class': 'moduletable'}).find_all('div', {'class': 'row-fluid'})

	base = 'https://bitrefine.group/'

	count = 0
	for job in jobs:
		try:
			job_title = job.find('h2').find('a').get_text().strip()

			job_description = np.nan

			job_location = np.nan

			job_type = np.nan
			years_of_experience = np.nan

			job_department = np.nan

			href = job.find('h2').find('a')['href']
			job_specific_url = urljoin(base, href)

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

			count += 1

		except:
			pass

	return df


def orbital_insight(company_name, companies_details):
	career_page_url = companies_details[company_name]['career_page_url']
	sector = companies_details[company_name]['sector']

	print(company_name)

	df = pd.DataFrame(columns=fields_needed)

	html = requests.get(career_page_url).text
	soup = BS(html, 'lxml')
	jobs = soup.find_all('div', {'class': 'card'})

	count = 0
	for job in jobs:
		try:
			job_title = job.find('h3').find('a').get_text().strip()

			job_description = np.nan

			job_location = job.find('h5').get_text().strip()

			job_type = np.nan

			years_of_experience = np.nan

			job_department = job.find('h5').findNext('p').get_text().strip()

			job_specific_url = job.find('h3').find('a')['href']

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
			count += 1

		except:
			pass

	return df



# Haptik_AI('Haptik','https://haptik.ai/careers/')
# Gramener('Gramener','https://gramener.com/careers/#?show=all')
# Boost_AI('Boost','https://web106.reachmee.com/ext/I002/1350/main?site=6&validator=21304e4cfc10bf6957ad60fe5e4eba40&lang=UK&ref=https%3a%2f%2fwww.boost.ai%2f&ihelper=https://www.boost.ai/career/')
# Lumiq_FreshTeam('Lumiq FreshTeam','https://lumiq.freshteam.com/jobs')
