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
class CreatePost(View):
    login_url = '/auth/login/'
    def post(self, request, id):
        data = json.loads(request.body)
        print("Title : " +data['title'])
        user = User.objects.get(id=id)
        new_post = Post(user = user, title = data['title'], description = data['description'])
        new_post.save()
        return redirect('/post/')
    
class ShowPost( View):
    def get(self, request):
        login_url = '/auth/login/'
        context = {
            'posts' : Post.objects.all()
        }
        
        return render(request, 'post/post.html', context)

class DeletePost(View):
    def post(self, request, id):
        post = Post.objects.get(pk=id)
        post.delete()
        return redirect('/post')
