import json
from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from authentication.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')         
#add the login required mixin after the testing -> this is essential 
class CreatePost(LoginRequiredMixin,View):
    login_url = '/auth/login/'
    def post(self, request, id):
        title = request.POST.get('title')
        description = request.POST.get('description')
        print("Title:", title)
        user = User.objects.get(id=id)
        Post.objects.create(
            user=user,
            title=title,
            description=description
        )
        return redirect('/post/')
    
class ShowPost(LoginRequiredMixin ,View):
    def get(self, request):
        login_url = '/auth/login/'
        context = {
            'posts' : Post.objects.all()
        }
        
        return render(request, 'post/post.html', context)

class DeletePost(LoginRequiredMixin, View):
    def post(self, request, id):
        post = Post.objects.get(pk=id)
        post.delete()
        return redirect('/post')
