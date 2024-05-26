import re
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin

from articon_api.data import REGIONS

# Create your models here.

USER_ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('artisan', 'Artisan'),
    ('client', 'Client')
]


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError("username field is required")
        if email is None:
            raise TypeError("email field is required")
        if password is None:
            raise TypeError("password field is required") #, password=password
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if username is None:
            raise TypeError("username field is required")
        if email is None:
            raise TypeError("password should not be none")
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.role = 'admin'
        user.save()
        return user

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate(registration):
    match = re.match(r"^[CEGR][0-9]{2}[0-9]{4}", registration)
    # self.role=='artisan' and ((role is None)
    if match is None or int(registration[1:3])>24:
        print("registration error")
        raise ValidationError(
            _("%(value)s is not a valid registration number"),
            params={"value": registration},
        )
        
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    fullname = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(unique=True)
    registration = models.TextField(unique=True, validators=[validate])
    role = models.CharField(choices=USER_ROLE_CHOICES, max_length=20, default='client')
    region = models.CharField(choices=REGIONS, max_length=50, default='Tunis')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    objects = UserManager()

    def __str__(self) -> str:
        return f'{self.username} ({self.email})'

    def tokens(self):
        return ''
    
