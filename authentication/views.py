from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginView(View):

    context = {'error' : ''}

    def post(self, request):

        if request.user.is_authenticated:
            return redirect('/')
        
        user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
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
        checkExist = User.objects.filter(email=request.POST['email']).exists()
        if checkExist:
            self.context['error'] = 'user already exist'
            return redirect('/auth/login')
        else :
            email = request.POST['email']
            register_number, graduation_year, department = decodeEmail(email)
            User.objects.create_user(
                email=email,
                password=request.POST['password'],
                register_number=register_number,
                graduation_year=graduation_year,
                department=department,
                role='student',
            )
            return redirect('/auth/pending')
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'authentication/signup.html')
    
class PendingPage(LoginRequiredMixin,View):
    login_url = '/auth/login'
    def get(self, request):
        if request.user.is_verified == 'verified':
            return redirect('/')
        return render(request, 'authentication/pending.html')

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


