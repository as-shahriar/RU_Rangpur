from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from ru.models import User,UserInfo
from django.http import Http404
from django.conf import settings
from search.models import Report,Committee,ResetCode
import smtplib as mail
import random,string, _thread, os
from django.core.paginator import Paginator
from . import auto


EMAIL = 'ru.rangpur.sadar@gmail.com'
PASSWORD = 'ydowsaqxzxbcauli'

@login_required
def search(request):
    object = None
    q = request.GET.get('q')
    btn = request.GET.get('btn')
    if q is not None:
        if btn == 'By Name':
            object = UserInfo.objects.filter(name__icontains = q)
        elif btn == 'By Department':
            object = UserInfo.objects.filter(dept__icontains = q)
        elif btn == 'By Blood Group':
            object = UserInfo.objects.filter(blood__iexact = q)
        elif btn == 'By School':
            object = UserInfo.objects.filter(school__icontains = q)
        elif btn == 'By College':
            object = UserInfo.objects.filter(college__icontains = q)
        elif btn == 'By Session':
            object = UserInfo.objects.filter(session__icontains = q)
        else:
            object = UserInfo.objects.filter(Q(name__icontains = q) | Q(blood__icontains = q) | Q(relation__icontains = q) | Q(dept__icontains = q) | Q(school__icontains = q) |Q(college__icontains = q) |Q(session__icontains = q) |Q(slug__icontains = q) |Q(mobile__icontains = q) |Q(email__icontains = q) |Q(bio__icontains = q) |Q(present_address__icontains = q) |Q(permanent_address__icontains = q)  )
        if object.count() == 0:
            messages.error(request,"User Not Found! Try again!")

    else:
        object = UserInfo.objects.order_by('?')
    return render(request,'search/search.html',{'objects':object})



@login_required
def other_profile(request,slugtxt):
    try:
        object = UserInfo.objects.get(slug = slugtxt)
    except:
        if slugtxt == str(request.user):
            return redirect('profile')
        else:
            raise Http404("No User Found!")
    return render(request,'search/view_profile.html',{'obj':object})


def handler404(request,Exception):
    return render(request, '404.html', status=404)

def report(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        report = request.POST.get('report')
        session = request.POST.get('session')
        dept = request.POST.get('department')
        try:
            new_report = Report()
            new_report.name = name.strip().title()
            new_report.email = email.strip()
            new_report.session = session.strip()
            new_report.dept = dept.strip()
            new_report.report = report.strip()
            new_report.save()
            messages.success(request,"Report successfully submitted! We will contanct as soon as possible.")
            _thread.start_new_thread(send_mail_to_admin,(name,session,dept,email,report))
        except:
            messages.error(request,"Report submission failed!")
    return render(request,'search/report.html')


def error_page(request):
    return render(request,'404.html')

def about(request):
    context,president = None,None
    q = request.GET.get('q')
    if q is not None:
        context = getObj(q,request)
    else:
        context = getObj('error',request)
    return render(request,'search/about.html',context)

def getObj(q,request):
    all = Committee.objects.all()
    for i in all:
        if i.active == True:
            year = i.year
            break
    if q =='error':
        q = year
    try:
        object = Committee.objects.get( year = q )
    except:
        object = Committee.objects.get( year = year )
    finally:
        try:
            president = UserInfo.objects.get(slug = object.president)
        except:
            object = Committee.objects.get( year = year )
            president = UserInfo.objects.get(slug = object.president)
            messages.error(request,"For this Committee, Some member's data is missing! ")
        context = {
              'president':president,
              'all':all,
              'obj':object,
            }
    return context

def pass_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            obj = User.objects.get(email=email)
            code = ''.join(random.sample(string.ascii_letters,6)).upper()
            email = EMAIL
            password = PASSWORD
            link = 'http://127.0.0.1:8000/password-reset/'+obj.username
            profile_link = 'http://127.0.0.1:8000/user/'+obj.username
            to = obj.email
            try:
                mail_obj = mail.SMTP('smtp.gmail.com',587)
                mail_obj.starttls()
                mail_obj.login(email,password)
                sub = 'Reset password'
                content = 'Dear '+str(obj.username)+',\n\nForgot your password? Not to worry!\nYou can change your current password by clicking the link below with the code.\n\nCode: '+code+'\nPassword Reset: '+link+'\nProfile: '+profile_link+'\n\nIf you did not make this request then you can safely ignore this email.\n\nSincerely,\nRangpur Metropolitan Student Welfare Association\nUniversity of Rajshahi'
                msg = 'Subject: '+sub+'\n'+content
                mail_obj.sendmail(email,to,msg)
                mail_obj.quit()
                if ResetCode.objects.filter(username=obj.username).count() == 0:
                    code_obj = ResetCode(username=obj.username,code=code)
                else:
                    code_obj = ResetCode.objects.get(username=obj.username)
                    code_obj.code = code
                code_obj.save()
                return redirect('input_password',username=obj.username)

            except:
                messages.error(request,'Email sending error! Report Now!')
                return redirect('reset')
        except:
            messages.error(request,"No user found!")
    return render(request,'search/pass_reset.html')

def input_password(request,username):

    if ResetCode.objects.filter(username=username).count() == 0:
        return redirect('reset')

    if request.method == 'POST':
        code = request.POST.get('code').strip()
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request,'Password did not match!')
            return redirect('input_password',username=username)
        else:
            try:
                obj = ResetCode.objects.get(username=username)
                if code == obj.code and username == obj.username:
                    user = User.objects.get(username=username)
                    user.set_password(password1)
                    user.save()
                    obj.delete()
                    messages.success(request,'Password changed successfully!')
                    return redirect('login')
                else:
                    messages.error(request,'Code did not match!')
            except:
                raise
    return render(request,'search/input_password.html')
