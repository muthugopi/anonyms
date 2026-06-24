from django.db import models
from authentication.models import User

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=250, null=False)

