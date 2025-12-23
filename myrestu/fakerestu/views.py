import random
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import FeedbackForm
from .models import BookingTable
from .models import FoodDiliver
from .models import CreateNewAccount
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import EmailOTP
from django.conf import settings



# Create your views here.



def home(request):
    
    return render(request,"fakerestu/home.html",{})



def feedback(request):
    
    if request.method=="POST":
        
        # Add Fetch
        
        feed_email=request.POST.get("feed_email")
        feed_name=request.POST.get("feed_name")
        feed_feedback=request.POST.get("feed_feedback")
        feed_review=request.POST.get("feed_review")

        #Create Model obj. & set the obj.

        f=FeedbackForm()
        f.email=feed_email
        f.name=feed_name
        f.feedback=feed_feedback
        f.review=feed_review
        f.save()

        messages.success(request,"✓ Feedback SuccessFully! We'll contact you shortly.")

        return redirect("/fakerestu/feedback/")
        
#return HttpResponse("Feedback Page")
    return render(request,"fakerestu/feedback.html",{})

def homee(request):
    return render(request,"fakerestu/homee.html",{})

def order(request):
    return render(request,"fakerestu/order.html")

def resto_table(request):

    if request.method=="POST":
        
        # Add Fetch
        book_date=request.POST.get("book_date")
        book_time=request.POST.get("book_time")
        book_email=request.POST.get("book_email")
        book_name=request.POST.get("book_name")
        book_phone=request.POST.get("book_phone")
        book_persons=request.POST.get("book_persons")
        book_request=request.POST.get("book_request")

        #Create Model obj. & set the obj.

        b=BookingTable()
        b.persons=book_persons
        b.date=book_date
        b.email=book_email
        b.name=book_name
        b.phone=book_phone
        b.request=book_request
        b.time=book_time
        b.save()

        messages.success(request,"✓ Table booked successfully! We'll contact you shortly.")

        return redirect("table_booking")
    return render(request,"fakerestu/table.html")

def food_dilivered(request):
    if request.method=="POST":
        
        # Add Fetch
        dilv_name=request.POST.get("dilv_name")
        dilv_phone=request.POST.get("dilv_phone")
        dilv_items=request.POST.get("dilv_items")
        dilv_food=request.POST.get("dilv_food")
        dilv_pin=request.POST.get("dilv_pin")
        dilv_address=request.POST.get("dilv_address")
        
        

        #Create Model obj. & set the obj.

        d=FoodDiliver()
        d.name=dilv_name
        d.phone=dilv_phone
        d.items=dilv_items
        d.food=dilv_food
        d.pin=dilv_pin
        d.address=dilv_address
    
        d.save()

        messages.success(request,"✓ Table booked successfully! We'll contact you shortly.")

        return redirect("diliver")
    return render(request,"fakerestu/diliver.html")


def auth(request):
    
    if request.method == "POST":
        u_email = request.POST.get('email')  # HTML input ka name 'email' rakhein
        u_pass = request.POST.get('password') # HTML input ka name 'password' rakhein

        # User check karna
        user = authenticate(request, username=u_email, password=u_pass)

        if user is not None:
            auth_login(request, user)
            return redirect('home_page') # Aapke urls.py mein 'home_page' naam hai
        else:
            messages.error(request, "Error: Incorrect Password!")
            return redirect('auth')
    
    
    return render(request,"fakerestu/auth.html",{})


def create(request):

    if request.method == "POST":
        new_name = request.POST.get("new_name")
        new_email = request.POST.get("new_email")
        new_password = request.POST.get("new_password")

        # Check karein ki user pehle se toh nahi hai
        if User.objects.filter(username=new_email).exists():
            messages.error(request, "Email has already registered!")
            return redirect('create_new_account')

        # Naya account banana (Isse password secure rahega)
        user = User.objects.create_user(username=new_email, email=new_email, password=new_password)
        user.first_name = new_name
        user.save()

        messages.success(request,"✓ Your account is created! we'll go.")

        return redirect("auth")

    return render(request,"fakerestu/create.html",{})

def logout(request):
    logout(request)
    return redirect('auth')
