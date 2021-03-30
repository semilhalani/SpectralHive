from selenium.webdriver.remote.webdriver import WebDriver

from core import TutorialBarScraper

from bs4 import BeautifulSoup

import requests, datetime

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
directory = "Course_files\\"

tb_scraper = TutorialBarScraper()
flag = course_counter = 0
old_file = directory + "allCourses.txt"
present_date = datetime.datetime.now()
new_file = directory + present_date.strftime("%b") + "_" + present_date.strftime("%d") + "_Courses.txt"

def get_old_course_details(file_name):
    file = open(file_name, "r", encoding="utf-8")
    file_data = file.read().split("\n")
    print(len(file_data))
    print(len(file_data)//4)
    course_names = []
    course_urls = []
    for i in range(len(file_data)):
        if i>0: 
            if ((i+4)%4)==0:
                course_names.append(file_data[i-4].split(". ")[1])
                course_urls.append(file_data[i-2])
    """print("\n\nCourse Names: ")
    for i in range(5):
        print(str(i) + ". " + course_names[i])
    print("\n\nCourse Links: ")
    for i in range(5):
        print(str(i) + ". " + course_urls[i])"""
    return course_names, course_urls

def get_new_course_details(counter, course_url):
    flag=0
    titleText = headlineText = ""
    counter = counter + 1
    req = requests.get(course_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    #print(course_url)
    titleTag = soup.find("h1", { "data-purpose" : "lead-title" })
    if titleTag == None:
        counter = counter - 1
    else:
        titleText = titleTag.text.strip()
        headlineTag = soup.find("div", { "data-purpose" : "lead-headline" })
        headlineText = headlineTag.text.strip()
        flag=1
    return flag, counter, titleText, headlineText
            
def save_new_course_details(course_number, course_website, course_title, course_description):
    if course_number==1:
        new_course_file.write(str(course_number) + ". " + course_title + "\n" + "Description: " + course_description +"\n" + course_website + "\n")
    else:
        new_course_file.write("\n" + str(course_number) + ". " + course_title + "\n" + "Description: " + course_description +"\n" + course_website + "\n")
    print(str(course_number) + ". " + course_title)


old_courses_names, old_course_links = get_old_course_details(old_file)

new_course_file = open(new_file, "w", encoding="utf-8")
print("99. All Courses")
choice = "99" #input('Please select what category you want? :')

while True:
    b=0
    udemy_course_links = tb_scraper.run(choice)
    for course_link in udemy_course_links:
        if  "bit.ly" in course_link:
            print("\n" + course_link + " is invalid\n")
        elif course_link in old_course_links:
            print("\n" + course_link + " is repeated\n")
            b=1
            break
        else:
            flag, course_counter, course_title, course_description = get_new_course_details(course_counter, course_link)
            if flag==1:
                if course_title in old_courses_names:
                    print("\n" + course_title + " is repeated")
                    course_counter = course_counter - 1
                else:
                    save_new_course_details(course_counter, course_link, course_title, course_description)
    if b==1:
        break
