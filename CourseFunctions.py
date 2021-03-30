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
presentDate = datetime.datetime.now()
today = presentDate.strftime("%d") + " " + presentDate.strftime("%b") + ", " + presentDate.strftime("%Y")
directoryName = "CourseFiles\\"

examFileName = "examCourses.txt"
designFileName = "designCourses.txt"
commerceFileName = "commerceCourses.txt"
marketingFileName = "marketingCourses.txt"
computerFileName = "computerCourses.txt"
technicalFileName = "technicalCourses.txt"
selfDFileName = "selfDevelopmentCourses.txt"
otherFileName = "otherCourses.txt"
courseFileNameList = [examFileName, designFileName, commerceFileName, marketingFileName, computerFileName, technicalFileName, selfDFileName, otherFileName]

def get_old_course_details(fileName):
    oldFile = open(fileName, "r", encoding="utf-8")
    oldData = oldFile.read().split("\n")
    courseTitles = []
    courseUrls = []
    print(len(oldData))
    for i in range(len(oldData)-1):
        if ((i+4)%4)==0:
            print(oldData[i])
            courseTitles.append(oldData[i].split(". ")[1])
            courseUrls.append(oldData[i+2])
    return courseTitles, courseUrls

def get_new_course_details(counter, course_url):
    flag=0
    titleText = ""
    headlineText = ""
    counter = counter + 1
    req = requests.get(course_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    titleTag = soup.find("h1", { "data-purpose" : "lead-title" })
    if titleTag == None:
        counter = counter - 1
    else:
        titleText = titleTag.text.strip()
        headlineTag = soup.find("div", { "data-purpose" : "lead-headline" })
        headlineText = headlineTag.text.strip()
        flag=1
    return flag, counter, titleText, headlineText

def save_new_course_details(course_number, courseUrl, courseTitle, courseDescription, newCourseFileName):
    if course_number==1:
        newCourseFile = open(newCourseFileName, "w", encoding="utf-8")
    else:
        newCourseFile = open(newCourseFileName, "a", encoding="utf-8")
    newCourseFile.write(str(course_number) + ". " + courseTitle + "\n" + "Description: " + courseDescription +"\n" + courseUrl + "\n\n")
    print(str(course_number) + ". " + courseTitle)

def getCourses(oldCourseFileName, newCourseFileName):
    tb_scraper = TutorialBarScraper()
    oldCourseNames, oldCourseUrls = get_old_course_details(oldCourseFileName)
    flag = 0
    courseCounter = 0
    choice = "99"
    while True:
        b=0
        newCourseUrls = tb_scraper.run(choice)
        for newCourseUrl in newCourseUrls:
            if  "bit.ly" in newCourseUrl:
                print("\n" + newCourseUrl + " is invalid\n")
            elif newCourseUrl in oldCourseUrls:
                print("\n" + newCourseUrl + " is repeated\n")
                b=1
                break
            else:
                flag, courseCounter, courseTitle, courseDescription = get_new_course_details(courseCounter, newCourseUrl)
                if flag==1:
                    if courseTitle in oldCourseNames:
                        print("\n" + courseTitle + " is repeated")
                        courseCounter = courseCounter - 1
                    else:
                        save_new_course_details(courseCounter, newCourseUrl, courseTitle, courseDescription, newCourseFileName)
        if b==1:
            break
    print("All new available courses are now successfully saved!")

def updateFiles(oldFileName, newFileName):
    oldFile = open(oldFileName, "r", encoding='utf-8')
    oldFileData = oldFile.read().split("\n")
    totalOldCourses = int((len(oldFileData))//4)
    newCourseNumber = totalOldCourses + 1
    #lastOldCourse = oldFileData[len(oldFileData)-2]
    oldFile.close()
    newFile = open(newFileName, "r", encoding='utf-8')
    newFileData = newFile.read().split("\n")
    #lastNewCourse = newFileData[len(newFileData)-2]

    oldFile = open(oldFileName, "a", encoding='utf-8')
    for data in newFileData:
        i = newFileData.index(data)
        if ((i+4)%4)==0:
            courseTitle= data.split(".")[1]
            firstLine = str(newCourseNumber) + "." + courseTitle
            if i==0:
                oldFile.write(firstLine)
            else:
                oldFile.write("\n" + firstLine)
            newCourseNumber = newCourseNumber + 1
        else:
            course_details = data
            oldFile.write("\n" + course_details)
    oldFile.close()
    newFile.close()
    print("Both Files are now successfully updated!")

def classify(fileName):
    exam = ['exam', 'exams', 'tests', 'preparation', 'interview', 'practice test', 'practice tests']
    design = ['draw', 'photoshop', 'photograhy', 'photo', 'edit', 'adobe', 'fiverr', 'color', 'colour', 'invideo', 'video', 'animation', 'effect', 'modeling']
    commerce = ['management', 'finance', 'financial', 'trade', 'trader', 'account', 'trading', 'sigma', 'recruiting', 'hr analytics', 'odoo']
    marketing = [ 'pinterest', 'marketing', 'instagram', 'sales']
    computer = ['html', 'css', 'python', 'java', 'php', 'javascript', 'c++', 'android', 'ios', 'django', 'flask', 'codeigniter', 'laravel', 'hibernate', 'angular', 'angularjs', 'react', 'reactjs', 'node', 'nodejs', 'gaming', 'web development', 'web design', 'hack','hacker', 'hacking', 'penetration testing', 'oscp', 'ceh', 'data science', 'data analytics', 'data analysis', 'cpanel', 'firebase', 'vue', 'vuejs', 'power bi', 'tableau', 'azure', 'nlp', 'cpu', 'jquery', 'c#', 'aws', 'cloud']
    technical = ['arduino', 'no code', 'no coding', 'without code', 'without coding', 'wordpress', 'wix', 'chemical', 'electrical', 'mechanical', 'matlab', 'calculus', 'physics', 'autocad', 'work from home', 'freelancer', 'freelancing', 'blog', 'blogger', 'blogging', 'youtube', 'channel','subscribers', 'powerpoint', 'affinity publisher', 'roboauthor', 'automation', 'microsoft word', 'microsoft excel', 'technician']
    selfD = ['speaking', 'speaker', 'confidence', 'motivation', 'depression', 'writing', 'music', 'guitar', 'piano', 'keyboard', 'psychology', 'happy', 'happier', 'happiness', 'depressed', 'critical thinking', 'innovate', 'language']
    examList = []
    designList = []
    commerceList = []
    marketingList = []
    computerList = []
    technicalList = []
    selfDList = []
    otherList = []
    CourseListCollection = [examList, designList, commerceList, marketingList, computerList, technicalList, selfDList, otherList]
    variableListCollection = [exam, design, commerce, marketing, computer, technical, selfD]

    examHeadline = "Exam/Interview Preparation Courses:\n\n"
    designHeadline = "Design, Animation and Photography:\n\n"
    commerceHeadline = "Business, Finance, Management, HR Courses:\n\n"
    marketingHeadline = "Marketing and Sales Courses:\n\n"
    computerHeadline = "Computer Science:\n\n"
    technicalHeadline = "Other Technical Courses:\n\n"
    selfDHeadline = "Language and Self Development Courses:\n\n"
    otherHeadline = "Other Courses:\n\n"
    headlineList = [examHeadline, designHeadline, commerceHeadline, marketingHeadline, computerHeadline, technicalHeadline, selfDHeadline, otherHeadline]

    courseFileName = fileName
    courseFile = open(courseFileName, "r", encoding="utf-8")
    courseFileData = courseFile.read()
    rawCourseList = courseFileData.split("\n\n")
    courseFile.close()
    print(rawCourseList[0].split("\n"))

    for i in range(len(rawCourseList)-1):
        course = rawCourseList[i]
        courseDetails = course.split("\n")
        print(courseDetails)
        courseTitle = courseDetails[0]
        courseDescription = courseDetails[1]
        courseInfo = courseTitle + " " + courseDescription
        courseInfo = courseInfo.lower()
        i=7
        for variableList in variableListCollection:
            for variable in variableList:
                if variable in courseInfo:
                    i = variableListCollection.index(variableList)
                    break
            if i<7:
                break
        if i<7:
            CourseListCollection[i].append(course)
        else:
            CourseListCollection[6].append(course)

    examFile = open(directoryName + examFileName, "w", encoding="utf-8")
    designFile = open(directoryName + designFileName, "w", encoding="utf-8")
    commerceFile = open(directoryName + commerceFileName, "w", encoding="utf-8")
    marketingFile = open(directoryName + marketingFileName, "w", encoding="utf-8")
    computerFile = open(directoryName + computerFileName, "w", encoding="utf-8")
    technicalFile = open(directoryName + technicalFileName, "w", encoding="utf-8")
    selfDFile = open(directoryName + selfDFileName, "w", encoding="utf-8")
    otherFile = open(directoryName + otherFileName, "w", encoding="utf-8")
    fileList = [examFile, designFile, commerceFile, marketingFile, computerFile, technicalFile, selfDFile, otherFile]
    flag = 0
    for i in range(8):
        if len(CourseListCollection[i])>0:
            currentFile = fileList[i]
            currentHeadline = headlineList[i]
            currentFile.write(currentHeadline)
            for details in CourseListCollection[i]:
                lines = details.split("\n")
                for j in lines:
                    currentFile.write(j)
                    currentFile.write("\n")
                currentFile.write("\n")        
            currentFile.close()
            flag = 1
        if flag==1:
            print("\n" + courseFileNameList[i] + " is now successfully created!\n")
        else:
            print("\n" + courseFileNameList[i] + " has no courses today!")
    print("\n" + courseFileName + " is now successfully classified into sub-files according to the categories!\n")
    
def reorder(fileName, flag=0):
    rawFileName = directoryName + fileName + ".txt"
    oldFileName = directoryName + fileName + "Old.txt"
    reorderedFileName = rawFileName
    rawFile = open(rawFileName, "r", encoding="utf-8")
    rawFileData = rawFile.read()
    oldFile = open(oldFileName, "w", encoding="utf-8")
    oldFile.write(rawFileData)
    oldFile.close()
    rawFile.close()

    reorderedFile = open(reorderedFileName, "w", encoding="utf-8")
    counter = 1
    rawFileData = rawFileData.split("\n")
    for data in rawFileData:
        i = rawFileData.index(data)
        if flag==1:
            if (i+4)%4==0:
                title = data.split(". ")
                data = str(counter) + ". " + title[1]
                counter = counter + 1
        else:
            if i%2==0:
                if (i+4)%4==0:
                    pass
                else:
                    title = data.split(". ")
                    data = str(counter) + ". " + title[1]
                    counter = counter + 1
        reorderedFile.write(data + "\n")
    print("\nFile: " + reorderedFileName + " has been reordered!")
    reorderedFile.close()

def reorderFiles():
    design = "designCourses"
    exam = "examCourses"
    commerce = "commerceCourses"
    marketing = "marketingCourses"
    computer = "computerCourses"
    technical = "technicalCourses"
    selfD = "selfDevelopmentCourses"
    allFiles = [design, exam, commerce, marketing, computer, technical, selfD]
    print("Which file/s would you like to reorder?")
    for i in range(len(allFiles)):
        print(str(i+1) + ". " + allFiles[i])
    print(str(len(allFiles)+1) + ". allFiles")
    print(str(len(allFiles)+2) + ". Custom File")

    choice = int(input("Enter your choice: "))
    flag=0
    if choice==1:
        reorder(design)
    elif choice==2:
        reorder(exam)
    elif choice==3:
        reorder(commerce)
    elif choice==4:
        reorder(marketing)
    elif choice==5:
        reorder(computer)
    elif choice==6:
        reorder(technical)
    elif choice==7:
        reorder(selfD)
    elif choice==8:
        for x in allFiles:
            reorder(x)
    elif choice==9:
        customfileName = input("Enter file name (without extension) to reorder its contents:")
        flag=1
        reorder(customfileName, flag)

def generatePost():
    wFileName = directoryName + "whatsappPost.txt"
    tFileName = directoryName + "telegramPost.txt"
    wFile = open(wFileName, "w", encoding="utf-8")
    tFile = open(tFileName, "w", encoding="utf-8")
    wStart = "_*Date: " + today + "*_\n"
    tStart = "Date: " + today + "\n"
    wEnd = "*Thank you for your Support!*\n*_Join our TELEGRAM channel for more courses:_*\n*https://t.me/freeknowledgesociety/*"
    tEnd = "Thank you for your Support!\nSource: https://t.me/freeknowledgesociety/"
    examFile = open(directoryName + examFileName, "r", encoding="utf-8")
    designFile = open(directoryName + designFileName, "r", encoding="utf-8")
    commerceFile = open(directoryName + commerceFileName, "r", encoding="utf-8")
    marketingFile = open(directoryName + marketingFileName, "r", encoding="utf-8")
    computerFile = open(directoryName + computerFileName, "r", encoding="utf-8")
    technicalFile = open(directoryName + technicalFileName, "r", encoding="utf-8")
    selfDFile = open(directoryName + selfDFileName, "r", encoding="utf-8")
    otherFile = open(directoryName + otherFileName, "r", encoding="utf-8")
    postDataFiles = [examFile, designFile, commerceFile, marketingFile, computerFile, technicalFile, selfDFile, otherFile]

    for i in range(8):
        currentFile = postDataFiles[i]   
        currentFileContent = currentFile.read()
        wFile.write(wStart)
        tFile.write(tStart)
        wFile.write(currentFileContent)
        tFile.write(currentFileContent)
        wFile.write(wEnd)
        tFile.write(tEnd)
        wFile.write("\n\n\n\n")
        tFile.write("\n\n\n\n")
        currentFile.close()
    
    print("WhatsApp and Telegram Posts have been successfully generated!")

def generateBlog():
    examFile = open(directoryName + examFileName, "r", encoding="utf-8")
    designFile = open(directoryName + designFileName, "r", encoding="utf-8")
    commerceFile = open(directoryName + commerceFileName, "r", encoding="utf-8")
    marketingFile = open(directoryName + marketingFileName, "r", encoding="utf-8")
    computerFile = open(directoryName + computerFileName, "r", encoding="utf-8")
    technicalFile = open(directoryName + technicalFileName, "r", encoding="utf-8")
    selfDFile = open(directoryName + selfDFileName, "r", encoding="utf-8")
    postDataFiles = [examFile, designFile, commerceFile, marketingFile, computerFile, technicalFile, selfDFile]
    blogFileName = today + "Blog.html"
    blogFile = open(directoryName + blogFileName, "w", encoding="utf-8")

    for i in range(7):
        currentFile = postDataFiles[i]
        currentFileContent = currentFile.read().split("\n")
        if len(currentFileContent)<5:
            pass
        else:
            title = currentFileContent[0]
            blogTitleCode = "<b><h2>" + title + "</h2></b>\n\n"
            blogBodyCode = ""

            for i in range(2, len(currentFileContent)):
                if (i+4)%4==0:
                    blogBodyCode = blogBodyCode + '<a href=' + currentFileContent[i] + ' target="_self">Click here to enroll for free!</a><br><br>\n'
                elif (i+5)%4==0:
                    blogBodyCode = blogBodyCode + "<i>" + currentFileContent[i] + "</i><br>\n"
                elif (i+6)%4==0:
                    blogBodyCode = blogBodyCode + "<b>" + currentFileContent[i] + "</b><br>\n"
                else:
                    blogBodyCode = blogBodyCode + currentFileContent[i] + "\n"
            currentFile.close()
            blogFile.write(blogTitleCode)
            blogFile.write(blogBodyCode)
    blogFile.close()
    print("Blog Has been successfully generated!")
