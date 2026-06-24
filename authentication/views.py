from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import *

class LoginView(View):

    context = {'error' : ''}

    def post(self, request):

        if request.user.is_authenticated:
            return redirect('/')
        
        user = authenticate(request, username = request.POST['email'], password = request.POST['password'])
        print(user)
        if user is not None : 
            login(request, user)
            # this is the temp render functinon ------------ remove it asap
            return redirect('/')
            # write the redirect code here -> 
            # return redirect()
        else :
            context = {'error' : 'invalid credentials'}
            return render(request, 'authentication/login.html', context)
        
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'authentication/login.html', self.context)


class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('/auth/login')
    
class Signup(View):
    context={'error':''}
    def post(self, request):
        checkExist = User.objects.filter(email = request.POST['email'])
        if checkExist :
            self.context['error'] = 'user already exist'
            return redirect('/auth/login')
        else :
            email = request.POST['email']
            register_number, graduation_year, department = decodeEmail(email)
            new_user = User(email = email, register_number = register_number, graduation_year = graduation_year, department = department, role = 'student')
            new_user.set_password(request.POST['password'])
            new_user.save()
            return redirect('/')
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'authentication/signup.html')

# utils

def decodeEmail(email):
    register_number = email.split('@')[0]
    graduation_year = int(register_number[4:6] )+ 2004
    dept_code = register_number[6:9]
    DEPARTMENTS = {
    "103": "Civil",
    "104": "CSE",
    "105": "EEE",
    "106": "ECE",
    "114": "Mechanical",
    "205": "IT",
}
    department = DEPARTMENTS[dept_code]
    
    return register_number, graduation_year, department
