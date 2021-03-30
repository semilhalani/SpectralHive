from CourseFunctions import getCourses, updateFiles, classify, reorderFiles, generatePost, generateBlog

directoryName = "CourseFiles\\"
oldCourseFileName = directoryName + "allCourses.txt"
newCourseFileName = directoryName + "courses.txt"

print("Below are all the available options:")
print("1. Get New Courses for Today")
print("2. Merge today's new courses with all courses")
print("3. Classify the Courses for today")
print("4. Reorder the file contents")
print("5. Generate Posts for today")
print("6. Generate Blog for today")
print("7. All of the above")
print()
option = int(input("What would you like to do?"))

if option==7:
    getCourses(oldCourseFileName, newCourseFileName)
    updateFiles(oldCourseFileName, newCourseFileName)
    classify(newCourseFileName)
    reorderFiles()
    generatePost()
    generateBlog()
elif option==1:
    getCourses(oldCourseFileName, newCourseFileName)
elif option==2:
    updateFiles(oldCourseFileName, newCourseFileName)
elif option==3:
    classify(newCourseFileName)
elif option==4:
    reorderFiles()
elif option==5:
    generatePost()
elif option==6:
    generateBlog()
else:
    print("Error!!!\nKindly recheck your entered choice!\n\nRetry and enter option choice from 1-6 only!")
