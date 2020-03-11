import requests
from bs4 import BeautifulSoup
import time
import datetime
import MySQLdb

#SQL connection data to connect and save the data in
HOST = "114.34.237.146"
USERNAME = "root"
PASSWORD = ""
DATABASE = "Bump"
PORT = 3000
table = 'GigSource_copy'

all_activities_url = []
all_activities_database = []
page = 1
domain = 'https://streetvoice.com/venue/activities/all/0/'
start_time = time.time()

def get_time(job, end_time):
    print("%s: %.3f" % (job, end_time))

def get_content(domain, selector, page=1):
    query_string = {
        'page': page
    }
    html = requests.get(domain, params=query_string).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup.select(selector)

def to_timestamp(time_list):
    YMD_list = time_list[0].split(' ')
    dt_local = datetime.datetime.strptime(f'{YMD_list[0]}-{YMD_list[2].zfill(2)}-{YMD_list[4].zfill(2)} {time_list[2]}:00','%Y-%m-%d %H:%M:%S')
    ts = time.mktime(dt_local.timetuple()) + 1e-6 * dt_local.microsecond
    dt_utc = datetime.datetime.utcfromtimestamp(ts)
    return str(dt_utc)
  
html_activities = get_content(domain, '.live-item-info')

while len(html_activities) > 0:
    for activity in html_activities:
        url = activity.select('h3 a', href=True)[0]["href"]
        all_activities_url.append(f'https://streetvoice.com{url}')
    page += 1
    html_activities = get_content(domain, '.live-item-info', page)
    time.sleep(5)

end_time = time.time() - start_time
get_time('get_all_activities_url', end_time)

# --------------------------------------------------------------------

start_time = time.time()
all_activities_url = ['https://streetvoice.com/venue/activities/883/', 'https://streetvoice.com/venue/activities/844/']
for url in all_activities_url:
    soup_tmp = get_content(url, '#pjax-container')[0]
    # soup_tmp = BeautifulSoup(requests.get(url).text).select('#pjax-container')[0]
    all_activities_database.append({
        'title': soup_tmp.select('h1')[0].text,
        'artist': soup_tmp.select('h3:nth-of-type(4)')[0].text.strip(),
        'startTime': to_timestamp(soup_tmp.select('h3:nth-of-type(1)')[0].text.strip().split(' l ')),
        'website': url,
        'photo': soup_tmp.select('img')[0]['src'],
        'describe': str(soup_tmp.select('.article-block')[0]),
        'location': soup_tmp.select('h3:nth-of-type(2)')[0].text.strip().split('\n')[0].split('．')[1]
    })
    time.sleep(3)

end_time = time.time() - start_time
get_time('get_all_activity_content', end_time)

# --------------------------------------------------------------------

start_time = time.time()

db = MySQLdb.connect(host=HOST, user=USERNAME, db=DATABASE, port=PORT)
# prepare a cursor object using cursor() method
cursor = db.cursor()
columns = ', '.join(list(map(lambda prop: f'`{prop}`', all_activities_database[0].keys())))
placeholders = ", ".join(['{}'] * len(all_activities_database[0]))
sql = "insert into {table} ({columns}) values ({values});".format(table=table, columns=columns, values=placeholders)

for activity in all_activities_database:
    sql_string = sql.format(
        repr(activity.get('title')),
        repr(activity.get('artist')),
        repr(activity.get('startTime')), 
        repr(activity.get('website')), 
        repr(activity.get('photo')), 
        repr(activity.get('describe')), 
        repr(activity.get('location'))
    )
    try:
        db.ping(True)
        # Execute the SQL command
        cursor.execute(sql_string)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
        # disconnect from server
        db.close()

db.close()
end_time = time.time() - start_time
get_time('insert_all_activity', end_time)