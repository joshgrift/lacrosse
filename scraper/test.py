import requests
import time
import calendar 
import sys
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import mysql.connector


mydb = mysql.connector.connect(
  host="db-mysql-tor1-86354-do-user-3862566-0.b.db.ondigitalocean.com",
  user="cp465",
  password="fskjd3njkfds8jk3ASDFuq38",
  database='cp465',
  port="25060"
)

ts = calendar.timegm(time.gmtime())
#print(ts)
                             #https://scheduleme.wlu.ca/vsb/getclassdata.jsp?term=202009&course_1_0=CP-102&rq_1_0=null&t=922&e=64&nouser=1&_=1618254474
depthResponse = requests.get("https://scheduleme.wlu.ca/vsb/getclassdata.jsp?term=202009&course_1_0=CP-102&rq_1_0=null&t=47&e=25&nouser=1&_=" + str(ts))


soup = BeautifulSoup(depthResponse.content, 'html.parser')

title = soup.course.attrs['title']
description = soup.course.attrs['desc']
faculty = soup.course.attrs['faculty']
prof = soup.block.attrs['teacher']
credits = soup.block.attrs['credits']
section = soup.block.attrs['disp']

queryprof = "SELECT * FROM professor WHERE name='"+prof+"'"
#queryprof = "SELECT * FROM professor"
    
cursor = mydb.cursor(buffered=True)
cursor.execute(queryprof)
results = cursor.fetchall()
#print(results)
if(len(results) == 0):
    sql = "INSERT INTO professor (name) VALUE ('" + prof + "')"
    val = ("Stevie")
    #print(queryprof)
    cursor.execute(queryprof)
    print(sql)
    
mydb.commit()
results = cursor.fetchall()    
print(results)