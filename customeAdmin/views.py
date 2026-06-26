from django.shortcuts import render, redirect
from django.views import View
from authentication.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class ShowAllUsers(LoginRequiredMixin, View):
    login_url = '/auth/login'
    def get(self, request):
        context = {
            'users' : ''
        }

        if request.user.role !='admin':
            return redirect('/')
        
        context['users'] = User.objects.all()
        return render(request, 'customeAdmin/users.html', context)

        # return render(request, )

"""
Handle Users is_verified field
1.Approve
2.Pending
3.Reject -> later
"""

class ApproveUser(LoginRequiredMixin, View):
     def post(self, request, pk):
        user = User.objects.get(pk = pk)
        user.is_verified = 'verified'
        user.save()
        return redirect('/dashboard/users')
    
# class that make the user under pending
class InvestigateUser(LoginRequiredMixin, View):
    def post(self, request, pk):
       user = User.objects.get(pk = pk)
       user.is_verified = 'pending'
       user.save()
       context = {'message' : "User Under Investigation"}
       return redirect('/dashboard/users')
    
class DeleteUser(LoginRequiredMixin, View):
    def post(self, request, id):
        user = User.objects.get(pk = id)
        user.delete()
        return redirect('/dashboard/users')
    

class PromoteToModeratorView(View):
    def post(self, request, id):
        user = User.objects.get(pk = id)
        user.role = 'moderator'
        user.save()
        return redirect('/dashboard/users/')
