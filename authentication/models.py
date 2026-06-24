from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(
        unique=True
    )
    register_number = models.CharField(
        null=True, unique=True, max_length=12
    )
    department = models.CharField(
        null = True, max_length=3
    )
    graduation_year = models.IntegerField(null=True)
    verified_choices = (
        ('not-verified' , 'Not Verfied'),
        ('pending' , 'Pending'),
        ('verified' , 'Verified')
    )
    roles_choice = ((0, "student"), (1, 'moderator'), (2, 'admin'))
    is_verified = models.CharField(choices=verified_choices, max_length=20, default='not-verified')
    role = models.CharField(choices=roles_choice, null=True, max_length=10, default='student')
    def __str__(self):
        return self.register_number