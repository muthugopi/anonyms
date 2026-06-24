from django.shortcuts import render, redirect
from django.views import View
from authentication.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class ShowAllUsers(View, LoginRequiredMixin):
    login_url = '/'
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

class ApproveUser(View):
     def post(self, request, pk):
        user = User.objects.get(pk = pk)
        user.is_verified = 'verified'
        user.save()
        return redirect('/dashboard/users')
    
# class that make the user under pending
class InvestigateUser(View):
    def post(self, request, pk):
       user = User.objects.get(pk = pk)
       user.is_verified = 'pending'
       user.save()
       context = {'message' : "User Under Investigation"}
       return redirect('/dashboard/users')
    
