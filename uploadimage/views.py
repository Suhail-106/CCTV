from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import ImageURL
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models  import User
from django.contrib import messages
import random
from django.core.mail import send_mail
from uploadimage.models import contactinfo,CCTVElectrical,datasave


@login_required
def save_image_url(request):
    if request.method == "POST":
        url = request.POST.get('url')
        print("Received URL:", url)  # Debug line
        if url:
            ImageURL.objects.create(user=request.user, url=url)
            return JsonResponse({"message": "URL saved!"})
    return JsonResponse({"error": "Invalid request"}, status=400)



def signup_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        genders = request.POST.get('genders')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        dob = request.POST.get('dob')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request,'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request,'signup.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request,'signup.html')


        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        #extra save
        datasave.objects.create(
           name = name,
           username = username,
           email = email,
           gender = genders,
           password = password,
           confirmpassword = confirm_password,
           DOB = dob
        )
        
        messages.success(request, "Signup successful!")
        return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    error_massage = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            error_massage = '⚠️ Please fill all your details'
            return render(request, 'login.html',{'error_massage':error_massage})

        user = None
        if User.objects.filter(username=email).exists():
            user = User.objects.get(username=email)
        elif User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)   
        else:
            error_massage = '⚠️ User not found. Please check your input.'
            return render(request, 'login.html',{'error_massage':error_massage})

        user_auth = authenticate(request, username=user.username, password=password)

        if user_auth is not None:
            auth_login(request, user_auth)
            

        if user_auth is None:
            error_massage = '⚠️ Invalid password.'
            return render(request, 'login.html', {'error_massage':error_massage})
        
        otp = random.randint(100000,999999)
        
        request.session['otp'] = str(otp)
        request.session['email'] = user.email
        request.session['username'] = user.username

        send_mail(
            subject = 'Your otp code',
            message = f'Hello {user.username},\nYour otp code is: {otp}',
            from_email = '',#This is the place of Email input in inverted comma
            recipient_list = [user.email],
        )
        return redirect('verify_otp')

    return render(request, "login.html",{'error_massage':error_massage})

def verify_otp(request):
    error_message = ''
    username = request.session.get('username') 

    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')

        #extra save
        datasave.objects.update(
            user_otp = user_otp,
            session_otp = session_otp,
        )
        
        if user_otp == session_otp:
            del request.session['otp']
            return redirect('home')
        else:
            error_message = '❌ Invalid OTP. Please try again.'
    return render(request, 'verify_otp.html', {'error_message': error_message})


def index_view(request):
    allCCTVElectrical = CCTVElectrical.objects.all()
    alldatasave = datasave.objects.all()

    context = {
       'CCTVElectrical':allCCTVElectrical,
       'datasave':alldatasave,
       'logged_in':request.user.is_authenticated
    }

    return render(request,'index.html',context)
    


def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']  # agar tum session me kuch store kar rahe ho
    auth_logout(request)  # isse session flush hota hai, isliye alag session setup karna hoga
    return redirect('home')


def formfilling(request):
    error_formfilling = ''
    if request.method == "POST":
        email1 = request.POST.get('email1')
        Name1 = request.POST.get('name1')
        Address1 = request.POST.get('Address1')
        Course1 = request.POST.get('course1')
        massage1 = request.POST.get('massage1')

        if User.objects.filter(email=email1).exists():
            User.objects.get(email=email1)
        else:
            error_formfilling = 'Email not exists please login'
            return render(request,'index.html',{'error_formfilling':error_formfilling})
            
        # Data ko database me save karo
        contactinfo.objects.create(
            email=email1,
            name=Name1,
            address=Address1,
            massage=massage1,
            selectcategory=Course1
        )

        request.session['user_email'] = email1
        request.session['user_name'] = Name1


        # Message body banaiye
        message_body = f"""
New Contact Info Submission:

Name: {Name1}
Email: {email1}
Address: {Address1}
Category: {Course1}
Message: {massage1}
"""

        # Email bhejna
        send_mail(
            subject="your submission",
            message= message_body,
            from_email = 'companypvtltd35@gmail.com',
            recipient_list = ["hasansuhail3666@gmail.com" ]
        )

        send_mail(
            subject="thanks for select my servicing",
            message=f"Have a nice day {Name1} and working start after 1 day and any condition after 1 to 3 days",
            from_email="companypvtltd35@gmail.com",
            recipient_list= [email1]
        )

        return redirect('home')
    return render(request,'index.html')



def edit_view(request, id):
    data = get_object_or_404(datasave, id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        dob = request.POST.get('dob')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'edit.html', {'data': data})
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"username Already exists")

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists") 
            return render(request,"edit.html")   

        # Optionally: email change par OTP verification karne ka logic yahan likh sakte ho
        user_auth = authenticate(request, username = username, email = email,password = password) 

        if user_auth is None:
           user = User.objects.create(
                username = username,
                email = email,
             )
           user.set_password(password)
           user.save()
                      
           datasave.objects.create(
                name=name,
                username = username,
                email = email,
                password = password,
                gender=gender,
                confirmpassword=confirm_password,
                DOB=dob

            )
           return redirect('login')
        # Save changes
        if request.method == 'POST':
        # validation...
           datasave.objects.create(
          name=name,
          username=username,
          email=email,
          gender=gender,
          password=password,
          confirmpassword=confirm_password,
           DOB=dob
         )
     
        messages.success(request, "Profile updated and new record saved!")
        return redirect('home') 

    return render(request, 'edit.html', {'data': data})


def profileedit(request):
    alldatasave = datasave.objects.all()
    return render(request,'profile.html',{'datasave':alldatasave})


def menubar(request):
    allCCTVElectrical = CCTVElectrical.objects.all()
    return render(request,'menu.html',{'CCTVElectrical':allCCTVElectrical,})




def order_view(request):
    user_email = request.session.get('user_email')
    user_name = request.session.get('user_name')
    if user_email:
        orders = contactinfo.objects.filter(email=user_email)
        order_count = orders.count()

        context = {
            'order_count': order_count,
            'user_name': user_name,
            'user_email': user_email,
            'logged_in':request.user.is_authenticated,
        }
        return render(request,'orders.html',context)

    else:
        return render(request, 'orders.html', {
            'order_count': 0,
            'user_name': '',
            'user_email': ''
        })
