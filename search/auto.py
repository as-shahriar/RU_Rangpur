# from ru.models import User,UserInfo
import random
import string
import datetime


def blood():
    l = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    return l[random.randint(0, 7)]


def session():
    current_year = datetime.datetime.now().year
    date_list = [str(current_year-1)+' - '+str(current_year)]
    for i in range(2, 14):
        date_list.append(str(current_year-i)+' - '+str(current_year-i+1))
    return date_list[random.randint(0, 9)]


def delete(User):
    x = 1
    u = User.objects.all()
    for i in u:
        if i.is_superuser == True:
            pass
        else:
            i.delete()
            print('DELETED '+str(x))
            x += 1


def dept():
    l = ["Philosophy",
         "History",
         "English",
         "Bangla",
         "Islamic History & Culture",
         "Arabic",
         "Islamic Studies",
         "Theatre",
         "Music",
         "Persian language and literature",
         "Sanskrit",
         "Law and Land Administration",
         "Mathematics",
         "Physics",
         "Chemistry",
         "Pharmacy",
         "Population Science & Human Resource Development",
         "Applied Mathematics",
         "Physical Education and Sports Sciences",
         "Accounting and Information Systems",
         "Management studies",
         "Marketing",
         "Finance",
         "Banking and Insurance",
         "Tourism and Hospitality Management",
         "Economics",
         "Political Science",
         "Social Work",
         "Sociology",
         "Mass Communication and Journalism",
         "Information Science & Library Management",
         "Public Administration",
         "Anthropology",
         "Folklore",
         "International Relations",
         "Geography & Environmental Studies",
         ]
    return l[random.randint(0, 35)]


r = ['student', 'teacher', 'student & teacher']


def get_user(User, UserInfo, no):
    for i in range(no):
        u = User()
        userinfo = UserInfo()
        u.username = ''.join(random.sample(string.ascii_letters, 10)).lower()
        u.email = ''.join(random.sample(string.ascii_letters, 5))+'@gmail.com'
        u.password = '123'
        u.save()
        userinfo.user = u
        userinfo.slug = u.username
        userinfo.email = u.email
        userinfo.relation = r[random.randint(0, 2)]
        userinfo.name = ''.join(random.sample(
            string.ascii_letters, 10)).title()
        userinfo.mobile = '017' + \
            ''.join(random.sample(string.digits, 8)).strip()
        userinfo.present_address = ''.join(
            random.sample(string.ascii_letters, 10)).title()
        userinfo.permanent_address = ''.join(
            random.sample(string.ascii_letters, 10)).title()
        userinfo.school = ''.join(random.sample(
            string.ascii_letters, 10)).title()
        userinfo.college = ''.join(random.sample(
            string.ascii_letters, 10)).title()
        userinfo.father = ''.join(random.sample(
            string.ascii_letters, 10)).title()
        userinfo.mother = ''.join(random.sample(
            string.ascii_letters, 10)).title()
        userinfo.fb = 'https://facebook.com/bbc'
        userinfo.bio = ''.join(random.sample(string.ascii_letters, 10)).title()
        userinfo.blood = blood()
        userinfo.session = session()
        userinfo.gender = 'Male'
        userinfo.dept = dept()
        userinfo.save()
        print(i+1)
