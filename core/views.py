from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(LoginRequiredMixin,View):
    login_url = '/auth/login'
    def get(self, request):
        return render(request, 'core/home.html')
    
class Rules(View):
    def get(self, request):
        return render(request, 'core/rules.html')

class PrivacyPage(View):
    def get(self, request):
        return render(request, 'core/privacy.html')