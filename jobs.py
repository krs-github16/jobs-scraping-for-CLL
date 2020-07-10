import pandas as pd
import re

df = pd.read_excel(r'outputs//filtered jobs in required format.xlsx')

import datetime
utc_datetime = datetime.datetime.utcnow()
utc_datetime = utc_datetime.strftime("%Y-%m-%d %H:%M:%S")

current_timestamp = utc_datetime

header = """# Active AI jobs 
###### _Last updated on {timeStamp}_

Welcome to the [**Co-learning Lounge**](https://colearninglounge.com). This page contains active AI jobs scrapped from the career page of [curated AI companies](companies.md) by our community so that you don't have to go anywhere on the internet to hunt for jobs. As it is frustrating to visit so many websites frequently and end up getting an outdated job. We VALUE your TIME hence we do that FOR YOU so that you FOCUS on applying for a job not searching for it.

#### Support Us <br>
✅    Give a star to the repo and add yourself to the watch list to never miss any update. <br>
    ![Support Us](CLL_Git_Star_watch.gif)<br>
✅    Update the missing company name here 👉 [AI companies](companies.md) <br>
✅    Subscribe to our YouTube channel and join our community. <br>
    <a href="https://bit.ly/CLLYT"> <img src="youtube.png" height="50" width="150" alt="YouTube"></a> 
    <a href="https://bit.ly/CLL_TG"> <img src="telegram.png" height="50" width="50" alt="Telegram"></a>
    <a href="https://bit.ly/CLL_FBG"> <img src="facebook.png" height="50" width="100" alt="Facebook"></a>  <br> <br>
***All the best for your job hunting 👍***"""

header = re.sub('{\w+}', utc_datetime, header)

grouped_by_domain = df.groupby('Market/Sector')

jobs_content = header

for domain_name, group_by_domain in grouped_by_domain:
    grouped_by_company = group_by_domain.groupby('Company Name')
    jobs_content = jobs_content + "\n ## " + domain_name.title()
    for company_name, group in grouped_by_company:
        jobs_content = jobs_content + "\n ### " + company_name
        for index, row in group.iterrows():
            jobs_content = jobs_content + "\n - " + row['Job Title'] + (", _" + str(row['Job Location']) + "_" if not pd.isnull(row['Job Location']) else "")

jobs_content = jobs_content + "\n \n"
footer = """#### Contributors
[Rajasekhara Reddy Kaluri](https://www.linkedin.com/in/raja-sekhara-reddy-kaluri-a8b7aa8b),[Vinod Kumar Mukku](https://www.linkedin.com/in/vinod-kumar-mukku-76a124121), [Manoj Biroj](https://www.linkedin.com/in/manoj-biroj), [Jagadeesh Chandra Kambampati](https://www.linkedin.com/in/jagadeesh-chandra-kambampati-99763a7a), [Sita Rama Rao](https://www.linkedin.com/in/venuturumilli-s-v-s-sita-rama-rao/) have contributed to this project.

#### Want to contribute?  <br>
[Check this](jobs.md#support-us-) """

jobs_content = jobs_content + footer

with open(r"outputs/jobs.md", "w",encoding='utf-8') as text_file:
    print(jobs_content, file=text_file)