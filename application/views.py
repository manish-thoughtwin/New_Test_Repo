from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from application.forms import SignupForm
from django.http import HttpResponse
import math, random
from .models import Registration ,Blogs
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import BlogForm


def home(request):
    return HttpResponse("welcome to my home page")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



def generate_otp():
    digits = "0123456789"
    otp = ""
    for _ in range(4):
        otp += digits[math.floor(random.random() * len(digits))]
    return otp

    
    
def login_view(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            otp = generate_otp()
            login(request, user)
            user = Registration.objects.get(email=user.email)
            user.otp = otp  
            user.save() 
            print("uuuuuuuuuuuuuuu",user.otp)

            
            
            subject = 'Your OTP Code'
            message = f'Your OTP code is {otp}.'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            
            try:
                send_mail(subject, message, from_email, recipient_list)
                return redirect('otp_view')
            except Exception as e:
                return HttpResponse(f'Error sending email: {e}')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
    


def otp_view(request):
    if request.method == 'POST':
        number1 = request.POST.get('number1')
        entered_otp = "".join([number1,])
        try:
            user = Registration.objects.last()
            saved_otp = user.otp
            print("check1")
            if int(entered_otp) == saved_otp:
                print("check2")
                return redirect('blog_list') 
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
        except Registration.DoesNotExist:
            messages.error(request, 'Invalid OTP. Please try again.')
    return render(request,'otpverify.html')


def blog_list(request):
    blog = Blogs.objects.all()
    return render(request, 'blog_list.html', {'blog':blog})
  



def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blogs/blog_form.html', {'form': form})



def blog_update(request,id):
    blog = get_object_or_404(Blogs, id=id)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'blog_update.html', {'form': form})


def blog_delete(request, id):
    if request.method == 'POST':
        Blog = Blogs.objects.get(id=id)

        Blog.delete()
        return redirect('Blogs_list')
    return render(request, 'blog_delete.html')








    