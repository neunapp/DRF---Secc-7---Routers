from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserMenager


class User(AbstractBaseUser, PermissionsMixin):
    
    MAS = 'M'
    FEM = 'F'
    OTROS = 'O'
    
    GENDER_CHOICES = (
        (MAS, 'Masculino'),
        (FEM, 'Femenino'),
        (OTROS, 'Otros'),
    )
    
    email = models.EmailField(unique=True)
    full_name = models.CharField('Nombres', max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )
    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    token_expired = models.DateTimeField(
        'Token exoired',
        blank=True,
        null=True
    )
    
    objects = UserMenager()
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['full_name']
    
    def get_full_name(self):
        return self.full_name
    