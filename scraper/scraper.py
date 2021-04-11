import requests
import time
import calendar 
import sys
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

courseCodes = ["AB", "AF", "AN", "AR", "AS", "BF", "BI", "BU", "CC", "CH", "CL", "CP", "CS", "DD", "DH", "EC", "EM", "EN", "ES", "EU", "FR", "FS", "GC", "GG", "GL", "GM", "GS", "GR", "HD", "HE", "HI", "HN",
               "HP", "HR", "HS", "ID", "IT", "KP", "KS", "LA", "LL", "LY", "OL", "MA", "MB", "MI", "ML", "MX", "MU", "MZ", "NO", "PP", "PC", "PD", "PO", "PS", "RS", "SC", "SE", "SL", "ST", "SY", "SP", "UU", "UX", "YC"]

courses = []

ts = calendar.timegm(time.gmtime())

#term = sys.argv

#temp input until I know what system arguments to look for
term = input("enter term: ")


for i in range(len(courseCodes)):
    for x in range(8):     

        # TODO: make the term dynamic from a commandline argument
        #202105
        response = requests.get("https://scheduleme.wlu.ca/vsb/add_suggest.jsp?term=" + str(term) +"&cams=C_K_T_V_W_Z_CC_G_X_Y_MC&course_add=" +
                                courseCodes[i] + "&page_num=" + str(x) + "&_=" + str(ts))
        soup = BeautifulSoup(response.content, 'html.parser')
        #numCourses = soup.find('add_suggest', results="")

        term_one = soup.find(id="term_202005")
        term_two = soup.find(id="term_202009")
        term_three = soup.find(id="term_202101")
        term_four = soup.find(id="term_202105")

        #print(term_one, term_two, term_three, term_four)
        # print(numCourses)
        for y in range(7):
            try:
                temp = soup.find(id=y+1).get_text()
                courses.append(temp)
            except:
                continue
# print(soup.prettify())

for course in courses:
    print(course)

# TODO: save data to database
