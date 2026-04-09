from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from User_panel.models import *

# Create your views here.
def Base(request):
    return render(request,'User/Base.html',{})

def Home(request):
    return render(request,'User/Home.html',{})

def About_Us(request):
    return render(request,'User/Aboutus.html',{})

def Services(request):
    return render(request,'User/Services.html',{})

def Contact(request):
    return render(request, 'User/Contact.html',{})

def Contact_Storing(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to DB
        Contact_Data.objects.create(
            Name=name, 
            Email=email, 
            Phone=phone,
            Subject=subject,
            Message=message
            )

#         # 📩 Email to Admin
#         send_mail(
#             subject=f"New Contact - {name}",
#             message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nSubject: {subject}\nMessage: {message}",
#             from_email='zeryons.official@gmail.com',
#             recipient_list=['zeryons.official@gmail.com'],
#         )

#         # 📩 Email to User (Auto Reply)
#         send_mail(
#             subject="Thanks for contacting Zeryons!",
#             message=f"""Hi {name},

# Thank you for contacting Zeryons.

# We’ve received your message and our team will review it shortly. One of our representatives will get back to you as soon as possible.

# If your inquiry is urgent, feel free to reply to this email.

# We appreciate your interest in working with us.

# Best regards,  
# Team Zeryons
#         """,
#             from_email='zeryons.official@gmail.com',
#             recipient_list=[email],
#         )
        messages.success(request, "Message sent successfully!")
        return redirect('/contact')