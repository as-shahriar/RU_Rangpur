from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from ru.models import User,UserInfo
from ru.forms import UserForm
import smtplib as mail
import datetime, _thread
from search.views import search,EMAIL,PASSWORD
from RU_rangpur.settings import MEDIA_DIR
import os





def login_view(request):
    if request.method == 'POST' and 'login_btn' in request.POST:
        login_username = request.POST.get('username').lower()
        login_password = request.POST.get('password')
        if login_password=="" or login_username=="":
            messages.error(request,"Fill Username and Password!")
        else:
            user = authenticate(username = login_username, password = login_password)
            if user :
                if user.is_active:
                    login(request,user)

                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))

                    return redirect('home')
                else:
                    messages.error(request,"This Id is Blocked!")
            else:
                messages.error(request,"Wrong username or password!")
    return render(request, "ru/login.html")

def signup_view(request):
    if request.method == 'POST' and 'reg_btn' in request.POST:
        reg_username = request.POST.get('username').lower().replace(" ", "")
        reg_password = request.POST.get('password')
        reg_email = request.POST.get('email')
        if reg_email=="" or reg_password =="" or reg_username=="":
            messages.error(request,"Fill Email, Username and Password!")
        elif User.objects.filter(email = reg_email).count() != 0:
            messages.error(request,"email exists! Try another!")
        else:
            try:
                new_user = User()
                new_user.username = reg_username
                new_user.email = reg_email
                new_user.password = reg_password
                new_user.set_password(reg_password)
                new_user.save()
                user = authenticate(username = reg_username, password = reg_password)
                login(request,user)
                _thread.start_new_thread(send_mail_to_admin,('',reg_username))
                _thread.start_new_thread(send_mail_to_user,(reg_email,reg_username))
                return redirect('profile')
            except:
                messages.error(request,"username exists! Try another!")

    return render(request,'ru/signup.html')

def send_mail_to_admin(email_to,username):
    email = EMAIL
    password = PASSWORD
    profile_link = 'http://rmswa.pythonanywhere.com/user/'+username
    to = 'rifat.rihan.bd@gmail.com'
    try:
        mail_obj = mail.SMTP('smtp.gmail.com',587)
        mail_obj.starttls()
        mail_obj.login(email,password)
        sub = 'New Account Created | '+username
        content = 'Dear Admin,\n\nNew Account Created on your site.\n\nUsername: '+username+'\nProfile: '+profile_link+'\n\nBy\nSystem\nRangpur Sadar Student Welfare Association\nUniversity of Rajshahi'
        msg = 'Subject: '+sub+'\n'+content
        mail_obj.sendmail(email,to,msg)
        mail_obj.quit()
    except:
        pass

def send_mail_to_user(email_to,username):
    email = EMAIL
    password = PASSWORD
    profile_link = 'http://rmswa.pythonanywhere.com/user/'+username
    to = email_to
    try:
        mail_obj = mail.SMTP('smtp.gmail.com',587)
        mail_obj.starttls()
        mail_obj.login(email,password)
        sub = 'Your Account Created | '+username
        content = 'Dear '+username+',\n\nYour Account Created on Site.\n\nUsername: '+username+'\nProfile: '+profile_link+'\n\nSincerely,\nRangpur Sadar Student Welfare Association\nUniversity of Rajshahi'
        msg = 'Subject: '+sub+'\n'+content
        mail_obj.sendmail(email,to,msg)
        mail_obj.quit()
    except:
        print('error')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def delete_view(request):
    u = User.objects.get(username = request.user.username)
    try:
        n = UserInfo.objects.get(user = u)
        n.img.delete()
    except:
        pass
    u.delete()
    messages.success(request, "Account deleted successfully!")
    return redirect("signup")

@login_required
def profile(request):
    form = UserForm()
    hasinfo = True

    current_year = datetime.datetime.now().year
    date_list = [str(current_year-1)+' - '+str(current_year)]
    for i in range(2,101):
        date_list.append(str(current_year-i)+' - '+str(current_year-i+1))

    user = User.objects.get(username=request.user)
    try:
        userinfo = UserInfo.objects.get(user = user)
    except:
        hasinfo = False
        userinfo = UserInfo()
        userinfo.user = user
    finally:
        if request.method == 'POST' and 'submit_btn' in request.POST:
            userinfo.slug = user.username
            userinfo.email = request.POST.get('email').strip().lower()
            userinfo.name =  request.POST.get('name')
            userinfo.mobile = request.POST.get('mobile').strip()
            userinfo.present_address= request.POST.get('present_address').strip().title()
            userinfo.permanent_address = request.POST.get('permanent_address').strip().title()
            userinfo.school = request.POST.get('school').strip().title()
            userinfo.college = request.POST.get('college').strip().title()
            userinfo.university = request.POST.get('uni').strip().title()
            userinfo.relation = request.POST.get('relation').strip().title()
            userinfo.father = request.POST.get('father').strip().title()
            userinfo.mother = request.POST.get('mother').strip().title()
            userinfo.bio = request.POST.get('bio').strip()
            userinfo.blood = request.POST.get('blood').strip()
            userinfo.session = request.POST.get('session').strip()
            userinfo.gender = request.POST.get('gender').strip()
            userinfo.dept = request.POST.get('dept').strip()
            userinfo.fb = request.POST.get('fb').strip()
            if request.POST.get('fb').split('/')[2] !='facebook.com':
                messages.error(request,"Invalid facebook URL!")
                return redirect('profile')

            if 'img' in request.FILES :
                extention = str(request.FILES['img']).split('.')[-1]
                if extention.lower() == 'jpg' or extention.lower() == 'jpeg' or extention.lower() == 'png':
                    pass
                else:
                    messages.error(request,"Invalid image format! Use jpg, jpeg or png.")
                    return redirect('profile')

                if  "default.png" not in str(userinfo.img):
                    img_path =  os.path.join(MEDIA_DIR,userinfo.img.name)
                    delete_old_img = True



                userinfo.img = request.FILES['img']

            if request.POST.get('passcheck')=="on":
                user.set_password(request.POST.get('pass'))
            user.email = userinfo.email
            user.save()
            userinfo.save()
            messages.success(request,"Profile Updated!")
            hasinfo = True
            try:
                if delete_old_img:
                    os.remove(img_path)
            except:
                pass

    return render(request,'ru/profile.html',{'hasinfo': hasinfo,'userinfo':userinfo, 'form': form,'date_list':date_list})


@login_required
def home(request):
    object = None
    q = request.GET.get('q')
    btn = request.GET.get('btn')
    if q is not None:
        return search(request)

    else:
        return render(request,'ru/home.html')


