import datetime

directory = "Course_files\\"
#old_filename = input("Enter the old courses file name (without file extension) where you want tosave everything: ")
old_filename = directory + "allCourses" + ".txt"
#old_filename2 = directory + "udemy_dec_courses" + ".txt"

old_file = open(old_filename, "r", encoding="utf-8")
old_filedata = old_file.read().split("\n")
last_course_number = (len(old_filedata))//4
print(last_course_number)
new_course_number = last_course_number + 1
old_file.close()

present_date = datetime.datetime.now()
new_filename = directory + present_date.strftime("%b") + "_" + str(int(present_date.strftime("%d"))) + "_Courses.txt"
#new_filename = directory + input("Enter the name of the file which you want to copy: ") + ".txt"

new_file = open(new_filename, "r", encoding="utf-8")
new_filedata = new_file.read().split("\n")

old_file = open(old_filename, "a", encoding="utf-8")
#old_file2 = open(old_filename2, "a", encoding="utf-8")

for i in range(len(new_filedata)):
    if ((i+4)%4)==0:
        course_title= new_filedata[i].split(".")[1]
        first_line = str(new_course_number) + "." + course_title
        old_file.write("\n" + first_line)
        #old_file2.write("\n" + first_line)
        new_course_number = new_course_number + 1
    else:
        course_details = new_filedata[i]
        old_file.write("\n" + course_details)
        #old_file2.write("\n" + course_details)

old_file.close()
#old_file2.close()
new_file.close()