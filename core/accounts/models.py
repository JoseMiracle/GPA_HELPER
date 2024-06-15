from django.db import models
from core.utils.base_class import BaseModel
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser, BaseModel):

    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=50, null=False, blank=False, unique=True)


    USERNAME_FIELD = "username"

    def __str__(self) -> str:
        return self.email
    


    


