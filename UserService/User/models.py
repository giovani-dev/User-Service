import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, user_name, password, is_admin=False, **extra_fields):
        now = timezone.now()
        if not user_name:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, is_admin=is_admin, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, password, **extra_fields):
        user=self._create_user(email, user_name, password, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user


# Create your models here.
class Login(AbstractBaseUser):
    registration_date = models.DateTimeField(auto_now_add=True)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(blank=False, null=False, unique=True, max_length=255)
    user_name = models.CharField(blank=False, null=False, unique=True, max_length=255)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_trusty = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'user_name']

    class Meta:
        db_table = 'login'


class Profile(models.Model):
    registration_date = models.DateTimeField(auto_now_add=True)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    login = models.OneToOneField(Login, null=False, blank=False, related_name='profile_user', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=False, blank=True)

    class Meta:
        db_table = 'profile'