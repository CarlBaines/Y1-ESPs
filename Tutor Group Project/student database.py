from os import getcwd
from json import dump,load
import time
import random
import string
global letters
global genders
global cwd
global username1
global password1
global malecount
cwd = getcwd()

data = ''
with open(f"{cwd}/studentdetails.json") as file:
    studentdetails = load(file)

def write(studentdetails):
    with open(f"{cwd}/studentdetails.json", 'w') as file:
        dump(studentdetails, file, indent = 1)


letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
genders = ["male","female","prefer not to say","Male","Female"]
forms = ["Canada","Russia","China","UK","Australia","Italy","Germany","Belgium","Albania"]
malecount = 0
femalecount = 0

def random_char ():
    return ''.join(random.choice(string.ascii_letters) for _ in range (7))
                   
username1 = 'mrleeman'
password1 = 'password'
username2 = input("Please enter your username ")
time.sleep(0.2)
password2 = input("Please enter your password ")
if username2 == 'mrleeman' and password2 == 'password':
    time.sleep(0.5)
    option = input("Welcome to the Tree Road School Student Database\nWhat would you like to do?:\n1. Add a new student to the database\n2. Search for a student\n3. Show School Report ")
else:
    print("Invalid login details")
def credentialscheck():
        if option == '1':
            time.sleep(0.2)
            print("Enter the student's details, their student email and ID have been done for you.")
            time.sleep(0.5)
            studentuuid = random.randint(1111111,9999999)
            studentemail = (random_char() + "@tree.ac.uk")
            print("Student ID: " + str(studentuuid))
            print("Student email: " + studentemail)
            time.sleep(0.5)
            global surname
            surname = input("Please enter the student's surname ")
            time.sleep(0.5)
            global forename
            forename = input("Please enter a student's forename ")
            time.sleep(0.5)
            dob = input("Please enter the student's date of birth in the format dd/m/yy ")
            time.sleep(0.5)
            age = int(input("Please enter the student's age "))
            time.sleep(0.5)
            homeaddress = input("Please enter the student's home address ")
            time.sleep(0.5)
            gender = input("Please enter the student's gender (Male/Female) ")
            if gender in genders:
                print("-------------------------------------------")
            else:
                print("Error")
            global form
            form = input("Please enter the student's tutor group ")
            if form in forms:
                print("")
            else:
                print("Invalid tutor group")
            studentdetails [f'Student ID: {studentuuid}'] = {
                "Student email" : studentemail,
                "Student surname": surname,
                "Student forename": forename,
                "Student date of birth": dob,
                "Student age": age,
                "Student home address": homeaddress,
                "Student's tutor group": form,
                "Student's gender": gender}
            write(studentdetails)
            print("-----------------------------------------------")
            enteranotherstudent = input("Do you want to add another student? ")
            if enteranotherstudent == 'y' or enteranotherstudent == 'yes':
                credentialscheck()
            else:
                quit()
        if option == '2':
            studentsearch = input("Enter a student's name? ").split(" ")
            found = False
            for item in studentdetails.keys():
                if studentdetails[item]["Student surname"] == studentsearch[1] and studentdetails[item]["Student forename"] == studentsearch[0]:
                   student = studentdetails[item]
                   found = True
                   print([studentdetails])
                   def append(studentdetails):
                        with open(f"{cwd}/studentdetails.json", 'a') as file:
                            dump(studentdetails, file, indent = 1)
        if option == '3':
            found2 = False
            for item in studentdetails.keys():
                if studentdetails[item]["Student's gender"].lower() == "male":
                    global malecount
                    malecount = malecount + 1
                    
            found3 = False
            for item in studentdetails.keys():
                if studentdetails[item]["Student's gender"].lower() == "female":
                    global femalecount
                    femalecount = femalecount + 1
            found4 = False
            if studentdetails[item]["Student's tutor group"] in forms:
                time.sleep(1)
                print(studentdetails[item]["Student forename"]+ studentdetails[item]["Student surname"] + " is from the tutor group, " + studentdetails[item]["Student's tutor group"])
            print("Tree Road School:\nHas a total of " + str(malecount) + " male students " + "and " + str(femalecount) + " female students")
            
credentialscheck()
    
    
