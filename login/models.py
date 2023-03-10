from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, id, email, password=None):

        user = self.model(
            id=id,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, email, password=None):
        user = self.create_user(
            id=id,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    email = models.EmailField(
        verbose_name='email address', max_length=255,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    #로그인(id)가 무엇인지 선정
    USERNAME_FIELD = 'id'

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


#python manage.py migrate
#python manage.py makemigrations