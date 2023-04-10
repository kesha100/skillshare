from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import MyUserManager
# Create your models here.


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )

    objects = MyUserManager()

    def __str__(self):
        return self.email