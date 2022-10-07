from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
def index(request):
    # context = {
    #      "variable":"This is sent"
    # }
    return render(request, 'index.html' )
    # return HttpResponse("this is home page")
def about(request):
    return render(request, 'about.html')

    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')

    # return HttpResponse("this is service page")
def plastic(request):
    return render(request, 'plastic.html')

def ci(request):
    return render(request, 'ci.html')

def contact(request):
    
    if request.method == "POST":
        #print("This is Post")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        text = request.POST.get("text")
        # contact = Contact(name=name, email=email, contact= contact, disc=disc, date=datetime.today() )
        con = Contact(email = email, text = text , name=name, phone=phone, date=datetime.today())
        text_type =text
        phone_number=phone
        email_from = settings.EMAIL_HOST_USER
        try:
            send_mail(text_type,phone_number,email_from,['hkotadiya001@gmail.com'])
            con.save()
            return redirect('home')
        except:
            return redirect('contact')
         
        messages.success(request, 'Message has been sent.')
    return render(request, 'contact.html')

    #return HttpResponse("this is contact page")
    
# def SaveEnquiry(request):
#     if request.method == "POST":
#         email = request.POST.get["email"]
#         text = request.POST.get["text"]
#         con = Contact(email = email, date=datetime.today())
#         con.save()
#     return render(request, 'contact.html')