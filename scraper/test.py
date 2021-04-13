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
cursor = mydb.cursor(buffered=True)
ts = calendar.timegm(time.gmtime())
#print(ts)
                             #https://scheduleme.wlu.ca/vsb/getclassdata.jsp?term=202009&course_1_0=CP-102&rq_1_0=null&t=922&e=64&nouser=1&_=1618254474
depthResponse = requests.get("https://scheduleme.wlu.ca/vsb/getclassdata.jsp?term=202009&course_1_0=CP-102&rq_1_0=null&t=328&e=44&nouser=1&_=" + str(ts))


soup = BeautifulSoup(depthResponse.content, 'html.parser')

title = soup.course.attrs['title']
description = soup.course.attrs['desc']
faculty = soup.course.attrs['faculty']
prof = soup.block.attrs['teacher']
credits = soup.block.attrs['credits']
section = soup.block.attrs['disp']
online = True #everything online
in_person = False
capacity = 150

queryprof = "SELECT * FROM professor WHERE name='"+prof+"'"
#queryprof = "SELECT * FROM professor"
    
cursor.execute(queryprof)
results = cursor.fetchall()
#print(results)
id = 1
if(len(results) == 0):
  sql = "INSERT INTO professor (name) VALUE (%s)"
  val = (prof,)
  #print(queryprof)
  cursor.execute(sql, val)
  prof_id = cursor.lastrowid
else:
  prof_id = results[0][0]

querydept = "SELECT * FROM department WHERE code='"+faculty+"'"
cursor.execute(querydept)
results = cursor.fetchall()

if(len(results) == 0):
  sql = "INSERT INTO department (code, name) VALUE (%s, %s)"
  val = (faculty, "temp")
  cursor.execute(sql, val)
  department_id = cursor.lastrowid
else:
  department_id = results[0][0]

term = 202101

sql = "INSERT INTO course (title, department, professor, description, semester, online, in_person, room, credits, capacity, space_left)" \
        "VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (title, department_id, prof_id, description, term, online, in_person, 0, credits, capacity, 0)
cursor.execute(sql, val)
mydb.commit()
queryprof = "SELECT * FROM professor"
cursor.execute(queryprof)
results = cursor.fetchall()    

print(results)
print(faculty)