import requests
import time
import calendar 
import sys
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import mysql.connector
import math


courseCodes = ["AB", "AF", "AN", "AR", "AS", "BF", "BI", "BU", "CC", "CH", "CL", "CP", "CS", "DD", "DH", "EC", "EM", "EN", "ES", "EU", "FR", "FS", "GC", "GG", "GL", "GM", "GS", "GR", "HD", "HE", "HI", "HN",
               "HP", "HR", "HS", "ID", "IT", "KP", "KS", "LA", "LL", "LY", "OL", "MA", "MB", "MI", "ML", "MX", "MU", "MZ", "NO", "PP", "PC", "PD", "PO", "PS", "RS", "SC", "SE", "SL", "ST", "SY", "SP", "UU", "UX", "YC"]

courses = []
#getting time
ts = calendar.timegm(time.gmtime())

#connecting to database
mydb = mysql.connector.connect(
  host="db-mysql-tor1-86354-do-user-3862566-0.b.db.ondigitalocean.com",
  user="cp465",
  password="fskjd3njkfds8jk3ASDFuq38",
  database='cp465',
  port="25060"
)
cursor = mydb.cursor(buffered=True)

#term = sys.argv

#temp input until I know what system arguments to look for
term = input("enter term: ")


if term=="202005":
    term_name = "Spring 2020"
elif term=="202009":
    term_name = "Fall 2020"
elif term=="202101":
    term_name = "Winter 2021"
else:
    term_name = "Spring 2021"

sql = "INSERT INTO semester (name) VALUE (%s)"
val = (term_name,)
cursor.execute(sql, val)    
mydb.commit()

for i in range(len(courseCodes)):
    for x in range(8):     
        
        response = requests.get("https://scheduleme.wlu.ca/vsb/add_suggest.jsp?term=" + str(term) +"&cams=C_K_T_V_W_Z_CC_G_X_Y_MC&course_add=" +
                                courseCodes[i] + "&page_num=" + str(x) + "&_=" + str(ts))
        soup = BeautifulSoup(response.content, 'html.parser')
       

        #term_one = soup.find(id="term_202005")
        #term_two = soup.find(id="term_202009")
        #term_three = soup.find(id="term_202101")
        #term_four = soup.find(id="term_202105")

        for y in range(7):
            try:
                temp = soup.find(id=y+1).get_text()
                temp = temp.replace(" ", "-").upper()
                courses.append(temp)
            except:
                continue

for course in courses:
    ts = calendar.timegm(time.gmtime())
    t = (math.floor((ts*1000)/60000)) % 1000
    e = t % 3+t % 29+t % 42
    
    #                             https://scheduleme.wlu.ca/vsb/getclassdata.jsp?term=202009&course_1_0=BU-127&rq_1_0=null&t=802&e=24&nouser=1&_=1618248019531
    depthResponse = requests.get("https://scheduleme.wlu.ca/vsb/getclassdata.jsp?term="+str(term)+"&course_1_0=" + str(course) + "&rq_1_0=null&t="+str(t)+"&e="+str(e)+"&nouser=1&_=" + str(ts))
    soup = BeautifulSoup(depthResponse.content, 'html.parser')

    #print(depthResponse.content)
    try: 
        title = soup.course.attrs['title']
        description = soup.course.attrs['desc']
        faculty = soup.course.attrs['faculty']
        prof = soup.block.attrs['teacher']
        credits = soup.block.attrs['credits']
        section = soup.block.attrs['disp']
        online = True #everything online
        in_person = False
        capacity = 150

        queryprof = "SELECT * FROM professor WHERE name=(%s)"  
        val = (prof,)
        cursor.execute(queryprof, val)
        results = cursor.fetchall()
        
        if(len(results) == 0):
            sql = "INSERT INTO professor (name) VALUE (%s)"
            val = (prof,)
            #print(queryprof)
            cursor.execute(sql, val)
            prof_id = cursor.lastrowid
        else:
            prof_id = results[0][0]

        querydept = "SELECT * FROM department WHERE code=(%s)"
        val = (faculty,)
        cursor.execute(querydept, val)
        results = cursor.fetchall()

        if(len(results) == 0):
            sql = "INSERT INTO department (code, name) VALUE (%s, %s)"
            val = (faculty, "temp")
            cursor.execute(sql, val)
            department_id = cursor.lastrowid
        else:
            department_id = results[0][0]

        sql = "INSERT INTO course (title, department, professor, description, semester, online, in_person, room, credits, capacity, space_left, code)" \
            "VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (title, department_id, prof_id, description, term, online, in_person, 0, credits, capacity, 0, course)
        cursor.execute(sql, val)
        mydb.commit()
        print(course + " added")
    except Exception as e:
        print(e)

""" +--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int          | NO   | PRI | <null>  | auto_increment |  x
| title        | varchar(128) | NO   |     | <null>  |                |  x
| department   | int          | NO   |     | <null>  |                |  x
| professor    | int          | NO   |     | <null>  |                |  x
| description  | text         | NO   |     | <null>  |                |  x
| semester     | int          | NO   |     | <null>  |                |  x
| online       | tinyint(1)   | NO   |     | <null>  |                |  x
| room         | int          | NO   |     | <null>  |                |  not applicable, everything online
| credits      | int          | NO   |     | <null>  |                |  x
| capacity     | int          | NO   |     | <null>  |                |  x
+--------------+--------------+------+-----+---------+----------------+ """