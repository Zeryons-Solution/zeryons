from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test  
from User_panel.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.

def is_admin(user):
    return user.is_staff

@login_required(login_url='admin_login_zeryons')
@user_passes_test(is_admin, login_url='admin_login_zeryons')
def Main(request):
    return render(request, "Admin/main.html", {})

@login_required(login_url='admin_login_zeryons')
@user_passes_test(is_admin, login_url='admin_login_zeryons')
def Header(request):
    return render(request, "Admin/header.html", {})

@login_required(login_url='admin_login_zeryons')
@user_passes_test(is_admin, login_url='admin_login_zeryons')
def Sidebar(request):
    return render(request, "Admin/sidebar.html", {})


@login_required(login_url='admin_login_zeryons')
@user_passes_test(is_admin, login_url='admin_login_zeryons')
def Admin(request):
    return render(request, "Admin/admin.html", {})

@login_required(login_url='admin_login_zeryons')
@user_passes_test(is_admin, login_url='admin_login_zeryons')
def Basic_Form(request):
    return render(request, "Admin/basic form.html", {})

@login_required(login_url='admin_login_zeryons')
@user_passes_test(is_admin, login_url='admin_login_zeryons')
def Basic_Table(request):
    return render(request, "Admin/basic table.html", {})
    
@login_required(login_url='admin_login_zeryons')
@user_passes_test(is_admin, login_url='admin_login_zeryons')
def Contact_Table(request):
    Read = Contact_Data.objects.all()
    context = { 'Display' : Read}
    return render(request, "Admin/contact table.html", context)




def admin_login_zeryons(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/Superior/')  # after login go to dashboard
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'Admin/login-of-admin-for-zeryons-portal.html')


def admin_logout_zeryons(request):
    logout(request)
    return redirect('/Superior/admin_login_zeryons')