@login_required
def show_all(request):
    obj = UserInfo.objects.order_by('session')
    # auto.get_user(User,UserInfo,30)  # Auto Generate User
    # auto.delete(User)  # Auto all delete User
    return render(request,'search/all.html',{'object':obj})

def send_mail_to_admin(name,session,dept,contact,problem):
    email = EMAIL
    password = PASSWORD
    to ='rifat.rihan.bd@gmail.com'
    try:
        mail_obj = mail.SMTP('smtp.gmail.com',587)
        mail_obj.starttls()
        mail_obj.login(email,password)
        sub = 'New Report'
        content = 'Dear Admin,\n\nYou get New Report!\n\nName: '+name+'\nSession: '+session+'\nDepartment: '+dept+'\nContact: '+contact+'\nProblem: '+problem+'\n\nBy\nSystem\nRangpur Metropolitan Student Welfare Association\nUniversity of Rajshahi'
        msg = 'Subject: '+sub+'\n'+content
        mail_obj.sendmail(email,to,msg)
        mail_obj.quit()
    except:
        pass

@login_required
def see_teachers(request):
    objects = UserInfo.objects.filter(relation__icontains = 'teacher')
    paginator = Paginator(objects, 10)  # Show 10 obj per page

    page = request.GET.get('page')
    objects = paginator.get_page(page)
    context={
        'objects':objects,
        'title': "Teachers"    
    }
    return render(request,'search/teacher_student.html',context)

@login_required
def see_students(request):
    objects = UserInfo.objects.filter(relation__iexact = 'student')
    paginator = Paginator(objects, 10)  # Show 10 obj per page

    page = request.GET.get('page')
    objects = paginator.get_page(page)
    context={
        'objects':objects,
        'title': "Students"
        }
    return render(request,'search/teacher_student.html',context)
@login_required
def see_alumni(request):
    if request.user.is_superuser:
        objects = UserInfo.objects.filter(alumni = True)
        paginator = Paginator(objects, 10)  # Show 10 obj per page

        page = request.GET.get('page')
        objects = paginator.get_page(page)

    
        context={
            'objects':objects,
            'title': "Alumni"
            }
        return render(request,'search/teacher_student.html',context)


    
def download(request):
    fl_path =  os.path.join(os.path.join(settings.STATIC_DIR, 'apk') ,'RMSWA_RU.apk')
    filename = 'RMSWA_RU.apk'
    fl = open(fl_path,'rb')
    response = HttpResponse(fl,content_type='application/vnd.android.package-archive')
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
    